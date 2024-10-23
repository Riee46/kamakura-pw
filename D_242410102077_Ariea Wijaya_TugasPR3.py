#SOAL 1
def cek_nilai(variabel):
    if variabel < 7 or (14 < variabel < 17):
        return True
    else:
        return False

# pengecek'an nilai
nilai_saya = 7
hasil_cek = cek_nilai(nilai_saya)

print(f"Apakah nilai {nilai_saya} memenuhi kriteria? {hasil_cek}")


#SOAL 2
#Inisialisasi data awal 
nama = input("masukan nama anda: ") #mohon input nama anda sendiri
rekening = input("nomor rekening: ")#mohon input norek anda sendiri(bebas)
saldo = float(input("saldo: "))#mohon input saldo anda sendiri(bebas)
#Fungsi untuk melakukan penarikan tunai
def tarik_tunai(jumlah):
    global saldo
    if jumlah > saldo :
        print("maaf, saldo tidak mencukupi. ")
    else:
        saldo -= jumlah
        print(f"penarikan berhasil. saldo terbaru: {saldo:.2f}")
#Program saldo (utama)
while True:
    print("\nMenu:")
    print("1. cek saldo")
    print("2. tarik tunai")
    print("3. keluar")
    pilihan = input("pilih menu(1/2/3): ")

    if pilihan == "1":
        print(f"saldo anda saat ini: {saldo:.2f}")
    elif pilihan == "2":
        jumlah_tarik = float(input("masukan jumlah ingin ditarik: "))
        tarik_tunai(jumlah_tarik)
    elif pilihan == "3":
        print("terima kasih telah menggunakan layanan kami, sampai jumpa!")
        break
    else:
        print("pilihan tidak valid, silahkan pilih menu yang benar")


#SOAL 3
# Daftar Harga Barang
harga_ram = 800000
harga_gpu = 12000000
harga_casing = 200000

diskon_ram = harga_ram-(harga_ram*5//100)
diskon_gpu = harga_gpu-(harga_gpu*5//100)
diskon_casing = harga_casing-(harga_casing*5//100)

total = diskon_ram + diskon_gpu + diskon_casing
voucher = ["H4L0D3K"]
total_barang = total-(total*3//100)

print(f"kode voucher = {voucher}")
print("keren kamu fauzul dapet diskon")
kode =(input("masukan voucher: "))
if kode == voucher[0]:
    print("Selamat bang fauzul dapet diskon nich")
    print(f"total yang harus dibayar : Rp {total_barang}")
else:
    print("kode nya salah bang")
    print(f"total yang harus dibayar : Rp {total}")

 

