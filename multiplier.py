'''
Adapt the code from one of the functions above to create a new function called 'multiplier'.
The user should be able to input two numbers that are stored in variables.
The function should multiply the two variables together and return the result to a variable in the main program.
The main program should output the variable containing the result returned from the function.
'''
def multi():
    x = int(input("Please enter a number: "))
    y = int(input("Please enter another number: "))
    return x * y

output_num = multi()

print(output_num)