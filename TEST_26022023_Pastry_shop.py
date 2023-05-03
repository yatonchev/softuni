jam = input()
count =  int(input())
day_from_december = int(input())
price = 0
total_count_sum = 1

if day_from_december <= 15:
    if jam == "Cake":
     price = 24
    elif jam == "Baklava":
     price = 12.60
    elif jam == "Soufle":
     price = 6.66
elif day_from_december > 15:
    if jam == "Cake": 
     price = 28.70
    elif jam == "Soufle":
     price = 9.80
    elif jam == "Baklava":
     price = 16.98
    
price_jam = count * jam
200 < price_jam
percent_count_sum = (price_jam / 100 ) * 25
total_count_sum = (price_jam - percent_count_sum) * 0.90
print(total_count_sum)