import os

# Binance API Credentials
API_KEY = os.getenv("BINANCE_API_KEY", "QOuO3VRDh6fnDCOAkgF3eU8akTo2z0n4TYwjMxDJ15wrPmiiYJfcbxmUG4uHjBqr")
API_SECRET = os.getenv("BINANCE_API_SECRET", "iOB7Tp5VRFSKCOxRToF3FkJ4T7R867LrGsCNNdBSE2k6t2pYHUP9eL6qhO2hzmcp")

# System Modes
TESTNET = False  # Live Binance Futures
SAFETY_MODE = True  # Safety First System

# Risk Management
MAX_LEVERAGE = 3
MAX_RISK_PER_TRADE_PCT = 1.0  # 1% Risk per trade
