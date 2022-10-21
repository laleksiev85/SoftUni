from math import floor

tournaments = int(input())
starting_points = int(input())

total_points_from_tournaments = 0
won_tournaments = 0
for n in range(1, tournaments + 1):
    ranking = input()

    if ranking == "W":
        won_tournaments +=1
        points_from_tournament = 2000
        total_points_from_tournaments += points_from_tournament
    elif ranking == "F":
        points_from_tournament = 1200
        total_points_from_tournaments += points_from_tournament
    elif ranking == "SF":
        points_from_tournament = 720
        total_points_from_tournaments += points_from_tournament


total_point = starting_points + total_points_from_tournaments
avarage_points = total_points_from_tournaments/ tournaments
procentage_won_tournaments = won_tournaments/tournaments*100

print(f"Final points: {total_point}")
print(f"Average points: {floor(avarage_points)}")
print(f"{procentage_won_tournaments:.2f}%")