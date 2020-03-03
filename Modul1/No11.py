def apakahKabisat(input):
    a = input

    while a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                print(input, "adalah tahun kabisat")
                break
            print(input, "adalah bukan tahun kabisat")
            break
        print(input, "adalah tahun kabisat")
        break

    if a % 4 != 0 :
        print(input, "adalah bukan tahun kabisat")


apakahKabisat(2400)