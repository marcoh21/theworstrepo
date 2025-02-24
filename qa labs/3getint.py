min = 10
max = 100
while True:
    value = int(input(f"what is yer value between {min} and {max}"))

    if min <= value <= max:
        print (f"valid integer entered: {value}")
        break
    elif type(value) != int:
        print ("dude, this aint an integer")
    else:
        print("not in the range probs")
