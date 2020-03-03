a = 1
for i in range(100):
    if a % 3 == 0 and a % 5 == 0:
        print("Python UMS")
    elif a % 3 == 0 :
        print("Python")
    elif a % 5 == 0 :
        print("UMS")
    else:
        print(a)
    a += 1