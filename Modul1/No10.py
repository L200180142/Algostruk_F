def selesaikanABC(a, b, c):
    D = b - (4*a*c)
    if D < 0 :
        print("Determinan negatif. Persamaan tidak mempunyai akar")
    else:
        print("Determinan positif. Persamaan mempunyai nilai akar")

selesaikanABC(1,2,3)
