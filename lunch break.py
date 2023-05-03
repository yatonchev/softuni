# По време на обедната почивка искате да изгледате епизод от своя любим сериал. 
# Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих. 
# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход:Game of Thrones 60 96 и 48 60

from math import ceil


name_of_movie = input()
movie_time = int(input())
all_time = int(input())


lunch_time = all_time / 8
time_relax = all_time / 4

after_time = all_time - lunch_time - time_relax

diff = abs(after_time - movie_time)
rounded_diff = ceil(diff)
if after_time >= movie_time:
    print(f"You have enough time to watch {name_of_movie} and left with {rounded_diff} minutes free time.")
else: 
    print(f"You don't have enough time to watch {name_of_movie}, you need {rounded_diff} more minutes.")
