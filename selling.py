def most_carpet(money, carpets, number_of_carpets):
    store = [[0 for w in range(money + 1)]
             for i in range(number_of_carpets + 1)]

    for i in range(number_of_carpets + 1):
        for m in range(money + 1):
            if i == 0 or m == 0:
                store[i][m] = 0
            elif carpets[i - 1] <= m:
                store[i][m] = max(1 + store[i - 1][m - carpets[i - 1]], store[i - 1][m])
            else:
                store[i][m] = store[i - 1][m]

    res = store[number_of_carpets][money]
    print(res)

    m = money
    for i in range(number_of_carpets, 0, -1):
        if res <= 0:
            break
        if res == store[i - 1][m]:
            continue
        else:
            print("carpet " + str(i) + ": " + str(carpets[i - 1]))

            res = res - 1
            m = m - carpets[i - 1]


if __name__ == '__main__':
    carpets = [600, 300, 300, 500, 600, 400, 250, 150, 450]
    customer_money = int(input())
    n = len(carpets)

    most_carpet(customer_money, carpets, n)
