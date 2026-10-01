#input semua nilai yang akan digunakan di dalam proses
import time
daya_tahan_pedang = 5
kekuatan_pendekar = 1000
kekuatan_monster1 = 200
kekuatan_monster2 = 2000
kekuatan_monster3 = 1200
kekuatan_monster4 = 100
kekuatan_monster5 = 1000
kekuatan_monster6 = 4000
kekuatan_monster7 = 500

print('==Selamat datang di permainan simpel dari Python menggunakan IF, ELIF, dan ELSE==')
time.sleep(3)
print('\t')
print('Kamu terjebak di sebuah hutan terkutuk bernama The Cursed Forest....')
time.sleep(4)
print('Kamu adalah seorang pendekar pedang, tapi sisa penggunaan pedang kamu hanya sisa 5 kali')
time.sleep(5)
print('\t')
print('Buatlah pilihan agar keluar selamat dari The Cursed Forest')
time.sleep(2)
print('\t')

nama = str(input('Nama kamu : '))
time.sleep(0.8)
print('Nama kamu adalah', nama, 'Dengan power 1000')
time.sleep(1)
print('\t')
time.sleep(1)

#PERCABANGAN JALAN PERTAMA
print('Di depan kamu ada 3 jalan: kanan, kiri, dan lurus. Manakah jalan yang ingin kamu ambil dahulu?')
time.sleep(2)
print('\n')

jalan = str(input('Pilih: ')).lower()
time.sleep(1.5)

if jalan in ['Kanan', 'kanan']:
    print(
        f"\n [Jalan Kanan] {nama} bertemu monster 2 (kekuatan: {kekuatan_monster2})!"
    )
    time.sleep(2)
    print('Kekuatan kamu :', kekuatan_pendekar)
    time.sleep(1)
    if kekuatan_monster2 > kekuatan_pendekar:
        print('Kamu tidak bisa kabur dan harus melawan monster!')
        time.sleep(1)
        daya_tahan_pedang -= 1
        print('Kamu menebas monster tersebut dan kamu menang!')
        time.sleep(1)
        print(f'\tTapi sisa penggunaan pedang kamu adalah {daya_tahan_pedang}')
        time.sleep(2)
    else:
        tindakan = input('Monster lebih lemah: Mau (Kabur) atau (Tebas)?').lower()
        if tindakan == 'tebas':
            print('Kamu memilih untuk menebas monster')
            time.sleep(1)
            daya_tahan_pedang -= 1
            print('Kamu berhasil mengalahkan monster!')
            time.sleep(2)
        else: 
            print('Kamu tidak melawan monster dan kamu berhasil kabur')
elif jalan == 'kiri':
    print(
        f"\n [Jalan Kanan] {nama} bertemu monster 1 (Kekuatan: {kekuatan_monster1})"
    )
    print('Kekuatan kamu:', kekuatan_pendekar)
    if kekuatan_monster1 > kekuatan_pendekar:
        print('Kamu tidak bisa kabur dan harus melawan monster!')
        time.sleep(1)
        daya_tahan_pedang -= 1
        print('Kamu menebas monster tersebut dan kamu menang!')
        time.sleep(1)
        print(f'\tTapi sisa penggunaan pedang kamu adalah {daya_tahan_pedang}')
        time.sleep(2)
    else:
        tindakan = input('Monster lebih lemah: Mau (Kabur) atau (Tebas)?').lower()
        if tindakan == 'tebas':
            print('Kamu memilih untuk menebas monster')
            time.sleep(1)
            daya_tahan_pedang -=1
            print('Kamu berhasil mengalahkan monster!')
            time.sleep(2)
        else:
            print('Kamu tidak melawan monster dan berhasil kabur')
            time.sleep(2)
elif jalan == 'lurus':
    print(
        f"\n [Jalan Lurus] {nama} tidak menemukan apa-apa dan dapat melanjutkan perjalanan"
    )
    time.sleep(3)
else:
    print(f"\n{nama} baru mulai saja sudah linglung, akhirnya dia diserang kawanan harimau deh.")
    daya_tahan_pedang -= 5

#============================================================
#PENGECEKAN STATUS SEBELUM LANJUT KE PERCABANGAN SELANJUTNYA
#============================================================
if daya_tahan_pedang <= 0:
    print('=========================================')
    print('GAME OVER! Pedangmu patah di jalan')
    print(f"{nama} tersesat selamanya di hutan")
    print('=========================================')
else:
    #Masuk ke percabangan kedua
    print('\n--------------------------------')
    print(
        f'Selamat {nama} berhasil melewati percabangan jalan pertama. Sisa pedang:{daya_tahan_pedang}'
    )
    print('--------------------------------')
    time.sleep(2)
    print(
        '\nKamu sekarang berada di Rawa Beracun'
    )
    time.sleep(1)
    print('1. Lewati jembatan gantung (kanan)')
    print('2. Menyusuri pinggiran (kiri)')
    time.sleep(1)

    jalan2 = str(input('Pilih: ')).lower()
    time.sleep(1.5)

    if jalan2 in ['Kanan', 'kanan']:
        print(
            f"\n [Jalan Kanan] {nama} bertemu monster 4 (kekuatan: {kekuatan_monster4})"
        )
        print('Kekuatan kamu:', kekuatan_pendekar)
        if kekuatan_monster4 > kekuatan_pendekar:
            print('Monster lebih kuat, kamu harus melawannya!')
            time.sleep(1)
            daya_tahan_pedang -= 1
            print('Kamu menebas monster tersebut dan kamu menang!')
            time.sleep(1)
            print(f"\t Tapi sisa penggunaan pedang kamu adalah {daya_tahan_pedang}")
            time.sleep(1)
        else:
            tindakan = input('Monster lebih lemah: Mau (Kabur) atau (Tebas)?').lower()
            if tindakan == 'tebas':
                print('Kamu memilih untuk menebas monster')
                time.sleep(1)
                daya_tahan_pedang -=1
                print('Kamu berhasil mengalahkan monster!')
                time.sleep(1)
                print(f"\t Tapi sisa penggunaan pedang kamu adalah {daya_tahan_pedang}")
                time.sleep(2)
            else: 
                print('\nKamu tidak melawan monster dan kamu berhasil kabur')
                time.sleep(2)
    elif jalan2 in ['Kiri','kiri']:
        print(
            f"\n [Jalan Kiri] {nama} bertemu 2 monster kuat (Kekuatan: {kekuatan_monster3} dan {kekuatan_monster5})"
        )
        time.sleep(2)
        print("Kekuatan kamu:", kekuatan_pendekar)
        time.sleep(1)
        print("Kamu ingin melawan keduanya atau melawan salah satu?")
        time.sleep(1)
        print("Jika melawan salah satunya saja, kamu akan kehilangan 3 pedang untuk menghindari monster yang sama kuatnya denganmu")
        time.sleep(3)
        print("Penggunaan Pedang: ", daya_tahan_pedang)
        time.sleep(1)

        serang = str(input('Serang Dua atau Serang Satu? ')).lower()
        time.sleep(2)

        if serang == 'dua':
            print(
                'Kamu berhasil menebas kedua monster!'
            )
            time.sleep(1)
            daya_tahan_pedang -= 2
            print(f"\nTapi sisa penggunaan pedang kamu adalah {daya_tahan_pedang}")
            time.sleep(3)

        elif serang == 'satu':
            print("Kamu berhasil menebas monster yang lebih kuat!")
            time.sleep(1)
            daya_tahan_pedang -= 3
            print(f"\nTapi sisa penggunaan pedang kamu adalah {daya_tahan_pedang}")
            time.sleep(3)
        else:
            print(f"{nama} tidak memilih salah satu atau keduanya, jadinya dia mati karena diserang kedua monster")
            daya_tahan_pedang -=5
            time.sleep(1.5)
#============================================================
#PENGECEKAN STATUS SEBELUM LANJUT KE PERCABANGAN TERAKHIR
#============================================================
if daya_tahan_pedang <= 0:
    print('=========================================')
    print('GAME OVER! Pedangmu patah di jalan')
    print(f"{nama} tersesat selamanya di hutan")
    print('=========================================')
else:
    #Masuk ke percabangan terakhir
    print('\n--------------------------------')
    print(
        f'Selamat {nama} berhasil melewati percabangan jalan kedua. Sisa penggunaan pedang:{daya_tahan_pedang}'
    )
    print('--------------------------------')
    time.sleep(3)
    print(
        '\nKamu sekarang berada di Last Gate'
    )
    time.sleep(2)
    print("Di depan mu ada dua pintu besar, masing-masing pintu memiliki warna yang berbeda dengan sebuah tulisan tertera di permukaan pintu")
    time.sleep(4)
    print(f"\n[Pintu Merah] bertuliskan (Kamu akan keluar dari hutan ini)")
    time.sleep(1.5)
    print(f"[Pintu Biru] bertuliskan (Kamu akan tersesat selamanya di hutan ini)")
    time.sleep(2)

    pilihan_akhir = str(input(f"\nPintu manakah yang akan kamu pilih?  ")).lower()
    time.sleep(1.5)

    if pilihan_akhir in ['merah','Merah']:
        print(f'\nKamu telah memilih [Pintu Merah]...')
        time.sleep(2)
        print(f"{nama} telah memasuki ruangan BOSS...")
        time.sleep(2)
        print("Monster di dalam ruangan ini bertanya kepadamu...")
        time.sleep(1)
        print("Boss Red: Jika kamu bertahan di sini selama satu jam, maka kamu akan berhasil pergi dari hutan terkutuk ini.")
        time.sleep(3)
        print("Boss Red: Jika kamu berhasil pergi dari hutan terkutuk ini, maka kamu akan mati.")
        time.sleep(2)
        print(f"\nA: Kamu akan berhasil pergi dari hutan terkutuk ini")
        print(f"\nB: Kamu akan mati")
        
        jawab = str(input(f"\nApa yang dimaksud Boss Red?  ")).lower()
        time.sleep(3)
        if jawab in ['A','a']:
            print(f"\nBoss Red: Ohoho kamu percaya diri sekali pendekar...")
            time.sleep(3)
            print("Boss Red: lain kali berpikirlah sebelum menjawab...")
            daya_tahan_pedang -= 5
        elif jawab in ['B','b']:
            print(f"\nBoss Red: Sangat bijak, itulah esensi seorang pendekar....")
            time.sleep(2)
        else:
            print(f"\nBoss Red: Seorang pendekar haruslah berpikiran tegas...")
            time.sleep(2)
            print(f"\nBoss Red: Kau tidak pantas untuk menjadi pendekar.")
            time.sleep(2)
            daya_tahan_pedang -= 5
    elif pilihan_akhir in ['biru','Biru']:
        print(f'\nKamu telah memilih [Pintu Merah]...')
        time.sleep(2)
        print(f"\n{nama} telah memasuki ruangan BOSS...")
        time.sleep(2)
        print(f"\nMonster di dalam ruangan ini bertanya kepadamu...")
        time.sleep(1)
        print(f"\nBoss Blue: Pendekar? Huh! Pendekar hanyalah sebutan untuk orang yang bodoh!")
        time.sleep(1)
        print(f"\nBoss Blue: Tidak ada satupun orang yang disebut pendekar bisa menjawab satu pertanyaan dariku...")
        time.sleep(0.5)
        print(f"\n{nama}: Akan ku buktikan jika aku bukanlah pendekar bodoh!")
        time.sleep(0.5)
        print(f"\nBoss Blue: Sejak kamu menginjakkan kaki di hutan ini, pedang pusakamu yang memuat daya tahan 5 kali tebasan terus menjadi penentu nasibmu.")
        time.sleep(0.5)
        print(f"\nBoss Blue: Di hadapanmu ada 6 buah peti batu terkunci. Di dalam setiap peti terdapat sebuah batu bertuliskan angka acak dari 1 sampai 5.Aku menantang otakmu:")
        time.sleep(0.5)
        print(f"\nBoss Blue: Apakah sudah PASTI ada minimal 2 peti yang berisi batu dengan angka yang SAMA EXACT, tanpa kamu perlu membuka petinya terlebih dahulu?")
        time.sleep(0.5)
        print(f"\nA. Pasti Ada" \
        "B. Belum Tentu" \
        "C. Tidak Mungkin")
        jawab2 = str(input("Apa yang akan kamu pilih?  ")).lower()
        time.sleep(1)

        if jawab2 in ['A','a']:
            print(f"\nBoss Blue: Cih! ternyata kau berhasil, pergilah! aku tak ingin melihat pendekar yang berhasil menjawab pertanyaanku!")
            time.sleep(3)
        elif jawab2 in ['B','b']:
            print(f"\nBoss Blue: Pendekar itu tidak boleh labil, kalau labil sama aja kamu dengan pendekar bodoh lainnya!")
            time.sleep(3)
            daya_tahan_pedang -= 5
        elif jawab2 in ['C','c']:
            print(f"\nBoss Blue: Hahaha! Jawaban yang lucu! Kamu adalah pendekar yang sangat bodoh!")
            time.sleep(3)
            daya_tahan_pedang -= 5
        else:
            print(f"\nBoss Blue: Hey apakah kamu tidak dengar apa pilihannya? sudah bodoh! Tuli juga!")
            time.sleep(3)
            daya_tahan_pedang -= 5
    else:
        print(f"{nama} tidak bisa memilih, seekor naga menyergapnya dari langit")
        time.sleep(3)
        daya_tahan_pedang -= 5

    if daya_tahan_pedang <= 0:
       print('=========================================')
       print('GAME OVER! Kesalahan berpikir dapat menghancurkan segalanya!')
       print(f"{nama} telah menjadi pendekar geprek")
       print('=========================================')
    elif daya_tahan_pedang >= 0:
       print('\n--------------------------------')
       print(
           f'Selamat {nama} berhasil keluar dari The Cursed Forest!'
        )
       print('--------------------------------')












