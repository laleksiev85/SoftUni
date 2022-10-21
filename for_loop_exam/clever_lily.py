age_lily = int(input())
washer = float(input())
toys_price = int(input())

toys_pcs = 0
money_birthdays = 0
total_money_saved = 0

for birthdays in range(1, age_lily + 1 ):

    if birthdays % 2 == 0:
        money_birthdays = money_birthdays + 10
        total_money_saved += money_birthdays - 1

    else:
        toys_pcs += 1

total_money = total_money_saved + toys_price * toys_pcs
diff = abs(total_money - washer)
if total_money >= washer:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")