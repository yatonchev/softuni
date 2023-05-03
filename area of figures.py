from cmath import pi


type_of_figure = input()
result = 0

if type_of_figure == "square":
    side = float(input())
    result = side * side
elif type_of_figure == "rectangle":
    fisrt_side = float(input())
    second_side = float(input())
    result= fisrt_side * second_side
elif type_of_figure == "circle":
    radius = float(input())
    result = pi * (radius * radius)
elif type_of_figure == "triangle":
    side = float(input())
    heigh = float(input())
    result = side * heigh / 2
print(f"{result:.3f}")