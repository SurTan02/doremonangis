def carirarity(x,datas):
    #x disini adalah rarity yang dicari
    #datas disini adalah gadget.csv

    for i in range(len(datas)):
        if datas[i][4]== x:
            print("Hasil Pencarian:\n")
            print("Nama             :", datas[i][1])
            print("Deskripsi        :", datas[i][2])
            print("Jumlah           :", datas[i][3])
            print("Rarity           :", datas[i][4])
            print("Tahun ditemukan  :", datas[i][5])


        print(end="")

def caritahun(x,y,datas):
    # x disini adalah tahun yang dicari
    #y adalah kategori (= , < , > ,>=, <=
    # datas disini adalah gadget.csv

    for i in range(len(datas)):
        if y=="=":
            if datas[i][5] == x:
                print("Hasil Pencarian:\n")
                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

            print(end="")
            else:
                print("Tidak ditemukan data")
        elif y == ">":
            if datas[i][5] > x:
                print("Hasil Pencarian:\n")
                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

            print(end="")
            else:
                print("Tidak ditemukan data")
        elif y == ">=":
            if datas[i][5] >= x:
                print("Hasil Pencarian:\n")
                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

            print(end="")
            else:
                print("Tidak ditemukan data")
        elif y == "<=":
            if datas[i][5] <= x:
                print("Hasil Pencarian:\n")
                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

            print(end="")
            else:
                print("Tidak ditemukan data")
        elif y == "<":
            if datas[i][5] < x:
                print("Hasil Pencarian:\n")
                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

            print(end="")
            else:
                print("Tidak ditemukan data")