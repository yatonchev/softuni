import math

width = float(input())
length = float(input())
height =  float(input())
height_astronaut =float(input())

spacecrat = width * length * height
room = (height_astronaut + 0.40) * 2 * 2
astronaut_space = math.floor(spacecrat / room)

if  3 < astronaut_space < 10:
     print(f"The spacecraft holds {astronaut_space} astronauts.")
elif astronaut_space < 3:
    print("The spacecraft is too small.")
elif astronaut_space > 10:
    print("The spacecraft is too big.")