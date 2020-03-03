def jumlahHurufVokal(x):
    a = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    b = len(x)
    e = 0
    for i in x:
        if i in a:
            e += 1
    print("(",str(b),",",str(e),")")

jumlahHurufVokal("Surakarta")