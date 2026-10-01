print("===Seleksi Peserta Lomba Pemrograman")

berkas = str(input("Apakah berkas Anda lengkap(ya/tidak)?  ")).lower()
nilai = int(input("Berapa nilai tes Anda(0-100)?  "))
pengalaman = str(input("Apakah Anda memiliki pengalaman mengikuti lomba(ya/tidak)?  ")).lower()

if berkas == 'ya':
    if nilai >= 85:
        if pengalaman == 'ya':
            print("Lolos tim utama")
        elif pengalaman == 'tidak':
            print("Lolos tim pembinaan")
    elif nilai >= 70:
        if pengalaman == 'ya':
            print("Lolos tim pembinaan")
        elif pengalaman == 'tidak':
            print("Masuk daftar cadangan")
    elif nilai < 70 :
        print("Tidak lolos seleksi")
elif berkas == 'tidak':
    print("Tidak lolos seleksi")