import math

price_videocard = int(input())
price_transition = int(input())
price_electrical = float(input())
price_profit =  float(input())

quantity_card =  price_videocard * 13
quanttity_transition = price_transition *13
money_spent = quantity_card + quanttity_transition + 1000
profit_of_day = abs(price_profit - price_electrical)
total_profit = abs(13 * profit_of_day)
day_of_refund_amount = math.ceil(money_spent / total_profit)
print(money_spent)
print(day_of_refund_amount)




# price_videocard = price_videocard * 13
# price_transition = price_transition * 13
# money_spent = price_videocard + price_transition + 1000
# profit_of_videocard = price_profit - 0.20
# all_profit_videocard = price_videocard *profit_of_videocard
# day_of_profit = math.ceil(money_spent / all_profit_videocard)
# print(day_of_profit)