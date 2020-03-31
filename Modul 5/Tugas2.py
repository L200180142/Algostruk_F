A = [2,34,56,78,89,190]
B = [1,4,12,23,36,76,120]

def sortToC(a, b):
    c = a+b
    for i in range(1, len(c)):
        nilai = c[i]
        pos = i
        while pos > 0 and nilai < c[pos - 1]:
            c[pos] = c[pos-1]
            pos -=1
        c[pos] = nilai
    return c
