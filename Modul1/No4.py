def rerata(input):
    x = len(input)
    hasil = 0
    for i in input:
        hasil += i 
    print(hasil/x)

rerata([1, 2, 3, 4, 5])