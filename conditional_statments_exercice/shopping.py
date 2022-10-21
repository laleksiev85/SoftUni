budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = video_cards * 250
processors_price = video_cards_price * 35/100
ram_price = video_cards_price * 10/100

total_processors = processors * processors_price
total_ram = ram * ram_price
total_sum = video_cards_price + total_processors + total_ram


if video_cards > processors:
    total_sum = total_sum - (total_sum*15/100)

left = budget - total_sum

if budget >= total_sum:
    print(f"You have {abs(left):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(left):.2f} leva more!")