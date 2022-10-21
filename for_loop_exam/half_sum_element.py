import sys

n = int(input())
sum_all_numbers = 0
bigger_number = - sys.maxsize

for i in range(1, n + 1):
    current_number = int(input())

    if bigger_number < current_number:
        bigger_number = current_number

    sum_all_numbers = sum_all_numbers + current_number

total_sum = sum_all_numbers - bigger_number

if total_sum == bigger_number:
    print("Yes")
    print(f"Sum = {total_sum}")
else:
    print("No")
    diff = abs(total_sum - bigger_number)
    print(f"Diff = {diff}")