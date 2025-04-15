# Use Python to calculate the number of seconds in a year.
DAYS_IN_YEAR=365
HOURS_IN_DAY=24
MINUTES_IN_HOUR=60
SECONDS_IN_MINUTES=60

def main():
    print(f"There are {DAYS_IN_YEAR*HOURS_IN_DAY*MINUTES_IN_HOUR*SECONDS_IN_MINUTES} Seconds in a year.")

if __name__=='__main__':
    main()