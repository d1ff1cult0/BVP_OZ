try:
    list = []
    while True:
        list.append(int(input()))
except:
    print(list)
i = 0
k = 0
n = 0
for i in range(len(list)):
    for k in range(len(list)):
        for n in range(len(list)):
            if list[i] + list[k] + list[n] == 2020:
                print(list[k], list[i], list[n], list[k] * list[i]*list[n])
                print(k, i, n)
                exit()

