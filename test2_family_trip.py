# Семейство Иванови планират семейната си почивка. 
# Вашата задача е да напишете програма, която да изчислява дали предвидения
# от тях бюджет ще им стигне, като знаете колко нощувки са планирали, каква е цената за нощувка и колко процента 
# от бюджета са предвидили за допълнителни разходи. 
# Трябва да се има предвид, че ако броят на нощувките е по-голям от 7, цената за нощувка се намаля с 5%.

budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.5
    
costs = number_of_nights * price_per_night
additional_costs = budget * (percent_additional_costs / 100)
total_sum_of_costs = costs + additional_costs

diff_between_budget_and_costs = abs(budget - total_sum_of_costs)

if budget >= total_sum_of_costs:
    print(f"Ivanovi will be left with {diff_between_budget_and_costs:.2f} leva after vacation.")
else:
    print(f"{diff_between_budget_and_costs:.2f} leva needed.")