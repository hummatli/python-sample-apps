from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print "Today is : ", today
    print "Today's components : ", today.day, today.month, today.year
    print "Today's weekday : ", today.weekday()


    today = datetime.now()
    print "Datetime today : ", today

    print "%10s %2d" % ("some string", 1)
if __name__ == "__main__":
    main()