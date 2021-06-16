text = input()
symbols = {}

for el in text:
    if el not in symbols:
        symbols[el] = 1
    else:
        symbols[el] += 1

for symbol, times in sorted(symbols.items()):
    print(f'{symbol}: {times} time/s')
