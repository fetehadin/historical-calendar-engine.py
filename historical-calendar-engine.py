# get the year from the User
while True:
    year = int(input("Enter the Gregorian year: "))
    if year < 8:
        print("Ethiopian calendar not defined before 8 AD.")
        choice = input("\nDo you want to generate another calendar? (y/n): ")
        if choice.lower() != 'y':
            print("Thanks for visiting!")
            break
        continue

    # #Determine calendar mode
    # if year < 1752:
    #     year_mode = "julian"
    # elif year == 1752:
    #     year_mode = "hybrid"
    # else:
    #     year_mode = "gregorian"

    week_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    mon = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    ethiopian_months = [
        "Meskerem", "Tikimt", "Hidar", "Tahsas", "Tir", "Yekatit",
        "Megabit", "Miyazya", "Ginbot", "Sene", "Hamle", "Nehase", "Pagume"
    ]

    months = list(mon.keys())

    def check_leap(y, m=None, d=None):
        if y < 1752 or (y == 1752 and (m is None or (m < 9 or (m == 9 and d <= 2)))): return y % 4 == 0
        else: return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

    def date_to_jdn(y, m, d):
        # Handle transition year 
        if y < 1752 or (y==1752 and (m<9 or (m==9 and d <= 2))):
            if m <= 2:
                y -= 1
                m += 12
            return (365 * y + y // 4 + (153 * (m - 3) + 2) // 5 + d + 1721117)
        else:  # Gregorian formula
            if m <= 2:
                y -= 1
                m += 12
            return (365 * y + y // 4 - y // 100 + y // 400 +
                    (153 * (m - 3) + 2) // 5 + d + 1721119)


    def jdn_to_ethiopia(jdn):
        ethiopian_epoch_jdn = 1723856
        n = jdn - ethiopian_epoch_jdn
        r = n % 1461
        if r >= 1460:
            day_of_year = 366
        else:
            day_of_year = (r % 365) + 1

        if day_of_year <= 360:
            month_ec = (day_of_year - 1) // 30 + 1
            day_ec = (day_of_year - 1) % 30 + 1
        else:
            month_ec = 13
            day_ec = day_of_year - 360

        return month_ec, day_ec
    

    def ec_months_for_gc_month(y, m, length):
        ec_set = []
        for d in range(1, length + 1):
            if year == 1752 and m == 9 and 3 <= d <= 13:
                continue
            jdn = date_to_jdn(y, m, d)
            ec_m, _ = jdn_to_ethiopia(jdn)
            if ec_m not in ec_set:
                ec_set.append(ec_m)
        return [ethiopian_months[m - 1] for m in ec_set]

    def weekday_from_jdn(jdn):
        return (jdn + 1) % 7  # 0 = Sunday

    def display(y, m, length):
        print("|  Sun  |  Mon  |  Tue  |  Wed  |  Thu  |  Fri  |  Sat  |")
        print("| ----- | ----- | ----- | ----- | ----- | ----- | ----- |")

        # handle September 1752 missing days
        days = []
        d = 1
        while d <= length:
            if year == 1752 and m == 9 and 3<=d<=13:
                d = 14
                continue   # skip 3–13
            days.append(d)
            d += 1
        if y==1752 and m==9:
            start_weekday = 2
        else:
            start_jdn = date_to_jdn(y, m, days[0])
            start_weekday = (start_jdn + 1)% 7

        count = 0
        for _ in range(start_weekday):
            print("|       ", end="")
            count += 1

        for d in days:
            jdn = date_to_jdn(y, m, d)
            ec_m, ec_d = jdn_to_ethiopia(jdn)
            print(f"| {ec_d:02d} {d:02d} ", end="")
            count += 1    

            if count == 7:
                print("|")
                print("| ----- | ----- | ----- | ----- | ----- | ----- | ----- |")
                count = 0

        if count != 0:
            while count < 7:
                print("|       ", end="")
                count += 1
            print("|")
            print("| ----- | ----- | ----- | ----- | ----- | ----- | ----- |")


    ec_year_start = year - 8
    ec_year_end = year - 7

    print(f"\nGregorian Year: {year}      Ethiopian Years: {ec_year_start} - {ec_year_end}")

 
    for index, gc_month_name in enumerate(months, start=1):
        month_length = mon[gc_month_name]

        if gc_month_name == "February" and check_leap(year, 2,1):
            month_length = 29

        # month_mode = year_mode
        if year == 1752 and index >= 9:
            month_mode = "gregorian"

        ec_names = ec_months_for_gc_month(year, index, month_length)

        print(f"\n{gc_month_name}     {' - '.join(ec_names)}")
        display(year, index, month_length)

    choice = input("\nDo you want to generate another calendar? (y/n): ")
    if choice.lower() != 'y':
        print("Thanks for visiting!")
        break

