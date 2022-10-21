name_of_student = input()
year = 0
sum_grade = 0
failed_years = 0

while True:
    grade = float(input())
    year += 1


    if grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name_of_student} has been excluded at {year} grade")
            break
        year -= 1

    else:
        sum_grade += grade

        if year == 12:
            avarage_grade = sum_grade / 12
            print(f"{name_of_student} graduated. Average grade: {avarage_grade:.2f}")
            break






