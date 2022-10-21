from math import ceil

name_of_movie = input()
duration_of_the_movie = int(input())
break_duration = int(input())

lunch_time = 1/8 * break_duration
relaxation_time = 1/4 * break_duration

time_left = break_duration - lunch_time - relaxation_time


if time_left >= duration_of_the_movie:
    print(f"You have enough time to watch {name_of_movie} and left with {ceil(time_left - duration_of_the_movie)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {ceil(duration_of_the_movie - time_left)} more minutes.")