# Пакет химикали - 5.80 лв.

# Пакет маркери - 7.20 лв.

# Препарат - 1.20 лв (за литър) 
# Цена за всички материали => 11.60 + 21.60 + 4.80 = 38.00 лв. 25% = 0.25 Цена с намаление = 38.00 – (38.00 * 0.25) = 28.50 лв.

from struct import unpack


pack_pan = int(input())

pack_markers = int(input())

pack_cleaner = int(input())

discount_percent = int(input())


price_pack_pan = pack_pan * 5.80
price_pack_markers = pack_markers * 7.20
price_pack_cleaner = pack_cleaner * 1.20

result = price_pack_pan + price_pack_markers + price_pack_cleaner
discount = result * (discount_percent / 100 )
total_price = result -discount
print(total_price)