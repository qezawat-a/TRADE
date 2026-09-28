"""
Thinking Engine - Multi-level Analysis
"""

from typing import Dict, Any, Optional
import json
from utils.logger import get_logger

logger = get_logger(__name__)


class ThinkingEngine:
    """
    Multi-level thinking system
    Levels 1-5 with increasing depth
    """
    
    def __init__(self, config):
        self.config = config
        
        # Thinking templates for each level
        self.level_templates = {
            1: self._quick_analysis,
            2: self._standard_analysis,
            3: self._deep_analysis,
            4: self._expert_analysis,
            5: self._master_analysis
        }
    
    async def build_prompt(
        self,
        task: str,
        context: Dict[str, Any],
        level: int = 3
    ) -> str:
        """
        Build thinking prompt based on level
        """
        if level not in self.level_templates:
            level = 3
        
        template_func = self.level_templates[level]
        return await template_func(task, context)
    
    async def _quick_analysis(self, task: str, context: Dict) -> str:
        """Level 1: Quick analysis"""
        return f"""
Task: {task}

Quick Analysis Required:
- Make a fast decision based on immediate data
- Focus on most critical factors only
- Respond concisely

Current Data:
{json.dumps(context, indent=2)}

Provide your quick assessment and action.
"""
    
    async def _standard_analysis(self, task: str, context: Dict) -> str:
        """Level 2: Standard analysis"""
        return f"""
Task: {task}

Standard Analysis Required:
1. Review current market conditions
2. Evaluate risk/reward
3. Check for conflicting signals
4. Make balanced decision

Current Data:
{json.dumps(context, indent=2)}

Provide your analysis and recommended action.
"""
    
    async def _deep_analysis(self, task: str, context: Dict) -> str:
        """Level 3: Deep analysis"""
        return f"""
Task: {task}

Deep Analysis Required:

1. Market Context Assessment:
   - What is the overall market structure?
   - What are the key support/resistance levels?
   - What is the current trend strength?

2. Signal Evaluation:
   - How many strategies confirm this signal?
   - What is the confidence level and why?
   - Are there any conflicting indicators?

3. Risk Analysis:
   - What is the risk/reward ratio?
   - What is the liquidation distance?
   - How does this fit our portfolio exposure?

4. Timing Evaluation:
   - Is this the optimal entry point?
   - Should we wait for better conditions?
   - Are we in a cooldown period?

5. Decision Framework:
   - What are the pros and cons?
   - What could go wrong?
   - What is the best action?

Current Data:
{json.dumps(context, indent=2)}

Provide comprehensive analysis with clear reasoning for your decision.
"""
    
    async def _expert_analysis(self, task: str, context: Dict) -> str:
        """Level 4: Expert analysis"""
        return f"""
Task: {task}

Expert-Level Analysis Required:

1. Market Structure Analysis:
   - Multi-timeframe trend alignment
   - Key institutional levels
   - Market regime (trending/ranging/volatile)
   - Volume profile analysis

2. Technical Deep Dive:
   - All indicator confirmations
   - Divergences and anomalies
   - Pattern recognition
   - Support/resistance clusters

3. Risk Management Evaluation:
   - Position sizing optimization
   - Correlation with existing positions
   - Maximum drawdown scenarios
   - Liquidity analysis

4. Behavioral Considerations:
   - Market sentiment indicators
   - Funding rates and open interest
   - Smart money vs retail positioning
   - Recent price action context

5. Strategic Planning:
   - Entry strategy (immediate vs scaled)
   - Exit strategy (TP/SL method selection)
   - Position management plan
   - Contingency scenarios

6. Meta-Analysis:
   - How does this align with recent performance?
   - Are we overtrading or undertrading?
   - Is our strategy adapting properly?
   - What can we learn from this setup?

Current Data:
{json.dumps(context, indent=2)}

Provide expert-level analysis with detailed reasoning, considering all factors and their interactions.
"""
    
    async def _master_analysis(self, task: str, context: Dict) -> str:
        """Level 5: Master analysis"""
        return f"""
Task: {task}

Master-Level Comprehensive Analysis:

1. MACRO MARKET CONTEXT:
   - Global market conditions and correlations
   - Crypto market regime and phase
   - Sector rotation and leadership
   - Volatility regime analysis

2. MULTI-DIMENSIONAL TECHNICAL ANALYSIS:
   - Cross-timeframe structure (1m to 1d)
   - Order flow and market microstructure
   - All technical indicators synthesis
   - Pattern completion probabilities
   - Statistical edge quantification

3. ADVANCED RISK MODELING:
   - Value at Risk (VaR) calculation
   - Portfolio heat and correlation matrix
   - Scenario analysis (best/worst/expected)
   - Kelly criterion position sizing
   - Tail risk assessment

4. MARKET PSYCHOLOGY & SENTIMENT:
   - Funding rate extremes and reversals
   - Open interest changes
   - Long/short ratio analysis
   - Social sentiment indicators
   - Fear & Greed context

5. STRATEGIC EXECUTION PLANNING:
   - Optimal entry methodology
   - TP/SL method selection rationale
   - Position management algorithm
   - Scale-in/scale-out strategy
   - Hedge consideration

6. PERFORMANCE & ADAPTATION:
   - Recent strategy performance review
   - Edge degradation monitoring
   - Market regime fit assessment
   - Behavioral bias check
   - Learning integration

7. META-COGNITIVE REFLECTION:
   - What assumptions am I making?
   - What could I be missing?
   - How confident should I really be?
   - What would change my mind?
   - Is this the best use of capital?

8. DECISION SYNTHESIS:
   - Weighted probability assessment
   - Expected value calculation
   - Confidence intervals
   - Final recommendation with full rationale

Current Data:
{json.dumps(context, indent=2)}

Provide master-level analysis that considers ALL dimensions, questions assumptions, 
and delivers a probabilistic assessment with clear action plan and reasoning.
"""
    
    def parse_response(self, response: str, task: str) -> Dict[str, Any]:
        """
        Parse AI response into structured decision
        """
        # Try to extract structured data from response
        decision = {
            "raw_response": response,
            "task": task,
            "timestamp": None,
            "action": None,
            "params": {},
            "reasoning": response
        }
        
        # Simple parsing - look for keywords
        response_lower = response.lower()
        
        # Detect action
        if "open" in response_lower and "position" in response_lower:
            decision["action"] = "open_position"
        elif "close" in response_lower and "position" in response_lower:
            decision["action"] = "close_position"
        elif "adjust" in response_lower or "modify" in response_lower:
            decision["action"] = "adjust_position"
        elif "wait" in response_lower or "hold" in response_lower or "no action" in response_lower:
            decision["action"] = "wait"
        
        # Try to extract JSON if present
        try:
            if "{" in response and "}" in response:
                start = response.find("{")
                end = response.rfind("}") + 1
                json_str = response[start:end]
                extracted = json.loads(json_str)
                decision["params"] = extracted
        except:
            pass
        
        return decision


# Task-specific thinking prompts
class TaskPrompts:
    """Pre-defined prompts for specific tasks"""
    
    @staticmethod
    def autonomous_trading(context: Dict) -> str:
        """Prompt for autonomous trading cycle"""
        return f"""
You are analyzing the market for autonomous trading opportunities.

Current State:
- Open Positions: {len(context.get('positions', []))}
- Recent Signals: {len(context.get('signals', []))}
- Market Conditions: {context.get('market_state', {})}

Evaluate:
1. Should we open any new positions based on current signals?
2. Do any existing positions need adjustment?
3. Should we close any positions early?
4. Or should we wait for better opportunities?

Consider:
- Risk management (current exposure, correlations)
- Signal quality and confidence
- Market conditions and volatility
- Recent performance

Provide your decision with clear reasoning.
"""
    
    @staticmethod
    def signal_evaluation(context: Dict) -> str:
        """Prompt for signal evaluation"""
        signal = context.get('signal', {})
        
        return f"""
Evaluate this trading signal:

Symbol: {signal.get('symbol')}
Direction: {signal.get('signal')}
Confidence: {signal.get('confidence')}%
Entry Price: {signal.get('entry_price')}
Strategies Agreeing: {signal.get('strategies', [])}

Should we:
1. Take this trade immediately?
2. Wait for better confirmation?
3. Ignore this signal?

Consider:
- Confidence level vs our threshold
- Number of confirming strategies
- Current market conditions
- Risk/reward potential
- Our current exposure

Make your recommendation.
"""
    
    @staticmethod
    def risk_assessment(context: Dict) -> str:
        """Prompt for risk assessment"""
        return f"""
Assess the current risk situation:

Portfolio:
- Total Positions: {context.get('position_count', 0)}
- Total Exposure: {context.get('total_exposure', 0)} USDT
- Unrealized PnL: {context.get('unrealized_pnl', 0)} USDT

Proposed Trade:
{json.dumps(context.get('proposed_trade', {}), indent=2)}

Evaluate:
1. Is the risk acceptable?
2. Are we over-exposed?
3. Should we reduce position size?
4. Any correlation risks?

Provide risk verdict: APPROVED, REDUCE_SIZE, or REJECTED with reasoning.
"""
