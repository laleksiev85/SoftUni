hours = int(input())
minutes = int(input())

hours = hours * 60
sum = hours + minutes + 15

hours = sum // 60
minutes= sum % 60
if hours == 24:
    hours = hours % 2

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")