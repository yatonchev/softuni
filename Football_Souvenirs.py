team = input()
souvenirs = input()
count_souvenirs = int(input())

price = 0

if team == "Argentina":
    if souvenirs == "flags":
       price = 3.25
    elif souvenirs == "caps":
        price =  7.20
    elif souvenirs == "tent":
        price =  5.10
    elif souvenirs == "stickers":
        price = 1.25
elif team == "Brazil":
    if souvenirs == "flags":
       price =  4.20
    elif souvenirs == "caps":
        price =  8.50
    elif souvenirs == "tent":
        price =  5.35
    elif souvenirs == "stickers":
        price =  1.20
elif team == "Croatia":
    if souvenirs == "flags":
       price =  2.75
    elif souvenirs == "caps":
        price =  6.90
    elif souvenirs == "tent":
        price =  4.95
    elif souvenirs == "stickers":
        price =  1.10
elif team == "Denmark":
    if souvenirs == "flags":
       price =  3.10
    elif souvenirs == "caps":
        price =  6.50
    elif souvenirs == "tent":
        price =  4.80
    elif souvenirs == "stickers":
        price =  0.90
        
choose = count_souvenirs * price
print(choose)