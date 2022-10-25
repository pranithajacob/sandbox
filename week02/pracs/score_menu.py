
age = int(input("Age: "))
while age < 0:
    print("Invalid age!")
    age = int(input("Age: "))
    print("You are {} years old".format(age))

is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)

