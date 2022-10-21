tabs = int(input())
salary = int(input())
sum = 0

for n in range(1, tabs + 1):
    current_web_site = input()

    if current_web_site == "Facebook":
        sum += 150
    elif current_web_site == "Instagram":
        sum += 100
    elif current_web_site == "Reddit":
        sum += 50

diff = abs(salary - sum)

if salary <= sum:
    print("You have lost your salary.")
else:
    print(f"{diff}")