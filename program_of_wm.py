program = input()
degree_prog = int(input())
time = 1

if program == "Cotton":
    if degree_prog == 1:
        time = time * 195
    elif degree_prog == 2:
        time = time * 145
    elif degree_prog == 3:
        time = time * 230
if program == "Syntetic":
    if degree_prog == 1:
        time == time * 112
    elif degree_prog == 2:
        time == time *  125
if program == "Light Wash":
    if degree_prog == 1:
        time = time *  80
if program == "Every day":
    if degree_prog == 1:
        time = time *  60
if program == "Wool":
    if degree_prog == 1:
        time = time *  80
if program == "Hand wash":
    if degree_prog == 1:
        time = time *  40
if program == "Speed":
    if  degree_prog == 1:
        time = time *  30
if program == "Spin":
    if degree_prog == 1:
         time = time *  20
if program == "Rinsing":
    if degree_prog == 1:
         time = time *  5
         
print(f"You choose program {program}, {degree_prog} - degrre_program and whashing machine is ready for {time} minutes.")