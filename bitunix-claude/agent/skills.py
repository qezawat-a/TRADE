"""
Skills Manager - Agent capabilities
"""

from typing import Dict, Any, List, Optional, Callable
import asyncio
from utils.logger import get_logger

logger = get_logger(__name__)


class SkillManager:
    """
    Manages agent skills (callable functions)
    """
    
    def __init__(self, config):
        self.config = config
        self.skills = {}
        self._register_default_skills()
    
    def _register_default_skills(self):
        """Register default skills"""
        # Market data skills
        self.register("get_market_state", self._get_market_state)
        self.register("get_price", self._get_price)
        self.register("get_ticker", self._get_ticker)
        
        # Position skills
        self.register("get_open_positions", self._get_open_positions)
        self.register("get_position_details", self._get_position_details)
        
        # Trading skills
        self.register("open_position", self._open_position)
        self.register("close_position", self._close_position)
        self.register("adjust_position", self._adjust_position)
        
        # Account skills
        self.register("get_balance", self._get_balance)
        self.register("get_account_info", self._get_account_info)
        
        # Signal skills
        self.register("get_recent_signals", self._get_recent_signals)
        
        logger.info(f"✅ Registered {len(self.skills)} default skills")
    
    def register(self, name: str, skill_func: Callable):
        """Register a new skill"""
        self.skills[name] = skill_func
        logger.debug(f"Skill registered: {name}")
    
    def unregister(self, name: str):
        """Unregister a skill"""
        if name in self.skills:
            del self.skills[name]
            logger.debug(f"Skill unregistered: {name}")
    
    async def execute(self, skill_name: str, **kwargs) -> Any:
        """Execute a skill"""
        if skill_name not in self.skills:
            logger.error(f"Skill not found: {skill_name}")
            return {"error": f"Skill '{skill_name}' not found"}
        
        try:
            skill_func = self.skills[skill_name]
            
            # Execute skill
            if asyncio.iscoroutinefunction(skill_func):
                result = await skill_func(**kwargs)
            else:
                result = skill_func(**kwargs)
            
            return result
            
        except Exception as e:
            logger.error(f"Skill execution failed ({skill_name}): {e}", exc_info=True)
            return {"error": str(e)}
    
    def list_skills(self) -> List[str]:
        """List all available skills"""
        return list(self.skills.keys())
    
    # ==================== DEFAULT SKILL IMPLEMENTATIONS ====================
    # These will be connected to actual services
    
    async def _get_market_state(self) -> Dict:
        """Get current market state"""
        # TODO: Connect to scanner/exchange
        return {
            "status": "placeholder",
            "message": "Market state retrieval not yet connected"
        }
    
    async def _get_price(self, symbol: str) -> Dict:
        """Get current price for symbol"""
        # TODO: Connect to exchange
        return {
            "symbol": symbol,
            "price": 0.0,
            "status": "placeholder"
        }
    
    async def _get_ticker(self, symbol: str) -> Dict:
        """Get ticker data"""
        return {
            "symbol": symbol,
            "status": "placeholder"
        }
    
    async def _get_open_positions(self) -> List[Dict]:
        """Get all open positions"""
        # TODO: Connect to exchange
        return []
    
    async def _get_position_details(self, symbol: str) -> Optional[Dict]:
        """Get details for specific position"""
        return None
    
    async def _open_position(self, **params) -> Dict:
        """Open a new position"""
        logger.info(f"Opening position with params: {params}")
        # TODO: Connect to order manager
        return {"status": "placeholder", "params": params}
    
    async def _close_position(self, symbol: str, **params) -> Dict:
        """Close a position"""
        logger.info(f"Closing position: {symbol}")
        # TODO: Connect to order manager
        return {"status": "placeholder", "symbol": symbol}
    
    async def _adjust_position(self, symbol: str, **params) -> Dict:
        """Adjust a position"""
        logger.info(f"Adjusting position: {symbol}")
        return {"status": "placeholder", "symbol": symbol}
    
    async def _get_balance(self) -> Dict:
        """Get account balance"""
        # TODO: Connect to exchange
        return {
            "total": 0.0,
            "available": 0.0,
            "status": "placeholder"
        }
    
    async def _get_account_info(self) -> Dict:
        """Get account information"""
        return {"status": "placeholder"}
    
    async def _get_recent_signals(self, limit: int = 10) -> List[Dict]:
        """Get recent trading signals"""
        # TODO: Connect to scanner
        return []
    
    def set_exchange(self, exchange):
        """Set exchange client for skills to use"""
        self.exchange = exchange
    
    def set_scanner(self, scanner):
        """Set scanner for skills to use"""
        self.scanner = scanner
    
    def set_order_manager(self, order_manager):
        """Set order manager for skills to use"""
        self.order_manager = order_manager


class Skill:
    """
    Skill decorator for easy skill creation
    """
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
    
    def __call__(self, func: Callable):
        """Decorator to mark function as skill"""
        func._is_skill = True
        func._skill_name = self.name
        func._skill_description = self.description
        return func
