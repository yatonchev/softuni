import math


count_boxes = int(input())
roll_of_wallpaper = int(input())
price_of_gloves = float(input())
price_of_brush = float(input())

price_of_boxes = count_boxes * 21.50
price_of_wallpaper = roll_of_wallpaper * 5.20
count_needed_gloves = math.ceil(0.35 * roll_of_wallpaper)
count_needed_brush = math.floor(0.48 * count_boxes)
sum_of_gloves = count_needed_gloves * price_of_gloves
sum_of_brush = count_needed_brush * price_of_brush
total_sum = price_of_boxes + price_of_wallpaper + sum_of_gloves + sum_of_brush
value_of_supplies = total_sum / 15
print(f"This delivery will cost {value_of_supplies:.2f} lv.")