import math


processors = int(input())
personals = int(input())
working_days = int(input())

hours =  personals * working_days * 8
new_processors = math.floor(hours / 3)
price_of_processors = 110.10
diff = abs(processors- new_processors)
value = diff * price_of_processors
if new_processors < processors:
    print(f"Losses: -> {value:.2f} BGN")
else:
    print(f"Losses: -> {value:.2f} BGN")