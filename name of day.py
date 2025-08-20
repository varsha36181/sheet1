# WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc. 

num = int(input("Enter a number (1-7): "))

match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")

