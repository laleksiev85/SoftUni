name_of_actor = input()
points_from_academy = float(input())
appreciative_count = int(input())

total_points = points_from_academy

for n in range(1, appreciative_count + 1):
    name_of_appreciative = input()
    point_from_appreciative = float(input())

    total_points_from_appreciative = (point_from_appreciative * len(name_of_appreciative) ) / 2
    total_points += total_points_from_appreciative
    if total_points >= 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = abs(total_points - 1250.5)
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")


