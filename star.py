print("***********")
print("1. Kiri")
print("2. Kanan")
print("3. Hitung luas segitiga")
print("***********")
pilihan = int(input("Masukkan pilihan : "))
ulang = 0
ulang2 = 0
if pilihan == 1 :
    bintang = int(input("Masukkan jumlah bintang : "))
    space = 2 * bintang - 2
    bintang_for = bintang
    space_for = space

    for ulang in range(0, bintang_for-1):
        for ulang2 in range(0, space_for):
            print(' ', end='')
        space_for = space_for - 2
        for ulang2 in range(0, ulang + 1):
            print(' *', end='')
        print('')
    space_for = 0
    for ulang in range(bintang_for):
        for ulang2 in range(space_for):
            print(' ', end='')
        space_for =space_for + 2
        for ulang2 in range(0, bintang_for):
            print(' *', end='')
        bintang_for = bintang_for - 1
        print('')

    ulang = 0
    while ulang<bintang-1:
        while ulang2<space:
            print(' ', end='')
            ulang2+=1
        space-=1
        ulang2 = 0
        while ulang2<ulang+1:
            print(' *', end='')
            ulang2+=1
        print('')
        ulang+=1
    space = 0
    ulang = 0
    bintang1 = bintang
    while ulang < bintang1:
        while ulang2<space:
            print(' ', end='')
            ulang2+=1
        space+=2
        ulang2 = 0
        while ulang2<bintang:
            print(' *', end='')
            ulang2+=1
        ulang2=0
        bintang-=1
        print('')
        ulang+=1

elif pilihan == 2 :
    bintang = int(input("Masukkan jumlah bintang : "))
    space = " "
    jumlah = 1
    for ulang in range(bintang) :
        space = space + " *"
        print(space)
        jumlah = jumlah + 1
    for ulang in range(jumlah) :
        space = space + " *"
        jumlah = jumlah - 1
        print(space[:(jumlah * 2)])

    space = " "
    jumlah = 1
    while bintang > 0 :
        space = space + " *"
        print(space)
        jumlah = jumlah + 1
        bintang = bintang - 1
    while jumlah > 1 :
        space = space + " *"
        jumlah = jumlah - 1
        print(space[:(jumlah * 2)])
elif pilihan == 3:
    alas = int(input("Masukkan nilai alas : "))
    tinggi = int(input("Masukkan nilai tinggi : "))
    luas = float(alas*tinggi)/2
    print("Luas : ",luas)