groups = int(input())

Musala = 0
Monbland = 0
Kilimandjaro = 0
K2 = 0
Everest = 0


for n in range(1, groups +1):
    people_in_groups = int(input())

    if people_in_groups <= 5:
        Musala += people_in_groups
    elif 6 <= people_in_groups <= 12:
        Monbland += people_in_groups
    elif 13 <= people_in_groups <= 25:
        Kilimandjaro += people_in_groups
    elif 26 <= people_in_groups <= 40:
        K2 += people_in_groups
    elif people_in_groups >= 41:
        Everest += people_in_groups

total_people = Musala + Monbland + Kilimandjaro + K2 + Everest

claim_musala = Musala/total_people * 100
claim_Monbland = Monbland/total_people * 100
claim_Kilimandjaro = Kilimandjaro/total_people * 100
claim_K2 = K2/total_people * 100
claim_Everest = Everest/total_people * 100

print(f"{claim_musala:.2f}%")
print(f"{claim_Monbland:.2f}%")
print(f"{claim_Kilimandjaro:.2f}%")
print(f"{claim_K2:.2f}%")
print(f"{claim_Everest:.2f}%")