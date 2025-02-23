import matplotlib.pyplot as plt
import math

def getIncomeTax(salary):
    
    # calculate the income tax for a salary based on:
    # personal allowance: £11,850 (no tax)
    # next £34,500 taxed at 20%
    # income from £34,501 to £150,000 taxed at 40%
    # income over £150,000 taxed at 45%
    
    personal_allowance = 11850
    band1_limit = 34500
    band1_rate = 0.20
    band2_rate = 0.40
    band3_rate = 0.45

    # No tax if salary is within the personal allowance
    if salary <= personal_allowance:
        return 0

    taxable_income = salary - personal_allowance
    tax = 0

    # Income in first tax band
    if taxable_income <= band1_limit:
        tax = taxable_income * band1_rate
    # Income in second tax band
    elif taxable_income <= 150000:
        tax = (band1_limit * band1_rate) + ((taxable_income - band1_limit) * band2_rate)
    # Income spilling into third tax band
    else:
        tax = (band1_limit * band1_rate) \
              + ((150000 - band1_limit) * band2_rate) \
              + ((taxable_income - 150000) * band3_rate)
    
    return tax

#testing getIncomeTax() and plotting the results

# Test with a single salary value
salary_example = 50000
income_tax = getIncomeTax(salary_example)
print(f"The income tax for a salary of £{salary_example} is £{income_tax:.2f}")

# Optional: Plotting tax vs. salary to visualize how tax changes with income
salaries = list(range(0, 200001, 5000))  # Salaries from £0 to £200,000 in steps of £5000
taxes = [getIncomeTax(s) for s in salaries]

plt.figure(figsize=(10, 6))
plt.plot(salaries, taxes, marker='o', linestyle='-', color='b')
plt.title("Income Tax vs. Salary (Illustrated with math and matplotlib)\nUsing math.pi for a fun fact: {:.2f}".format(math.pi))
plt.xlabel("Salary (£)")
plt.ylabel("Tax (£)")
plt.grid(True)
plt.show()
