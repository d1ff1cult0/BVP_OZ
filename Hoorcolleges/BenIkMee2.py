from datetime import date

todays_date = date.today()

age = int(input('Give your age: '))
if 0 <= age <= 134:
    if age >= 18:
        print('You are an adult!')
    else: print('You are a minor!')
    birthyear = todays_date.year - age
    print(f'You were born in {birthyear}')
else: print('You have given an invalid age')

