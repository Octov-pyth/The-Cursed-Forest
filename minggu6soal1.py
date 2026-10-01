mahasiswa_aktif = str(input("Apakah Anda mahasiswa aktif(ya/tidak)?  ")).lower()
reservasi = str(input("Apakah Anda memiliki reservasi(ya/tidak)?  ")).lower()

if mahasiswa_aktif == 'ya':
    if reservasi == 'ya':
        print("Diizinkan masuk")
    elif reservasi == 'tidak':
        print("Silahkan melakukan reservasi")
else:
    print("Akses ditolak")

