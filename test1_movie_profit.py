# Наети сте от "SoftUni Studios" да напишете програма, която
# пресмята потенциалната печалба от продажбата на билети за филм. 
# Прожекцията на филма трае предварително зададен брой дни, 
# като всеки ден се продават определен брой билети. 
# Цената на 1 билет се определя от студиото. За излъчване на продукцията,
# определен процент от общия приход остава за киното.


name_of_movie = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_ticket = float(input())
percent_for_cinema = int(input())

profit_per_day = number_of_tickets * price_per_ticket
total_profit = profit_per_day * number_of_days
total_profit -= total_profit * (percent_for_cinema / 100)

print(f"The profit from the movie {name_of_movie} is {total_profit:.2f} lv.")