stock_prices = []
with open("","r") as f:
    for sentence in f:
        tokens = sentence.split(',')
        day = tokens[0]
        price = tokens[1]
        stock_prices.append([day,price])

print(stock_prices)

for element in stock_prices:
    if element[0] == 'apple':
        print(element[1])