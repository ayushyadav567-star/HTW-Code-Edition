"""A simple calculator for two numbers."""

first = float(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ").strip()
second = float(input("Enter the second number: "))

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/" and second != 0:
    result = first / second
else:
    print("Invalid operator or division by zero.")
    raise SystemExit

print("Result:", result)
