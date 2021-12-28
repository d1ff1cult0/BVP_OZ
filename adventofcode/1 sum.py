try:
    list = []
    while True:
        list.append(int(input()))
except:
    print(list)
i = 0
k = 0
for i in range(len(list)):
    for k in range(len(list)):
        if list[i] + list[k] == 2020:
            print(list[k], list[i], list[k] * list[i])
            print(k, i)
            exit()

