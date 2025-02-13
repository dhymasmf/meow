from tabulate import tabulate
import random

data = [
    {"Kode": 5729, "Nama Barang": "Neko Hoodie ふわふわ", "Harga": 185000, "Kategori": "Jaket", "Stok": 7},
    {"Kode": 8391, "Nama Barang": "Whisker Kimono シャツ", "Harga": 180000, "Kategori": "Kemeja", "Stok": 5},
    {"Kode": 2468, "Nama Barang": "Meow Mochi Tote バッグ", "Harga": 110000, "Kategori": "Tas", "Stok": 0},
    {"Kode": 9135, "Nama Barang": "Fuwafuwa Nyan Tee", "Harga": 145000, "Kategori": "Kaos", "Stok": 12},
    {"Kode": 6852, "Nama Barang": "Pawsteps Sneakers にゃん", "Harga": 310000, "Kategori": "Sepatu", "Stok": 3},
    {"Kode": 4973, "Nama Barang": "Kawaii Paws Bracelet", "Harga": 95000, "Kategori": "Aksesoris", "Stok": 15},
    {"Kode": 7284, "Nama Barang": "Sakura Neko Sling バッグ", "Harga": 155000, "Kategori": "Tas", "Stok": 8},
    {"Kode": 3691, "Nama Barang": "Shiro Neko Fluffy シャツ", "Harga": 165000, "Kategori": "Kemeja", "Stok": 0},
    {"Kode": 1027, "Nama Barang": "Kuro Neko Cargo パンツ", "Harga": 160000, "Kategori": "Celana", "Stok": 10},
    {"Kode": 8316, "Nama Barang": "Meow Senpai Denim ジャケット", "Harga": 275000, "Kategori": "Jaket", "Stok": 0},
    {"Kode": 2745, "Nama Barang": "Purrfect Marshmallow Tee", "Harga": 125000, "Kategori": "Kaos", "Stok": 0},
    {"Kode": 9163, "Nama Barang": "Meow-chan Leather ベルト", "Harga": 130000, "Kategori": "Aksesoris", "Stok": 0},
    {"Kode": 6048, "Nama Barang": "Nyan Dash Sneakers", "Harga": 280000, "Kategori": "Sepatu", "Stok": 0},
    {"Kode": 3157, "Nama Barang": "Fuwa Meow Sweatpants", "Harga": 140000, "Kategori": "Celana", "Stok": 0},
]

headers = ["Kode", "Nama Barang", "Harga", "Kategori", "Stok"]

def daftar(data):
    print("\n===== Daftar Barang =====")
    if data:
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
    else:
        print("\nTidak ada barang dalam daftar.")

def letters(prompt):
    while True:
        inp = input(prompt)
        if inp.replace(" ", "").isalpha():
            return inp
        else:
            print("Inputan harus huruf.")

def number(prompt):
    while True:
        inp = input(prompt)
        if inp.isdigit():
            return int(inp)
        else:
            print("Inputan harus angka.")

def generate_unique_code(data):
    while True:
        kode = random.randint(1000, 9999)
        if kode not in [item["Kode"] for item in data]:
            return kode

def create(data):
    print("\n===== Tambahkan Barang Baru =====")
    while True:
        kode = generate_unique_code(data)
        nama = input('\nMasukkan Nama Barang: ').title()
        harga = number('Masukkan Harga: ')
        print("Pilih kategori barang:")
        print("1. Kaos")
        print("2. Kemeja")
        print("3. Celana")
        print("4. Sepatu")
        print("5. Tas")
        print("6. Aksesoris")
        while True:
            pilihan = number("Masukkan nomor kategori: ")
            if pilihan == 1:
                Kategori = "Kaos"
            elif pilihan == 2:
                Kategori = "Kemeja"
            elif pilihan == 3:
                Kategori = "Celana"
            elif pilihan == 4:
                Kategori = "Sepatu"
            elif pilihan == 5:
                Kategori = "Tas"
            elif pilihan == 6:
                Kategori = "Aksesoris"
            else:
                print("Pilihan tidak valid, silakan masukkan angka 1-6.")
                continue
            break
        stok = number('Masukkan Stok Barang: ')
        data.append({"Kode": kode, "Nama Barang": nama, "Harga": harga, "Kategori": Kategori, "Stok": stok})
        print("\nBarang berhasil ditambahkan!\n")
        daftar(data)
        while True:
            lanjut = letters("\nApakah ingin menambah data lagi? (Yes/No): ").lower()
            if lanjut in ('yes', 'no'):
                break
            print("Masukkan hanya 'Yes' untuk lanjut atau 'No' untuk kembali ke menu.")
        if lanjut == 'no':
            return

def update(data):
    while True:
        daftar(data)
        print("\n===== Ubah Daftar Barang =====")
        kode = number("\nMasukkan kode barang yang ingin diubah (0 untuk batal): ")
        item = None
        for barang in data:
            if barang["Kode"] == kode:
                item = barang
                break
        if item:
            while True:
                print("\n1. Ubah Nama Barang")
                print("2. Ubah Harga")
                print("3. Ubah Kategori Barang")
                print("4. Ubah Stok Barang")
                pilihan = number("\nMasukkan nomor pilihan: ")
                if pilihan == 1:
                    item["Nama Barang"] = input("\nMasukkan Nama Barang Baru: ").title()
                elif pilihan == 2:
                    item["Harga"] = number("\nMasukkan Harga Baru: ")
                elif pilihan == 3:
                    while True:
                        print("\nPilih Kategori Barang Baru:")
                        print("1. Kaos")
                        print("2. Kemeja")
                        print("3. Celana")
                        print("4. Sepatu")
                        print("5. Tas")
                        print("6. Aksesoris")
                        kategori_pilihan = number("\nMasukkan nomor kategori: ")
                        if kategori_pilihan == 1:
                            item["Kategori"] = "Kaos"
                        elif kategori_pilihan == 2:
                            item["Kategori"] = "Kemeja"
                        elif kategori_pilihan == 3:
                            item["Kategori"] = "Celana"
                        elif kategori_pilihan == 4:
                            item["Kategori"] = "Sepatu"
                        elif kategori_pilihan == 5:
                            item["Kategori"] = "Tas"
                        elif kategori_pilihan == 6:
                            item["Kategori"] = "Aksesoris"
                        else:
                            print("\nPilihan tidak valid, silakan masukkan angka 1-6.")
                            continue
                        break
                elif pilihan == 4:
                    item["Stok"] = number("\nMasukkan Stok Baru: ")
                elif pilihan == 0:
                    print("\nUbah barang dibatalkan")
                    break
                else:
                    print("\nPilihan tidak valid!")
                    continue
                print("\nData berhasil diperbarui!")
                daftar(data)
                while True:
                    lanjut = letters("\nApakah ingin mengubah data lagi? (Yes/No): ").lower()
                    if lanjut in ('yes', 'no'):
                        break
                    print("Masukkan hanya 'Yes' untuk lanjut atau 'No' untuk kembali ke menu.")
                if lanjut == 'no':
                    return
        elif kode == 0:
            print("\nUbah barang dibatalkan")
            break
        else:
            print("\nKode barang tidak ditemukan!")

def delete(data):
    while True:
        daftar(data)
        print("\n===== Hapus Daftar Barang =====")
        kode = number("\nMasukkan kode barang yang ingin dihapus (Masukan 0 jika batal): ")
        item = None
        for barang in data:
            if barang["Kode"] == kode:
                item = barang
                break
        if item:
            while True:
                konfirmasi = letters(f"\nApakah Anda yakin ingin menghapus '{item['Nama Barang']}'? (Yes/No): ").lower()
                if konfirmasi == 'yes':
                    recycle_bin.append(item)
                    data.remove(item)
                    print("\nBarang berhasil dipindahkan ke Recycle Bin!")
                    daftar(data)
                    break
                elif konfirmasi == 'no':
                    print("\nPenghapusan dibatalkan.")
                    break
                else:
                    print("\nMasukkan hanya 'Yes' atau 'No'.")
        elif kode == 0:
            print("\nHapus barang dibatalkan")
        else:
            print("\nKode barang tidak ditemukan!")
        while True:
            lanjut = letters("\nApakah ingin hapus data lagi? (Yes/No): ").lower()
            if lanjut in ('yes', 'no'):
                break
            print("Masukkan hanya 'Yes' untuk lanjut atau 'No' untuk kembali ke menu.")
        if lanjut == 'no':
            return

recycle_bin = []

def restore(data, recycle_bin):
    print("\n===== Restore Barang =====")
    if not recycle_bin:
        print("\nRecycle Bin kosong! Tidak ada barang untuk dipulihkan.")
        return
    print("\nBarang dalam Recycle Bin:")
    print(tabulate(recycle_bin, headers="keys", tablefmt="fancy_grid"))
    while True:
        kode = number("\nMasukkan kode barang yang ingin dipulihkan (Masukan 0 jika batal): ")
        if kode == 0:
            print("\nRestore barang dibatalkan.")
            return
        item = None
        for barang in recycle_bin:
            if barang["Kode"] == kode:
                item = barang
                break
        if item:
            data.append(item)
            recycle_bin.remove(item)
            print(f"\nBarang '{item['Nama Barang']}' berhasil dipulihkan ke daftar barang!")
            return
        else:
            print("\nKode barang tidak ditemukan dalam Recycle Bin. Coba lagi.")

def data_filter(data):
    print("\n===== Filter Barang Berdasarkan Kategori =====")
    print("Pilih kategori barang yang dicari:")
    print("1. Kaos")
    print("2. Kemeja")
    print("3. Celana")
    print("4. Sepatu")
    print("5. Tas")
    print("6. Aksesoris")
    pilihan = input("Masukkan nomor kategori: ")
    if pilihan == "1":
        Kategori_dicari = "Kaos"
    elif pilihan == "2":
        Kategori_dicari = "Kemeja"
    elif pilihan == "3":
        Kategori_dicari = "Celana"
    elif pilihan == "4":
        Kategori_dicari = "Sepatu"
    elif pilihan == "5":
        Kategori_dicari = "Tas"
    elif pilihan == "6":
        Kategori_dicari = "Aksesoris"
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        return
    hasil_filter = [item for item in data if item["Kategori"].lower() == Kategori_dicari.lower()]
    if hasil_filter:
        print(tabulate(hasil_filter, headers="keys", tablefmt="fancy_grid"))
    else:
        print("Barang dengan kategori tersebut tidak ditemukan.")

cart = []

def to_cart(data, cart):
    while True:
        daftar(data)
        print("\n===== Tambah ke Keranjang =====")
        kode = number("\nMasukkan kode barang yang ingin dimasukkan ke keranjang: ")
        item = None
        for barang in data:
            if barang["Kode"] == kode:
                item = barang
                break
        if item:
            if item["Stok"] == 0:
                print(f"\nMaaf, stok '{item['Nama Barang']}' sedang kosong!")
            else:
                while True:
                    jumlah = number(f"\nMasukkan jumlah yang ingin dibeli (Stok tersedia: {item['Stok']}): ")
                    if jumlah > item["Stok"]:
                        print("\nJumlah melebihi stok yang tersedia! Silakan masukkan jumlah yang valid.")
                    elif jumlah <= 0:
                        print("\nJumlah harus lebih dari 0! Silakan masukkan jumlah yang valid.")
                    else:
                        break
                found = False
                for produk in cart:
                    if produk["Kode"] == item["Kode"]:
                        produk["Jumlah"] += jumlah
                        found = True
                        break
                if not found:
                    cart.append({"Kode": item["Kode"], "Nama Barang": item["Nama Barang"], "Harga": item["Harga"], "Jumlah": jumlah})
                print(f"\n'{item['Nama Barang']}' sebanyak {jumlah} ditambahkan ke keranjang!")
        else:
            print("\nKode barang tidak ditemukan!")

        while True:
            lanjut = letters("\nApakah ingin menambah barang ke keranjang lagi? (Yes/No): ").lower()
            if lanjut in ('yes', 'no'):
                break
            print("Masukkan hanya 'Yes' untuk lanjut atau 'No' untuk kembali ke menu.")
        if lanjut == 'no':
            return

def see_cart(cart):
    if not cart:
        print("\nKeranjang belanja kosong.")
    else:
        print("\n===== Keranjang =====")
        print(tabulate(cart, headers="keys", tablefmt="fancy_grid"))

def remove_cart(cart):
    print("\n===== Hapus Barang =====")
    if not cart:
        print("\nKeranjang masih kosong!")
        return
    see_cart(cart)
    kode = number("\nMasukkan kode barang yang ingin dihapus dari keranjang: ")
    for item in cart:
        if item["Kode"] == kode:
            cart.remove(item)
            print(f"\nBarang '{item['Nama Barang']}' berhasil dihapus dari keranjang.")
            return
    print("\nKode barang tidak ditemukan di keranjang!")

def checkout(data, cart):
    print("\n===== CHECKOUT!! =====")
    if not cart:
        print("\nKeranjang masih kosong! Tambahkan barang terlebih dahulu.")
        return
    total = 0
    for item in cart:
        total += item["Harga"] * item["Jumlah"]
        for barang in data:
            if barang["Kode"] == item["Kode"]:
                barang["Stok"] -= item["Jumlah"]
    diskon = 0
    if total > 1_000_000:
        diskon = 0.25
    elif total > 500_000:
        diskon = 0.10

    total_diskon = int(total * diskon)
    total_setelah_diskon = total - total_diskon
    print("\nCheckout berhasil! Berikut barang yang dibeli:")
    see_cart(cart)
    print(f"\nTotal: Rp. {total:,}")
    if diskon > 0:
        print(f"Selamat anda mendapatkan Diskon sebesar: {int(diskon * 100)}% !!")
        print(f"Diskon {int(diskon * 100)}%: Rp. {total_diskon:,}")
        print(f"Total uang yang harus di bayar: Rp. {total_setelah_diskon:,}")
    else:
        print("Tidak ada diskon yang diterapkan.")
    while True:
        uang = number("\nMasukkan jumlah uang yang dibayarkan: Rp. ")
        if uang < total_setelah_diskon:
            print("\nUang tidak cukup! Silakan masukkan jumlah yang sesuai atau lebih.")
        else:
            kembalian = uang - total_setelah_diskon
            if kembalian > 0:
                print(f"\nPembayaran berhasil! Kembalian Anda: Rp. {kembalian:,}")
            else:
                print("\nPembayaran berhasil! Uang pas, tidak ada kembalian.")
            cart.clear()
            break

def main_admin():
    print("\nDaftar Barang Saat Ini:")
    daftar(data)
    while True:
        print('\n======= MENU ADMIN =======')
        print('1. Daftar Barang')
        print('2. Tambahkan Barang')
        print('3. Ubah Daftar Barang')
        print('4. Hapus Barang')
        print('5. Restore Barang')
        print('6. Keluar')
        pilihan = number('\nMasukkan Nomor: ')
        if pilihan == 1:
            daftar(data)
        elif pilihan == 2:
            create(data)
        elif pilihan == 3:
            update(data)
        elif pilihan == 4:
            delete(data)
        elif pilihan == 5:
            restore(data, recycle_bin)
        elif pilihan == 6:
            print('\n======== Terima Kasih, Admin ========')
            break
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")

def main_customer():
    cart = []
    while True:
        print('\n======= MENU CUSTOMER =======')
        print('1. Lihat Daftar Barang')
        print('2. Filter by Kategori')
        print('3. Tambah ke Keranjang')
        print('4. Lihat Keranjang')
        print('5. Hapus Barang dari Keranjang')
        print('6. Checkout')
        print('7. Keluar')
        pilihan = number('\nMasukkan Nomor: ')
        if pilihan == 1:
            daftar(data)
        elif pilihan == 2:
            data_filter(data)
        elif pilihan == 3:
            to_cart(data, cart)
        elif pilihan == 4:
            see_cart(cart)
        elif pilihan == 5:
            remove_cart(cart)
        elif pilihan == 6:
            checkout(data, cart)
        elif pilihan == 7:
            print('\n======== Terima Kasih, Customer ========')
            break
        else:
            print('\nPilihan tidak valid! Silakan coba lagi.')

def login():
    while True:
        print("\n======= LOGIN =======")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Customer")
        print("3. Keluar")
        pilihan = number("\nMasukkan pilihan: ")
        if pilihan == 1:
            print("\nMasukan Username dan Password")
            username = input("Username: ")
            password = input("Password: ")
            if username == "admin" and password == "admin":
                print("\nLogin berhasil!")
                print("Selamat datang, Admin.")
                main_admin()
            else:
                print("\nLogin gagal! Username atau password salah.\n")
        elif pilihan == 2:
            print("\nLogin berhasil sebagai Customer.\n")
            main_customer()
        elif pilihan == 3:
            print("\nTerima kasih telah menggunakan aplikasi.\n")
            break
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")

login()
### WTF TEMBUS 450? ###