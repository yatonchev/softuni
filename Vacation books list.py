#За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги. 
# Понеже Жоро предпочита да играе с приятели навън, 
# вашата задача е да му помогнете да изчисли колко часа на ден трябва да отделя, за да прочете необходимата литература.
# 212 20 2

pages_from_book = int(input())
pages_hour = int(input())
days = int(input())

total_hours = pages_from_book // pages_hour
hour_per_day = total_hours // days
print(hour_per_day)