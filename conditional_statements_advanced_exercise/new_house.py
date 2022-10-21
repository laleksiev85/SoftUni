kind_of_flowers = input()
quantity = int(input())
budget = int(input())

sum = 0

if kind_of_flowers == "Roses":
    sum = quantity * 5
    if quantity >80:
        sum = sum * 0.9
elif kind_of_flowers == "Dahlias":
    sum = quantity * 3.80
    if quantity >90:
        sum = sum * 0.85
elif kind_of_flowers == "Tulips":
    sum = quantity * 2.80
    if quantity > 80:
        sum = sum * 0.85
elif kind_of_flowers == "Narcissus":
    sum = quantity * 3
    if quantity < 120:
        sum = sum * 1.15
elif kind_of_flowers == "Gladiolus":
    sum = quantity * 2.50
    if quantity < 80:
        sum = sum * 1.20
diff = abs(budget - sum)

if budget >= sum:
    print(f"Hey, you have a great garden with {quantity} {kind_of_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")