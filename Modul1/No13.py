def katakan(input):
    x = str(input)
    hitung = len(x)
    print(hitung)
    angka = {1:"satu", 2:"dua", 3:"tiga", 4:"empat", 5:"lima", 6:"enam", 7:"tujuh", 8:"delapan", 9:"sembilan"}
    angkaRatusan = {1:"seratus", 2:"dua ratus", 3:"tiga ratus", 4:"empat ratus", 5:"lima ratus", 6:"enam ratus", 7:"tujuh ratus", 8:"delapan ratus", 9:"sembilan ratus"}
    hasil = ""
    for i in x:
        if int(i) == 0:
            if hitung == 4:
                hasil = hasil + " " + "ribu"
            hitung -= 1
            continue
        elif hitung == 7:
            hasil = hasil + str.title(angka[int(i)]) + " juta"
            hitung -= 1
        elif hitung == 6:
            hasil = hasil + " " + angkaRatusan[int(i)]
            hitung -= 1
        elif hitung == 5:
            hasil = hasil + " " + angka[int(i)] + " puluh"
            hitung -= 1
        elif hitung == 4:
            hasil = hasil + " " + angka[int(i)] + " ribu"
            hitung -= 1
        elif hitung == 3:
            hasil = hasil + " " + angkaRatusan[int(i)]
            hitung -= 1
        elif hitung == 2:
            hasil = hasil + " " + angka[int(i)] + " puluh"
            hitung -= 1
        elif hitung == 1:
            hasil = hasil + " " + angka[int(i)]

    print(hasil)


katakan(3225759)
