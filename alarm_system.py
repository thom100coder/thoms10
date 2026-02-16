# Alarm program
try:
    bell = int(input("Enter the alarm level (1-20): "))

    if 17 <= bell <= 20:
        print("High fire risk")
    elif 12 <= bell <= 16:
        print("Medium fire risk")
    elif 1 <= bell <= 11:
        print("Low fire risk")
    else:
        print("Value out of accepted range")

except ValueError:
    print("Please enter an integer number between 1 and 20")
