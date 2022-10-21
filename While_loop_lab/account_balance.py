payment = 0
total_sum = 0

while payment != "NoMoreMoney":
    payment = input()

    if payment == "NoMoreMoney":
        break
    payment = float(payment)
    if payment < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {payment:.2f}")
    total_sum += payment

print(f"Total: {total_sum:.2f}")