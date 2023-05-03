city = input("City ")
factory = input("Factory ")
shop = input("Shop ")

furniture = input("furniture ")
# wardrobe = int(input("Wardrobe "))
# cabinet = int(input("Cabinet "))
# bed = int(input("bed "))
price = 1
total_price = 0
flag = "Wardrobe"
if city == "Sofia":
    if factory == "Bulgaria":
        if shop == "Enikom":
            if furniture == "Wardrobe":
                price = price * 830
            elif furniture == "cabinet":
                price = price * 80
            elif furniture == "bed":
                price = price * 430
                
            while furniture != "cabinet":
                for num in range(1,3,10):
                    print("Price new furniture")
                    flag = False
                    continue 
            if furniture != "cabinet":
                   print("Buy bed!")
print(f"You visit {city} buy {furniture} from {factory} in {shop}")