

number1 = int(input("First Number:"))
number2 = int(input("Second Number:"))
number3 = int(input("Third Number:"))

if (number1>=number2) and (number1>=number3):
    max = number1
elif (number2>=number1) and (number2>=number3):
    max = number2
else:
    max = number3
    
print("Largest Number:",max)

