price_page = float(input())
price_cover = float(input())
percent_reduction_page = int(input())
payment_amount = float(input())
percent_all_sum = int(input())

start_sum = price_page * 899 + price_cover * 2
reduction = (start_sum / 100) * percent_reduction_page 
new_reduction = start_sum - reduction
designer_costs = new_reduction + payment_amount
team_reduction = (designer_costs / 100) * percent_all_sum
new_team_reduction = designer_costs - team_reduction
print(F"Avtonom should pay {new_team_reduction:.2f} BGN.")