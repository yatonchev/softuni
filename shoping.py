# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. 
# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка.
# Важат следните цени:

# · Видеокарта – 250 лв./бр.
# · Процесор – 35% от цената на закупените видеокарти/бр.
# · Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

#Вход: 900 2 1 3 И 920.45 3 1 1 

#Изход: You have 198.75 leva left! И Not enough money! You need 3.92 leva more!

budget = float(input())
video_count = float(input())
cpu_count = float(input())
ram_count = float(input())

video_sum = video_count * 250
cpu_sum = cpu_count * (video_sum * 0.35)
ram_sum = ram_count * (video_sum * 0.10)

all_sum = video_sum + cpu_sum + ram_sum

if video_count > cpu_count:
    all_sum = all_sum * 0.85
    
diff = abs(budget - all_sum)
if all_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")    