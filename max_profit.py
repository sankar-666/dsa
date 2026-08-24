# def max_profit(prices):
#     min_price = float("inf")
#     profit = 0

#     for price in prices:
#         if price < min_price:
#             min_price = price

#         current_profit = price - min_price
#         profit = max(profit, current_profit)

#     return profit

# print(max_profit([7, 6, 4, 3, 1]))

def max_profit(prices):
    profit = 0
    buy_price = prices[0]

    for price in prices:
        buy_price = min(buy_price, price)

        profit = max(profit, price-buy_price)

    return profit 

print(max_profit([7, 1, 4, 3, 5]))