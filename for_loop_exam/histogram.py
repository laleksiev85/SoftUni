n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    current_number = int(input())

    if current_number < 200:
        p1 += 1
    elif current_number <= 399:
        p2 += 1
    elif current_number <= 599:
        p3 += 1
    elif current_number <= 799:
        p4 += 1
    else:
        p5 += 1

p1_= p1 / n * 100
p2_= p2 / n * 100
p3_= p3 / n * 100
p4_= p4 / n * 100
p5_= p5 / n * 100

print(f"{p1_:.2f}%")
print(f"{p2_:.2f}%")
print(f"{p3_:.2f}%")
print(f"{p4_:.2f}%")
print(f"{p5_:.2f}%")
