# Времето се затопля и туристите започват да си правят разходки високо в планината,
# където все още има сняг, като за целта те трябва да закупят нужната туристическа
# екипировка.
# Вашата задача е да напишете програма, която да изчислява,
# стойността на екипировката, както и дали определения бюджет е достатъчен или не,
# #като се знае, че в магазина има следната промоция:
# Всеки трети продукт е на половин цена.

# Вход
# От конзолата се чете:
# · На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
# · След това поредица от два реда 
# (до получаване на команда "Stop" или при заявка за купуване на продукт, чиято стойност е по-висока от наличния бюджет) :
# . Име на продукта – текст
# . Цена на продукта – реално число в интервала [1.00… 5000.00]

budget = float(input())
costs = 0
counter_of_products = 0
budget_condition = False
needed_money =0

while True:
    name_of_product = input()
    
    if name_of_product == "Stop":
       break

    product_price = float(input())

    counter_of_products += 1

    if counter_of_products % 3 == 0:
       product_price /= 2
    
    if product_price > budget:
        budget_condition = True
        needed_money = product_price - budget
        counter_of_products -= 1
        break

    costs += product_price
    budget -= product_price

if not budget_condition:
   print(f"You bought {counter_of_products} products for {costs:.2f} leva.")
else:
    print(f"You don't have enough money!\nYou need {needed_money:.2f} leva!")