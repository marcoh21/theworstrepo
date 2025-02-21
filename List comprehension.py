# Task: List Comprehension Practice
# You are given a list of numbers. Your goal is to complete the following tasks using list comprehensions:
#
# Create a new list containing only the even numbers from the original list.
# Create a new list containing the squares of the even numbers from the original list.
# Create a new list containing only the numbers that are divisible by 3 but not by 5 from the original list.
# Create a new list containing the words in a sentence that are longer than 4 characters (ignoring case).
# Create a new list containing the first letter of each word in a sentence (ignore punctuation).
# Expression for value in iterable if condition 


numbers = list(range(1, 16))

even_numbers = [num for num in numbers if num % 2 == 0]
print (f"your even numbers are {even_numbers}")

evens_squared = [num ** 2 for num in numbers if num % 2 == 0]
print(f"squared even numbers are:")





