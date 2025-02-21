import re

def palindrome_check(input_string):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(re.findall(r'[a-zA-Z0-9]', input_string)).lower()
    
    # Check if the string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Test cases
test_strings = [
    "A man, a plan, a canal, Panama!",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon.",
    "Eva, can I see bees in a cave?!@!!",
    "Madam, in Eden, I'm Adam!!%%!!!@@"
]

# Apply the function to each string
for test in test_strings:
    print(f"'{test}': {palindrome_check(test)}")



