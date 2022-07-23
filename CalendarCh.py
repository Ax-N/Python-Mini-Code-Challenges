from calendar import calendar
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def cal():
    run = True
    try:
        while(run):
            day = input("Which day of the week do you want to count?\n"
                        + "0: Monday\n"
                        + "1: Tuesday\n"
                        + "2: Wednesday\n"
                        + "3: Thursday\n"
                        + "4: Friday\n"
                        + "5: Saturday\n"
                        + "6: Sunday\n"
                        + "Or 'exit' to quit\n"
                        + "? ")
            if day == "exit":
                run = False
                break
            year = int(input("Enter the Year: "))
            month = int(input("Enter the Month: "))
            d = int(day)
            count = 0
            start, end = calendar.monthrange(year, month)
            for i in range(end):
                if start == d:
                    count += 1
                if (start - 7) == d:
                    count += 1
                elif (start - 14) == d:
                    count += 1
                elif (start - 21) == d:
                    count += 1
                elif (start - 28) == d:
                    count += 1
                start += 1
            print("There are " + str(count) + " of those days in the month and year specified")
            print("----------------\n")
    except Exception as e:
        print(e)
        print("Oops")

cal()