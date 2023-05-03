#Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
# дали предвидените средства са достатъчни за снимането на филма.
# За снимките ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.

#Известно е, че:
#.Декорът за филма е на стойност 10% от бюджета.
#.При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.
#вход:20000 120 55.5 или 15437.62 186 57.99 или 9587.88 222 55.68 
#изход: Action! Wingard starts filming with 11340.00 leva left. 
#изход: Action! Wingard starts filming with 4186.33 leva left.
#изход: Not enough money! Wingard needs 2495.77 leva more.

budget = float(input())
count_statists = int(input())
price_clothing_one = float(input())

decor = budget * 0.10
all_clothes_price = count_statists * price_clothing_one

if count_statists > 150:
    all_clothes_price = all_clothes_price * 0.90
    
expenses = decor + all_clothes_price

diff = abs(expenses - budget)
if expenses <= budget:
    print("Action!")
    print(f"Wingard starts filming with{diff: .2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs{diff: .2f} leva more.")