type_flowers = input()
count_flowers = int(input())
budget = int(input())
total_sum = 0

if type_flowers == "Roses":
     total_sum = 5 * count_flowers
     if count_flowers > 80:
         total_sum = total_sum * 0.90
elif type_flowers == "Dahlias":
     total_sum = 3.80 * count_flowers
     if count_flowers > 90:
         total_sum = total_sum * 0.85
elif type_flowers == "Tulips":
     total_sum = 2.80 * count_flowers
     if count_flowers > 80:
         total_sum = total_sum * 0.85
elif type_flowers == "Narcissus":
     total_sum = 3 * count_flowers
     if count_flowers < 120:
         total_sum = total_sum * 1.15
elif type_flowers == "Gladiolus":
    total_sum = 2.50 * count_flowers
    if count_flowers < 80:
     total_sum = total_sum * 1.20

diff = abs(budget - total_sum)
if total_sum <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")