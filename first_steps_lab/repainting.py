nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + (paint * 0.1))* 14.50
thinner_price = thinner * 5.00

materials_sum = nylon_price + paint_price + thinner_price + 0.40
price_hours = (materials_sum - (materials_sum * 0.7)) * hours

total_sum = materials_sum + price_hours
print(f"Total price is {total_sum}")

