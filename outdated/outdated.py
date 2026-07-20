months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    # Format 1: MM/DD/YYYY
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except:
            pass

    # Format 2: Month Day, Year
    else:
        try:
            month_name, rest = date.split(" ", 1)
            day, year = rest.split(", ")
            day = int(day)
            year = int(year)

            if month_name in months and 1 <= day <= 31:
                month = months.index(month_name) + 1
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except:
            pass
