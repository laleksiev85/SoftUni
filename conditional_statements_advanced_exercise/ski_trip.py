days = int(input())
type_of_room = input()
rating = input()

nigth = days - 1
price = 0

if type_of_room == "room for one person":
    price = nigth * 18

elif type_of_room == "apartment":
    price = nigth * 25
    if days <= 10:
        price = price * 0.70
    elif 10 < days <= 15:
        price = price * 0.65
    elif days > 15:
        price = price * 0.50
elif type_of_room == "president apartment":
    price = nigth * 35
    if days <= 10:
        price = price * 0.90
    elif 10 < days <= 15:
        price = price * 0.85
    elif days > 15:
        price = price * 0.80

if rating == "positive":
        price = price * 1.25
else:
        price = price * 0.90

print(f"{price:.2f}")