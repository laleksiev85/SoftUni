pens_count = int(input())
markers_count = int(input())
detergent_leters = int(input())
discount_percent = int(input())

pen_price = pens_count * 5.80
markers_price = markers_count * 7.20
detergent_price = detergent_leters * 1.20

total_price = pen_price + markers_price + detergent_price
price = total_price - (total_price * (discount_percent/100))

print(price)
