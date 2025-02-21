def is_palindrome(input_str: str):
    # Define a tuple of all special characters to remove
    special_chars = (" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~")

    # Create an empty string to store the cleaned version
    cleaned_str = ''

    # Iterate through each character in the input string
    for char in input_str:
        # Check if the character is not in the special characters tuple
        if char not in special_chars:
            # If it's not a special character, add it to the cleaned string (converted to lowercase)
            cleaned_str += char.lower()

    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Testing the function with the strings from the task
strings = [
    "A man, a plan, a canal, Panama!",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon.",
    "Eva, can I see bees in a cave?!@!!",
    "Madam, in Eden, I'm Adam!!%%!!!@@"
]

for s in strings:
    print(f"'{s}' -> {is_palindrome(s)}")
