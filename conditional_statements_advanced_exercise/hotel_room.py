month = input()
nights = int(input())

price_apartament = 0
price_studio = 0

if month == "May" or month == "October":
    price_studio = nights * 50
    price_apartament = nights * 65
    if 7 < nights <= 14 :
        price_studio = price_studio * 0.95
    elif nights > 14:
        price_studio = price_studio * 0.70
elif month == "June" or month == "September":
    price_studio = nights * 75.20
    price_apartament = nights * 68.70
    if nights > 14:
        price_studio = price_studio * 0.80
elif month == "July" or month == "August":
    price_studio = nights * 76
    price_apartament = nights * 77

if nights > 14:
    price_apartament = price_apartament * 0.9

print(f"Apartment: {price_apartament:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")