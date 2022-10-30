try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1 When will a ValueError occur?
# when numerator and denominator is not valid.

# 2 When will a ZeroDivisionError occur?
# when denominator is zero

# 3 Could you change the code to avoid the possibility of a ZeroDivisionError?
# no
