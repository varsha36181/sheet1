# print all factors/divisor of a given +ve number
# Read N,print No.of digits in N
n= int(input("enter a number\n"))


print(f"Factors of {n} are:")
i = 1
while (i <= n):
    if (n % i == 0):
        print(i)
    i += 1

print("\n")  