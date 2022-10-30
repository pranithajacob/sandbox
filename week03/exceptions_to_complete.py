is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
    except:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)


finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a valid integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
