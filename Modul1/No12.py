import random

a = random.randrange(0, 100)
c = 1
b = int(input("Masukkan tebakan ke-"+str(c)+":> "))

while a > 0:
    if b == a:
        print("Ya. Anda benar")
        break
    else:
        if a > b :
            print("Itu terlalu kecil. Coba lagi.")
            c += 1
            b = int(input("Masukkan tebakan ke-" + str(c) + ":> "))
        else:
            print("Itu terlalu besar. Coba lagi.")
            c += 1
            b = int(input("Masukkan tebakan ke-" + str(c) + ":> "))
