# Деси много обича да гледа филми, но често й е трудно да си избере подходящ за гледане. 
# Набелязва си определен брой филми и иска да си избере кой филм да гледа спрямо рейтинга на филмите.
# Напишете програма, която показва кой филм е с най-висок рейтинг, кой е с най-нисък и колко е средният рейтинг от всички 
# филми, които си е набелязала да гледа.
# Вход
# От конзолата първо се чете един ред:
# · Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
# За всеки филм се прочитат два отделни реда:
# · Име на филма – текст
# · Рейтинг на филма - реално число в интервала [1.00…10.00]
import sys

number_of_movies = int(input())
low_rating_movie_name = " "
low_rating = sys.maxsize
max_rating_movie_name = " "
max_rating = -sys.maxsize
sum_of_ratings = 0

for count in range(number_of_movies):
    name_of_movie = input()
    current_movie_rating = float(input())
    
    sum_of_ratings += current_movie_rating
    
    if current_movie_rating > max_rating:
        max_rating = current_movie_rating
        max_rating_movie_name = name_of_movie
    
    if current_movie_rating < low_rating:
        low_rating = current_movie_rating
        low_rating_movie_name = name_of_movie
        
average_rating = sum_of_ratings / number_of_movies

print(f"{max_rating_movie_name} is with highest rating: {max_rating:.1f}")
print(f"{low_rating_movie_name} is with lowest rating: {low_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")