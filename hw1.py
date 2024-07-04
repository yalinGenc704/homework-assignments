#####################################################################################################################
# Calculator Application                                                                                            #
# In this application, we will design an application that receives two operands and one operator from the user.     #
# The operand will be one of +, -, /, *.                                                                            #
# The operator will be a float or int type number.                                                                  #
#####################################################################################################################

# **************************** Stage 1 : User Inputs  ****************************#
# Get first number from user
# operand1 = float(input("Enter the first number (float or int): "))
operand1 = float(input("Enter the first number (float or int): "))

# Get second number from user
# Enter the necessary codes here to get the second operand from the user.
operand2 = float(input("Enter the second number (float or int): "))
# Get operand from user
# The code on line 21 is missing. Fill in this gap.
# Tips
# Input is a function.
# It takes string as parameter.
operator = input("Enter the operand: ")


# **************************** Stage 2 : Calculation  ****************************#

# Perform the calculation

# There is an error in line 29, the comparison cannot be performed. Complete the necessary additions.
if operator == "+":
    result = operand1 + operand2

# There is an error in line 34, to assign to result variable cannot be performed. Complete the necessary updates.
elif operator == "-":
    result = operand1 - operand2

# Line 37 has been completely deleted. Complete it with the appropriate keyword and action.
elif operator == "*":
    result = operand1 * operand2


elif operator == "/":
    if operand2 != 0:
        result = operand1 / operand2

# Complete lines 50 and 51 with codes that will check if the second operator 0 is entered and show the required message to the user.
# Tips 
# else keyword
# print function
# indent
    else:  
        print("Invalid operator")
        exit()


# Add a comment line to line 55 describing the transactions in lines 56 and 57.
# If the second number is equal to 0, it is an invalid operator.



# **************************** Stage 3 : Display Result  ****************************# 
# Print the result
# The code on line 65 is missing. Fill in this gap.
# Tips
# Result Variable
print("Result:",result)