word = input("enter a word: ")
vowels = "aeiou"
count = 0

for letter in word:
    if letter.lower() in vowels:
        count += 1

print(count)