price_page_print = float(input())
price_cover_print = float(input())
percent_reduction = int(input())
payment_amount = float(input())
percentage_of_the_total_amount = int(input())

page_cover_sum = (price_page_print * 899) + (price_cover_print * 2)
expenses = (page_cover_sum / 100) * percent_reduction
percent = page_cover_sum - expenses
payment = percent + payment_amount
team_percent = (payment / 100) * percentage_of_the_total_amount 
total_sum = payment - team_percent

print(f"Avtonom should pay {total_sum:.4} BGN.")