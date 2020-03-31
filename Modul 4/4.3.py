def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)

    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return True
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

a = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
print(binSe(a, 10))