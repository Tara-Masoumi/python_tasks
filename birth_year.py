def converter(day, month, year):
    if month > 10 or day > 10 and month == 10:
        birthday = year + 622

    else:
        birthday = year + 621
    print(f"your year of birthday is {birthday}")


while True:
    day = int(input(" :روز تولد را وارد کنید"))
    month = int(input(" :ماه تولد را وارد کنید"))
    year = int(input(" :سال تولد را وارد کنید"))
    converter(day, month, year)


