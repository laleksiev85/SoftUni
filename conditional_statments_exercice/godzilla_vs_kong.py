budget = float(input())
statisti = int(input())
price_of_clotes = float(input())
money_left = 0
sum_dekor = budget - (budget*0.9)

if statisti > 150:
    price_of_clotes = price_of_clotes - (price_of_clotes*10/100)

sum_clotes = statisti * price_of_clotes
total_sum = sum_dekor + sum_clotes
money_left = budget-total_sum
if budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {abs(money_left):.2f} leva left.")
elif budget < total_sum:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} leva more.")