def ArrayChallenge(arr):
    if not arr or len(arr)<2:
        return 0
    min_price=arr[0]
    max_profit=0
    for price in arr[1:]:
        profit=price- min_price
        if profit>max_profit:
            max_profit=profit
        if price<min_price:
            min_price=price
    return max_profit
stock_prices=[44, 30, 24, 32, 35, 30, 40, 38, 16]
print(ArrayChallenge(stock_prices))
