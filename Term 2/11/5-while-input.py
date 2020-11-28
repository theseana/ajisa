number = input("Enter Number: ")
counter = 0

while number != '0':
    print(number)
    number = input("Enter Number: ")
    counter += 1
print(f"You entered {counter} numbers.")