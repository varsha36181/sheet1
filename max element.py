#Write a program to input two numbers(A & B) from the user and print the maximum element among A & B. 

A = float(input("Enter first number (A): "))
B = float(input("Enter second number (B): "))

if A > B:
    print("Maximum:", A)
elif B > A:
    print("Maximum:", B)
else:
    print("Both are equal")

