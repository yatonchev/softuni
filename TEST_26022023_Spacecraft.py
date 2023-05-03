import math

width = float(input())
length = float(input())
height = float(input())
astronaut_height = float(input())

all_space = width * length * height
space_room = (astronaut_height + 0.40) * 2 * 2
space_for = math.floor(all_space / space_room)
if 3 <= space_for <= 10:
    print(f"The spacecraft holds {space_for} astronauts.")
elif space_for < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")