amount_of_seconds = int(input('Give the amount of seconds:'))

days = amount_of_seconds//(60*60*24)
days_remainder = amount_of_seconds%(60*60*24)
hours = days_remainder//(60*60)
hours_remainder = days_remainder%(60*60)
minutes = hours_remainder//(60)
minutes_remainder = hours_remainder%(60)
seconds = minutes_remainder

print(f'{amount_of_seconds} seconds can be converted into {days} days, {hours} hours, {minutes} minutes and {seconds} seconds')


