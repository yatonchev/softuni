#Петя има магазин за детски играчки.
# Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.
#Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# вход: 40.8 20 25 30 50 10 или 320 8 2 5 5 1
# Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# Брой пъзели - цяло число в интервала [0… 1000]
# Брой говорещи кукли - цяло число в интервала [0 … 1000]
# Брой плюшени мечета - цяло число в интервала [0 … 1000]
# Брой миньони - цяло число в интервала [0 … 1000]
# Брой камиончета - цяло число в интервала [0 … 1000]
#изход: Yes! 418.20 lv left. или Not enough money! 238.73 lv needed.

trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

#total_sum = (puzzle_count * 2.60) + (dolls_count * 3) + (bears_count * 4.10) + (minions_count * 8.20) + (trucks_count * 2)
price_puzzle = puzzle_count * 2.60
price_dolls =  dolls_count * 3
price_bears =  bears_count * 4.10
price_minions = minions_count * 8.20
price_trucks = trucks_count * 2
total_sum = price_puzzle + price_dolls +price_bears + price_minions +price_trucks
all_count = puzzle_count + dolls_count + bears_count + minions_count + trucks_count


if all_count >= 50:
    total_sum = total_sum * 0.75
    
total_sum = total_sum - (total_sum * 0.10)

diff = abs(total_sum - trip_price)
if total_sum >= trip_price:
    print(f"Yes!{diff: .2f} lv left.")
else:
    print(f"Not enough money!{diff: .2f} lv needed.")