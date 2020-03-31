def cariTerkecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan[0]

    for i in range(1,n):
        if kumpulan[i] < terkecil:
            terkecil = kumpulan[i]
    return terkecil

Daftar = [12,60,13,4,7,19]
print(cariTerkecil(Daftar))