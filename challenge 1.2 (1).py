if 2004 % 4 == 0:
    if 2004 % 100 == 0:
        if 2004 % 400 == 0:
            print("The year is a leap year!")
        else:
            print("The year is not a leap year!")
    else:
        print("The year is a leap year!")
else:
    print("The year is not a leap year!")
