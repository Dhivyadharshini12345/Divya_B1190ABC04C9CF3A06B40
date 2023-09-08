def isLeapYear(year):
    # Check if the year is divisible by 4 but not divisible by 100,
    # or if it's divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if isLeapYear(year):
    print("{} is a Leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))
