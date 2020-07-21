def date_time(time: str) -> str:
    #replace this for solution
    date, time = time.split()
    day, month, year = date.split(".")
    day, month, year = int(day), int(month), int(year)
    hour, minute = time.split(":")
    hour, minute = int(hour), int(minute)
    months = ("January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December")
    if hour == 1:
        hs = "hour"
    else:
        hs = "hours"
    if minute == 1:
        ms = "minute"
    else:
        ms = "minutes"
    time = f"{day} {months[month-1]} {year} year {hour} {hs} {minute} {ms}"
    return time

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")