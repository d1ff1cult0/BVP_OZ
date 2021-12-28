def check_devidor(number, devidor, factors):
    if number % devidor == 0:
        factors.append(devidor)
        check_devidor(number / devidor, devidor, factors)
        return factors
    elif number == 1:
        return factors
    else:
        check_devidor(number, devidor + 1, factors)
        return factors


def find_devidors(number):
    factors = []
    devidor = 2
    if devidor < number:
        check_devidor(number, devidor, factors)
        return factors
    else:
        return factors


def main():
    number = int(input("Geef een getal"))
    print(find_devidors(number))


main()