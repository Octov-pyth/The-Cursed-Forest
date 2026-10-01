print("===Diskon Toko Alat Tulis===")

anggota = str(input("Apakah Anda memiliki kartu anggota(ya/tidak)?   ")).lower()
total_belanja = int(input("Berapa total belanja Anda? Rp"))

if anggota == 'ya':
    if total_belanja >= 200000:
        diskon = total_belanja * 0.15
        total_pembayaran = total_belanja - diskon
        print("Anda mendapat diskon 15%")
        print(f"Anda menghemat Rp{diskon}")
        print(f"Total pembayaran Anda adalah Rp{total_pembayaran}")
    elif total_belanja < 200000:
        diskon = total_belanja * 0.1
        total_pembayaran = total_belanja - diskon
        print("Anda mendapat diskon 10%")
        print(f"Anda menghemat Rp{diskon}")
        print(f"Total pembayaran Anda adalah Rp{total_pembayaran}")

elif anggota == 'tidak':
    if total_belanja >= 200000:
        diskon = total_belanja * 0.15
        total_pembayaran = total_belanja - diskon
        print("Anda mendapat diskon 15%")
        print(f"Anda menghemat Rp{diskon}")
        print(f"Total pembayaran Anda adalah Rp{total_pembayaran}")
    elif total_belanja < 200000:
        print("Anda tidak mendapatkan diskon")
        print(f"Total pembayaran Anda adalah Rp{total_belanja}")
