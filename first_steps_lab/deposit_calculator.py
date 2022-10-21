amount_deposited = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())

sum = amount_deposited + term_of_the_deposit *((amount_deposited * (annual_interest_rate/100))/12)

print(sum)