import math

record_seconds = float(input())
distance_meters = float(input())
swimming_time = float(input())
time=0

if distance_meters >= 15:
    time = math.floor(distance_meters/15) * 12.5

total_time = distance_meters * swimming_time + time
diferance = record_seconds - total_time

if record_seconds > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(diferance):.2f} seconds slower.")


