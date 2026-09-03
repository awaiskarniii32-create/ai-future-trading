import ccxt
import config

def initialize_bot():
    print("Initializing Binance Futures Trading Bot...")
    exchange = ccxt.binance({
        'apiKey': config.API_KEY,
        'secret': config.API_SECRET,
        'options': {
            'defaultType': 'future',
        },
    })
    
    if config.TESTNET:
        exchange.set_sandbox_mode(True)
        print("Running in TESTNET mode.")
    else:
        print("Running in LIVE mode.")
        
    return exchange

if __name__ == "__main__":
    bot = initialize_bot()
    print("Bot initialized successfully!")
  
