import sys
sys.path.append('src')
from DataSource import IEXCloud, Polygon  # noqa autopep8

iex = IEXCloud()
symbols = iex.get_symbols()

# Double redundancy

for symbol in symbols[250:]:
    # 1st pass
    try:
        iex.save_dividends(symbol=symbol, timeframe='5y')
    except Exception as e:
        print(f'IEX Cloud dividend update failed for {symbol}.')
        print(e)

    # 2nd pass
    try:
        iex.save_splits(symbol=symbol, timeframe='5y')
    except Exception as e:
        print(f'IEX Cloud split update failed for {symbol}.')
        print(e)