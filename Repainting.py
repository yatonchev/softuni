#Румен иска да пребоядиса хола и за целта е наел майстори.
# Напишете програма, която изчислява разходите за ремонта, предвид следните цени:

# · Предпазен найлон - 1.50 лв. за кв. метър
# · Боя - 14.50 лв. за литър
# . Разредител за боя - 5.00 лв. за литър

# За всеки случай, към необходимите материали, 
# Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон, разбира се и 0.40 лв. за торбички. 
# Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали 

protective_nylon = int(input())
paint = int(input())
paint_thinner = int(input())
working_hour = int(input())

price_of_nylon = (protective_nylon +2 ) * 1.50
price_of_paint = (paint * 1.10) * 14.50
price_of_paint_thinner = paint_thinner * 5

sum =price_of_nylon + price_of_paint +price_of_paint_thinner + 0.40
sum_workers = (sum * 0.30) * working_hour
total_sum = sum + sum_workers
print(total_sum)