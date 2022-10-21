chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
vegetarian_price = vegetarian_menu * 8.15
price_sum = chicken_price + fish_price +vegetarian_price
dessert = price_sum - (price_sum * 0.8)

total_sum = price_sum + dessert + 2.50

print(f"Price of order:{total_sum:.2f}")