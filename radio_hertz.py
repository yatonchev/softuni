import winsound


city = input("City ")
hertz = float(input("hertz "))

if city == "Plovdiv":
    if hertz == 87.6:
     print("BNR programa Horizont")
    elif hertz == 88.1:
     print("Radio FM+")
    elif hertz == 89.1:
     print("Radio Fokus")
    elif hertz == 90.6:
     print("Radio Energy")
    elif hertz == 91.1:
     print("Radio City")
    elif hertz == 93.4:
     print("Radio Veronika")
    elif hertz == 94.6:
     print("BG Radio")
    elif hertz == 97.0:
     print("Radio Vitosha")
    elif hertz == 97.7:
     print("Magic")
    elif hertz == 102.0:
     print("Radion N-joy")
    elif hertz == 102.7:
     print("Bulgaria ON AIR")
    elif hertz == 103.3:
     print("Radio Fresh!")
    elif hertz == 103.7:
     print("Z-Rock")
    if 87.6 < hertz < 103.7 and city == "Plovdiv":
     print("You listen toxic signal!")
    elif hertz ==103.7:
     print("You listen God's signal!")
elif city == "Sofia":
    if hertz == 87.6:
       print("Radio Zorana")
    elif hertz == 88.4:
     print("Bulgaria ON AIR")
    elif hertz == 89.1:
     print("Z-Rock")
    elif hertz == 89.5:
     print("Radio Energy")
    elif hertz == 91.0:
     print("Radio Antena")
    elif hertz == 91.9:
     print("BG Radio")
    elif hertz == 92.4:
     print("Magic")
    elif hertz == 92.9:
     print("BR programa Hristo Botev")
    elif hertz == 93.4:
     print("Radio Melody")
    elif hertz == 96.2:
     print("The Voice")
    elif hertz == 96.7:
     print("Radio Veronika")
    elif hertz == 98.3:
     print("Radio 1 Rock")
    elif hertz == 99.1:
     print("Radio Veselina")
    if 87.5 > hertz or hertz > 99.2:
        print("No signal!")
    elif 87.6 < hertz < 89.1 or 89.2 < hertz < 98.3 or 98.4 < hertz < 99.2 and city == "Sofia":
        print("You listen toxic signal!")
    elif hertz == 89.1:
        print("Very good signal!")
else:
    print("I can't find this place!")


    