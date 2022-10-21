import sys

max_number = sys.maxsize
number = 0
while number != "Stop":
    number = input()

    if number == "Stop":
        break

    number = int(number)

    if max_number > number:
        max_number = number

print(max_number)