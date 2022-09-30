
def main():
    print(format_date())

def format_date():
    valid_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:
        date = input("Input a date: ")
        try:
            split_date = date.split("/")
            year = int(split_date[2])
            day = int(split_date[1])
            month = int(split_date[0])

        except IndexError:
            split_date = date.split()
            year = int(split_date[2])
            day = int(split_date[1].replace(",",""))
            month = split_date[0].title()

            if month not in valid_months:
                print("Invalid month")
            month = valid_months.index(month)+1

        if day > 31:
            print("Invalid number of days")
        elif month > 12:
            print("Invalid number of months")
        else:
            break

    return f'{year}-{month:02}-{day:02}'

if __name__ == "__main__":
    main()