# Conditional Statement Example

def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Example usage
number = int(input("Enter a number: "))
result = check_number(number)
print(result)


#use and or operators in conditional statements

if number > 0 and number < 100:
    print("The number is positive and less than 100.")
elif number > 100 or number < -100:
    print("The number is either greater than 100 or less than -100.")
else:
    print("The number is either negative or zero, or it is between 0 and 100.")



# nested conditional statements
def nested_check(num):
    if num >= 0:
        if num == 0:
            return "The number is zero."
        else:
            return "The number is positive."
    else:
        return "The number is negative."
