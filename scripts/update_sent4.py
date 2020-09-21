import sys
sys.path.append('src')
from DataSource import StockTwits  # noqa autopep8
import Constants as C  # noqa autopep8

twit = StockTwits()
symbols = twit.get_symbols()

# Fourth batch
for symbol in symbols[C.TWIT_RATE*3:C.TWIT_RATE*4]:
    try:
        twit.save_social_sentiment(symbol=symbol)
    except Exception as e:
        print(f'Stocktwits sentiment update failed for {symbol}.')
        print(e)
