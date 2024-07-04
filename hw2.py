#####################################################################################################################
# Updated Calculator Application                                                                                    #
# The calculator application should be able to perform multiple operations as many times as the user wants.         #
# The application should only terminate when the user enters the x character.                                       #
# Otherwise, it will continuously request new inputs from the user.                                                 #
# Note: The application should continue to run even in the case of undefined operations or invalid inputs,          #
# giving the necessary warning and asking the user for new numbers and operators.                                   #
#####################################################################################################################

while True:
# The function was forgotten on line 12
    isContinue = input("Press 'x' to finish: ")

# There are three errors in line 17: the first is a keyword error, the second is case sensitive and the other is a logical error.
# Tips
# Read the application instructions at the beginning of the file carefully.
    if isContinue == "x":
        exit()

# Lines 22-52 work if else works, there is a significant deficiency in these lines.
    else:
    # Get first number from user
        operand1 = float(input("Enter the first number (float or int): "))
    # Get second number from user
        operand2 = float(input("Enter the second number (float or int): "))

    # Get operator from user
        operator = input("Enter the operator (+, -, *, /)")



    # Perform the calculation
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 != 0:
            result = operand1 / operand2
        else:
            # Check if the second operand is 0 and show the required message to the user.
            print("Error: Division by zero is not allowed.")
            continue
    else:
        # If the operator is invalid, set the result as an error message. 
        result = "Invalid operator."

    print("Result:", result)