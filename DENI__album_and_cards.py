white_card = float(input("white_card: "))
color_card = float(input("color_car: "))
glue = float(input("glu: "))
decoration = float(input("decoration: "))
card200gr = float(input("card200g: "))
deco_paper = float(input("deco_pape: "))
rezult = 0

price_white_card = white_card * 2.00
price_color_card = color_card * 2.50
price_glue = glue * 4.60
price_decoration =(decoration * 7.00) // 2
price_card200gr = card200gr * 0.17
price_deco_paper = deco_paper * 16.00

album_card = price_white_card + price_color_card +price_glue + price_decoration + price_card200gr + price_deco_paper
print(f"{album_card:.2f}lv. cost of materials")

if album_card > 5:
    result = album_card + (album_card * 1.2)
    print(f"{result}lv. product price")
    pure_profit = result - album_card
    print(f"{pure_profit}lv. pure profit")
else:
    print("litle_pay")