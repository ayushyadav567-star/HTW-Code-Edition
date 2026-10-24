"""Print a countdown from a positive integer to zero."""

start = int(input("Enter a positive starting number: "))

if start < 1:
    print("Please enter a positive integer.")
else:
    while start >=0:
        print(start)
        start -= 1

    print("Go!")
