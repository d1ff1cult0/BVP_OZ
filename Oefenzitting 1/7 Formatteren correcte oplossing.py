number = int(input('Give a number'))
format_number = f'{number:,}'
seperated_number = format_number.replace(',', ' ')
print(seperated_number)