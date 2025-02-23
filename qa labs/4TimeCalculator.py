import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",")  # Split the string by ','
grades = list(map(int, grades))  # Convert to a list of integers

# Calculate statistics
min_grade = min(grades)
max_grade = max(grades)
average_grade = round(sum(grades) / len(grades), 2)
mean_grade = round(statistics.mean(grades), 2)
median_grade = statistics.median(grades)

# Display results using string formatting
output = """
Statistics of Student Grades:
Minimum Grade: {}
Maximum Grade: {}
Average Grade: {}
Mean Grade: {}
Median Grade: {}
""".format(min_grade, max_grade, average_grade, mean_grade, median_grade)

print(output)
