def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
cariLurus(A,31) # Hasil True
cariLurus(A,8) # Hasil False

