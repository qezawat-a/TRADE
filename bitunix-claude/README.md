bitunix-ai-agent/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── main.py
│
├── agent/
│   ├── __init__.py
│   ├── core.py                 # Main Agent Logic
│   ├── thinking.py             # Thinking Levels
│   ├── soul.py                 # Agent Personality & Prompts
│   ├── skills.py               # Agent Skills Management
│   ├── mcp.py                  # Model Context Protocol
│   ├── models.py               # AI Models Manager (auto-switch)
│   └── memory.py               # Long-term Memory (Neon DB)
│
├── trading/
│   ├── __init__.py
│   ├── bitunix_client.py       # Bitunix API Client
│   ├── websocket_client.py     # WebSocket Real-time Data
│   ├── position_manager.py     # Position Management
│   ├── order_manager.py        # Order Execution
│   ├── tpsl_manager.py         # Dynamic TP/SL (ATR-based)
│   └── risk_manager.py         # Risk & Money Management
│
├── scanner/
│   ├── __init__.py
│   ├── scanner_engine.py       # Main Scanner Logic
│   └── strategies/
│       ├── __init__.py
│       ├── ema_strategy.py
│       ├── rsi_strategy.py
│       ├── macd_strategy.py
│       ├── volume_strategy.py
│       ├── momentum_strategy.py
│       ├── atr_breakout.py
│       ├── funding_rate.py
│       ├── supertrend.py
│       ├── bollinger.py
│       └── smart_money.py      # 10th strategy
│
├── telegram/
│   ├── __init__.py
│   ├── bot.py                  # Telegram Bot Interface
│   ├── handlers.py             # Command Handlers
│   └── keyboards.py            # Inline Keyboards
│
├── database/
│   ├── __init__.py
│   ├── models.py               # Database Models
│   └── migrations/
│
└── utils/
    ├── __init__.py
    ├── config.py               # Configuration Manager
    ├── logger.py               # Logging System
    └── helpers.py              # Helper Functions
