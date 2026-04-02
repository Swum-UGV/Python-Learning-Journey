month_days={'dec':31,'feb':28 or 29,'sep':30}
month=input('enter month:').lower()
if month in month_days:
    print(f'{month.capitalize()} has {month_days[month]} days')
else:
    print('something worng!')