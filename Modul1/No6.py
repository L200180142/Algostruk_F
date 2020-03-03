def cetakPrima(input):
    bilanganPrima = []
    bukanbilPrima = []
    for i in range(input):
        a = 2
        if i == 2 or i == 3:
            bilanganPrima.append(i)
        else :
            for x in range(i):
                if i == a:
                    bilanganPrima.append(i)
                    break
                elif i % a == 0:
                    bukanbilPrima.append(i)
                    break
                else:
                    a += 1

    print('bilangan prima :', bilanganPrima)
    print('bukan bilangan prima : ', bukanbilPrima)

cetakPrima(1000)
        