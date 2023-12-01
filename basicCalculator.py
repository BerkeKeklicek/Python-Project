def add(number1,number2):
    return number1 + number2

def subtract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1 * number2

def divide(number1,number2):
    return number1 / number2
    
    
print("Options:")
print("1 : Addition")
print("2 : Subtraction")
print("3 : Multiplication")
print("4 : Division")

choice = input("Your choice?")

number1 = int(input("First number?"))
number2 = int(input("Second number?"))

if choice == "1":
    print("Result : " +str(add(number1,number2)))    
elif choice == "2":
    print("Result : " +str(subtract(number1,number2)))
elif choice == "3":
    print("Result : " +str(multiply(number1,number2)))
elif choice == "4":
    print("Result : " +str(divide(number1,number2)))        
else:
    print("Invalid Number!")

    
    
    
    
