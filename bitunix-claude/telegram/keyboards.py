"""
Telegram Inline Keyboards
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class TelegramKeyboards:
    """Telegram inline keyboard layouts"""
    
    @staticmethod
    def main_menu() -> InlineKeyboardMarkup:
        """Main menu keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("📊 Status", callback_data="cmd_status"),
                InlineKeyboardButton("💰 Balance", callback_data="cmd_balance")
            ],
            [
                InlineKeyboardButton("📈 Positions", callback_data="cmd_positions"),
                InlineKeyboardButton("📜 History", callback_data="cmd_history")
            ],
            [
                InlineKeyboardButton("🎯 Signals", callback_data="cmd_signals"),
                InlineKeyboardButton("⚙️ Settings", callback_data="cmd_settings")
            ],
            [
                InlineKeyboardButton("🤖 Auto-Trade", callback_data="cmd_autotrade"),
                InlineKeyboardButton("📊 Stats", callback_data="cmd_stats")
            ]
        ]
        
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def autotrade_control() -> InlineKeyboardMarkup:
        """Auto-trade control keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("✅ ON", callback_data="autotrade_on"),
                InlineKeyboardButton("❌ OFF", callback_data="autotrade_off")
            ],
            [
                InlineKeyboardButton("« Back", callback_data="cmd_main")
            ]
        ]
        
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def position_actions(symbol: str) -> InlineKeyboardMarkup:
        """Position action keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("📈 Details", callback_data=f"pos_details_{symbol}"),
                InlineKeyboardButton("🔴 Close", callback_data=f"pos_close_{symbol}")
            ],
            [
                InlineKeyboardButton("🎯 Modify TP/SL", callback_data=f"pos_tpsl_{symbol}"),
                InlineKeyboardButton("💪 Move to BE", callback_data=f"pos_breakeven_{symbol}")
            ],
            [
                InlineKeyboardButton("« Back", callback_data="cmd_positions")
            ]
        ]
        
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def thinking_levels() -> InlineKeyboardMarkup:
        """Thinking level selection"""
        keyboard = [
            [
                InlineKeyboardButton("1️⃣ Quick", callback_data="thinking_1"),
                InlineKeyboardButton("2️⃣ Standard", callback_data="thinking_2"),
                InlineKeyboardButton("3️⃣ Deep", callback_data="thinking_3")
            ],
            [
                InlineKeyboardButton("4️⃣ Expert", callback_data="thinking_4"),
                InlineKeyboardButton("5️⃣ Master", callback_data="thinking_5")
            ],
            [
                InlineKeyboardButton("« Back", callback_data="cmd_settings")
            ]
        ]
        
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def confirm_action(action: str, data: str) -> InlineKeyboardMarkup:
        """Confirmation keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("✅ Confirm", callback_data=f"confirm_{action}_{data}"),
                InlineKeyboardButton("❌ Cancel", callback_data="cancel")
            ]
        ]
        
        return InlineKeyboardMarkup(keyboard)
