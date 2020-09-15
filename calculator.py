'''
Collaborators: 

'''
def add_nums(a, b):
    return a + b

def sub_nums(a, b):
    return a - b

def multi_nums(a, b):
    return a * b

def divide_nums(a, b):
    return a / b
    

a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))

final = int(input("Press 1 to add, 2 to subtract, 3 to multiply, and 4 to divide. "))

if final == 1:
    print(add_nums(a, b))
elif final == 2:
    print(sub_nums(a, b))
elif final == 3:
    print(multi_nums(a, b))
elif final == 4:
    print(divide_nums(a, b))

else:
    print("You did not input 1, 2, 3, or 4.")
