def formatRupiah(input):
    x = str(input)
    y = 0
    textbalik = x[::-1]
    hasil = ""
    for i in textbalik:
        if y % 3 == 0 and y != 0:
            hasil = hasil + "." + i
            y += 1
        else:
            hasil = hasil + i
            y += 1
    print("Rp. "+hasil[::-1])


formatRupiah(2560000)
