current_hours = int(input())
day_of_week = input()

if day_of_week in ["Monday", "Tuesday",	"Wednesday", "Thursday", "Friday", "Saturday"]:
    if 10 <= current_hours <= 18:
        print("open")
    else:
        print("closed")
elif day_of_week == "Sunday":
    print("closed")