def pyramid(height, symbol='+'):
    i = 1
    for j in range(height-i):
        print((height-i)*' ' + (1+2*(i-1))*symbol)
        i += 1


pyramid(12, 'x')