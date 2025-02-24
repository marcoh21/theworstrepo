word = input("give a word")

counter = 0
vowel_counter = 0

while counter < len(word):
    x = word[counter]
    if x in "aeiouAEIOU":
        vowel_counter += 1
    counter += 1

print(f"number of vowels in {word} is {vowel_counter}")