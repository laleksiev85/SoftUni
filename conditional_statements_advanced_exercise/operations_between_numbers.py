N1 = int(input())
N2 = int(input())
operator = input()

result = 0
even_or_odd = ""

if operator == "+":
    result = N1 + N2
elif operator == "-":
    result = N1 - N2
elif operator == "*":
    result = N1 * N2
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2

if operator in ["+", "-", "*"]:
    even_or_odd = result % 2 == 0
    if even_or_odd == True:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
elif operator == "/":
    if N2 == 0:
        pass
    else:
        print(f"{N1} / {N2} = {result:.2f}")
elif operator == "%":
    if N2 == 0:
        pass
    else:
        print(f"{N1} % {N2} = {result}")


