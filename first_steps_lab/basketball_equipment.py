annual_fee = int(input())

shoes = annual_fee - (annual_fee * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes /4
accessories = ball /5

total_sum = annual_fee + shoes + clothes + ball + accessories
print(total_sum)