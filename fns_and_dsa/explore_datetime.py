def display_current_datetime():
    from datetime import datetime
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    from datetime import datetime, timedelta
    current_date = datetime.now()
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days)
    print(f"Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
