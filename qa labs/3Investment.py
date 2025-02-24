initial_investment = float(input("what is the initial investment"))
target_value = float(input("what is the target value"))
interest_rate = float(input("what is the interest rate"))

years = 0
current_value = initial_investment

while current_value < target_value:
    current_value += current_value * interest_rate
    years += 1

print(f"It will take {years} years for the investment to grow to £{target_value}.")