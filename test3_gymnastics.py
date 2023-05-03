# На световно първенство по художествена гимнастика три от 
# държавите се изявяват като лидери в класирането (Русия, България, Италия).
# Вашата задача е да изчислите каква е оценката дадена от журито за конкретно 
# съчетание, като знаете държавата, която е играла и с кой уред е играла
# - лента, обръч или въже. За съчетанието си, отбора е получил две оценки:
# оценка за трудност и оценка за изпълнение на съчетанието, като крайната оценка е 
# сбор на двете оценки. 
# В таблицата са показани какви оценки за трудност и изпълнение са получили ансамблите
# за всеки един уред.

# Уред            Русия                             България                         Италия

# Лента (ribbon) Трудност: 9.100 Изпълнение: 9.400 Трудност: 9.600 Изпълнение: 9.400 Трудност: 9.200 Изпълнение: 9.500

# Обръч (hoop) Трудност: 9.300 Изпълнение: 9.800 Трудност: 9.550 Изпълнение: 9.750 Трудност: 9.450 Изпълнение: 9.350

# Въже (rope) Трудност: 9.600 Изпълнение: 9.000 Трудност: 9.500 Изпълнение: 9.400 Трудност: 9.700 Изпълнение: 9.150

country = input()
device = input()

difficulty = 0
evaluation = 0

if country == "Russia":
    if device == "ribbon":
        difficulty = 9.1
        evaluation = 9.4
    elif device == "hoop":
        difficulty = 9.3
        evaluation = 9.8
    elif device == "rope":
        difficulty = 9.6
        evaluation = 9
    
elif  country == "Bulgaria":
    if device == "ribbon":
        difficulty = 9.6
        evaluation = 9.4
    elif device == "hoop":
        difficulty = 9.55
        evaluation = 9.75
    elif device == "rope":
        difficulty = 9.5
        evaluation = 9.4
    
elif  country == "Italy":
    if device == "ribbon":
        difficulty = 9.2
        evaluation = 9.5
    elif device == "hoop":
        difficulty = 9.45
        evaluation = 9.35
    elif device == "rope":
        difficulty = 9.7
        evaluation = 9.15
        
total_score = difficulty + evaluation
needed_percent = ((20 -total_score) / 20) * 100
print(f"The team of {country} get {total_score:.3f} on {device}.")
print(f"{needed_percent:.2f}%")