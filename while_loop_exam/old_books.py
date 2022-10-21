book = input()

count = 0
input_book = input()
isFound = False

while input_book != "No More Books":
    if input_book == book:
        isFound = True
        break

    count += 1
    input_book = input()

if isFound:
    print(f"You checked {count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")