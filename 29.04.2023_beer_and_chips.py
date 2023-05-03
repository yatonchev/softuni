import math
name = input()
budjet = float(input())
count_beers = int(input())
count_chips = int(input())

all_sum_beers =  1.20 * count_beers
price_pack_chips = (all_sum_beers / 100) * 45
all_sum_chips =  math.ceil(price_pack_chips * count_chips)
total_sum = all_sum_beers + all_sum_chips
needed_sum = abs(budjet - total_sum)

if total_sum < budjet:
    print(f"{name} bought a snack and has {needed_sum:.2f} leva left.")
elif total_sum > budjet:
    print(f"{name} needs {needed_sum:.2f} more leva!")