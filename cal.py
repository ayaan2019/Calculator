print ("what do you want to do?")
print ("1. add")
print ("2. subtract")
print ("3. multiply")
print ("4. divide")

choice = input ("enter choice (1/2/3/4): ")

if choice == '1':
    num1 = float(input ("enter first number: "))
    num2 = float(input ("enter second number: "))
    print (num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    num1 = float(input ("enter first number: "))
    num2 = float(input ("enter second number: "))
    print (num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    num1 = float(input ("enter first number: "))
    num2 = float(input ("enter second number: "))
    print (num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    num1 = float(input ("enter first number: "))
    num2 = float(input ("enter second number: "))
    if num2 != 0:
        print (num1, "/", num2, "=", num1 / num2)
    else:
        print ("Error: Division by zero is not allowed.")
else:    print ("Invalid input")