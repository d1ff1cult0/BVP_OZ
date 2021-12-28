number = int(input('The number you want to reformat:'))

if 999999 >= number >= 1000:
    last_3_digits = str(number)[-3:]
    if len(str(number)) == 4:
        first_digit = slice(0, 1)
        number = str(number)
        print(number[first_digit], last_3_digits)
    if len(str(number)) == 5:
        first_digits2 = slice(0, 2)
        number = str(number)
        print(number[first_digits2], last_3_digits)
    if len(str(number)) == 6:
        first_digits3 = slice(0, 3)
        number = str(number)
        print(number[first_digits3], last_3_digits)
