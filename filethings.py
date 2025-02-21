# Ask for forgiveness approach
# May not exist!

try:
    my_file = open("myfile.txt", "r")
    print(my_file.read())
except FileNotFoundError as e:
    print(f"Your file hasn't been found!: {e}")
except FileExistsError as e:
    print(f"Your file already exists: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    my_file.close()

# Look before you leap approaches
# Will exist!
if os.path.exists("myfile.txt"):
    with open("myfile.txt", "r") as my_file:
        print(my_file.read())
else:
    print("File does not exist!")