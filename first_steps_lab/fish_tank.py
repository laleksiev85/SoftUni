length = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_volume = length * width * height
tank_volume_lt = tank_volume / 1000

total_lt_water = tank_volume_lt - (tank_volume_lt * (percent/100))
print(total_lt_water)