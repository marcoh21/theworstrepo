# Step 1: Record the length of the list
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,
9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,
63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

length_of_ages = len(ages)
print("Length of ages list:", length_of_ages)

# Step 2: Display each age on a new line
for age in ages:
    print(age)

# Step 3: Add one year to each age
ages = [age + 1 for age in ages]
print("Ages after adding one year:", ages)

# Step 4: Remove ages outside the range 16-65
ages = [age for age in ages if 16 <= age <= 65]
print("Filtered ages (16-65):", ages)

# Step 5: Count 16-25 year olds
count_16_25 = sum(1 for age in ages if 16 <= age <= 25)
print("Count of 16-25 year olds:", count_16_25)

# Step 6: Sort the ages list
ages.sort()
print("Sorted ages:", ages)

# Step 7: Calculate and display the proportion of ages that are 16-25
proportion_16_25 = count_16_25 / len(ages)
print("Proportion of ages between 16-25:", proportion_16_25)
