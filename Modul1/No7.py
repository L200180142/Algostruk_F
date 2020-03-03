def faktorPrima(input):
    a = 1
    b = input
    d = 0
    bilanganPrima = [2, 3, 5, 7, 11]
    c = []
    while a >= 0:
        if a == input:
            break
        elif d == 4:
            c = [input]
            break
        elif b % bilanganPrima[d] == 0:
            c.append(bilanganPrima[d])
            a = a * bilanganPrima[d]
            b = b / bilanganPrima[d]
        else :
            d += 1

    print(c)

faktorPrima(15)