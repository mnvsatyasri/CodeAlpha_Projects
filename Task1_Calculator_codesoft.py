while True:
    try:
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        break
    except ValueError:
        print("Invalid input! Please enter numbers only.")
while True:
    operator = input("Enter an operator (+,-,*,/):")
    if operator in {'+' , '-' , '*' , '/'}:
        break
    else:
        print(f"{operator} is an invalid input,Please enter operator")
if operator == '+':
    output = num1 + num2
    print(round(output,3))
elif operator == '-':
    output = num1 - num2
    print(round(output,3))
elif operator == '*':
    output = num1 * num2
    print(round(output,3))
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        output = num1 / num2
        print(round(output,3))

