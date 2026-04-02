from math import floor
days=['sunday','mon','tue','wed','thurs','fri','sat']
year=int(input('enter the year:'))
day_of_the_week =(year+floor((year-1)/4)-floor((year-1)/100)+floor((year-1)/400))%7
print(f'jan 1 {year} is {days[day_of_the_week]}')