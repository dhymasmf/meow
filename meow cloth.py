from tabulate import tabulate
import random

data = [
    {"Kode": 4821, "Nama Barang": "Hoodie Zip Up", "Harga": 150000, "Jenis": "Jaket", "Stok": 10},
    {"Kode": 7315, "Nama Barang": "Cargo Pants", "Harga": 135000, "Jenis": "Celana", "Stok": 8},
    {"Kode": 1593, "Nama Barang": "Denim Jacket", "Harga": 200000, "Jenis": "Jaket", "Stok": 0},
    {"Kode": 8462, "Nama Barang": "Sneakers Classic", "Harga": 300000, "Jenis": "Sepatu", "Stok": 0},
    {"Kode": 2907, "Nama Barang": "Beanie Hat", "Harga": 50000, "Jenis": "Aksesoris", "Stok": 20},
    {"Kode": 5186, "Nama Barang": "T-Shirt Oversized", "Harga": 120000, "Jenis": "Baju", "Stok": 15},
    {"Kode": 9374, "Nama Barang": "Jogger Pants", "Harga": 140000, "Jenis": "Celana", "Stok": 12},
    {"Kode": 1045, "Nama Barang": "Leather Jacket", "Harga": 350000, "Jenis": "Jaket", "Stok": 5},
    {"Kode": 7629, "Nama Barang": "High-Top Sneakers", "Harga": 275000, "Jenis": "Sepatu", "Stok": 7},
    {"Kode": 3150, "Nama Barang": "Snapback Cap", "Harga": 75000, "Jenis": "Aksesoris", "Stok": 18},
    {"Kode": 6823, "Nama Barang": "Slim Fit Jeans", "Harga": 180000, "Jenis": "Celana", "Stok": 9},
    {"Kode": 2418, "Nama Barang": "Flannel Shirt", "Harga": 160000, "Jenis": "Baju", "Stok": 14},
    {"Kode": 8905, "Nama Barang": "Canvas Tote Bag", "Harga": 65000, "Jenis": "Aksesoris", "Stok": 25},
    {"Kode": 4571, "Nama Barang": "Chelsea Boots", "Harga": 400000, "Jenis": "Sepatu", "Stok": 3},
    {"Kode": 9098, "Nama Barang": "Bomber Jacket", "Harga": 250000, "Jenis": "Jaket", "Stok": 6},
    {"Kode": 1267, "Nama Barang": "Track Pants", "Harga": 130000, "Jenis": "Celana", "Stok": 11},
    {"Kode": 3745, "Nama Barang": "Bucket Hat", "Harga": 60000, "Jenis": "Aksesoris", "Stok": 20},
    {"Kode": 8429, "Nama Barang": "Graphic Hoodie", "Harga": 175000, "Jenis": "Jaket", "Stok": 8},
    {"Kode": 5061, "Nama Barang": "Leather Belt", "Harga": 90000, "Jenis": "Aksesoris", "Stok": 15}
]


recycle_bin = []

headers = ["Kode", "Nama Barang", "Harga", "Jenis", "Stok"]

def daftar(data):
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
        kode = random.randint(1000, 9999)  # Membuat kode unik 4 digit
        if kode not in [item["Kode"] for item in data]:  # Pastikan kode tidak duplikat
            return kode
def create(data):
    while True:
        kode = generate_unique_code(data)  # Menggunakan kode unik acak
        nama = input('\nMasukkan Nama Barang: ').title()
        harga = number('Masukkan Harga: ')
        jenis = letters('Masukkan Jenis Barang: ').title()
        stok = number('Masukkan Stok Barang: ')
        data.append({"Kode": kode, "Nama Barang": nama, "Harga": harga, "Jenis": jenis, "Stok": stok})
        print("\nBarang berhasil ditambahkan!\n")
        daftar(data)
        while True:
            lanjut = input("\nApakah ingin menambah data lagi? (y/n): ").lower()
            if lanjut in ('y', 'n'):
                break
            print("Masukkan hanya 'y' untuk lanjut atau 'n' untuk kembali ke menu.")
        if lanjut != 'y':
            return

def update(data):
    while True:
        daftar(data)  
        kode = number("\nMasukkan kode barang yang ingin diubah: ")  
        item = next((barang for barang in data if barang["Kode"] == kode), None)
        if item:
            while True:
                print("\n1. Ubah Nama Barang")
                print("2. Ubah Harga")
                print("3. Ubah Jenis Barang")
                print("4. Ubah Stok Barang")
                pilihan = number("\nMasukkan nomor pilihan: ")
                if pilihan == 1:
                    item["Nama Barang"] = input("\nMasukkan Nama Barang Baru: ").title()
                elif pilihan == 2:
                    item["Harga"] = number("\nMasukkan Harga Baru: ")
                elif pilihan == 3:
                    item["Jenis"] = letters("\nMasukkan Jenis Barang Baru: ").title()
                elif pilihan == 4:
                    item["Stok"] = number("\nMasukkan Stok Baru: ")
                else:
                    print("\nPilihan tidak valid!")
                    continue
                print("\nData berhasil diperbarui!")
                daftar(data)
                while True:
                            lanjut = input("\nApakah ingin menambah data lagi? (y/n): ").lower()
                            if lanjut in ('y', 'n'):
                                break
                            print("Masukkan hanya 'y' untuk lanjut atau 'n' untuk kembali ke menu.")
                if lanjut != 'y':
                    return
        else:
            print("\nKode barang tidak ditemukan!")

def delete(data):
    while True:
        daftar(data)
        kode = number("\nMasukkan kode barang yang ingin dihapus: ")
        item = next((barang for barang in data if barang["Kode"] == kode), None)
        if item:
            konfirmasi = input(f"\nApakah Anda yakin ingin menghapus '{item['Nama Barang']}'? (y/n): ").lower()
            if konfirmasi == 'y':
                recycle_bin.append(item)
                data.remove(item)
                print("\nBarang berhasil dipindahkan ke Recycle Bin!")
                daftar(data)
            else:
                print("\nPenghapusan dibatalkan.")
        else:
            print("\nKode barang tidak ditemukan!")
        while True:
                    lanjut = input("\nApakah ingin menambah data lagi? (y/n): ").lower()
                    if lanjut in ('y', 'n'):
                        break
                    print("Masukkan hanya 'y' untuk lanjut atau 'n' untuk kembali ke menu.")
        if lanjut != 'y':
            return

def beli(data):
    while True:
        daftar(data)
        kode = number("\nMasukkan kode barang yang ingin dibeli: ")
        item = None
        for barang in data:
            if barang["Kode"] == kode:
                item = barang
                break
        if item:
            if item["Stok"] == 0:
                print(f"\nMaaf, stok '{item['Nama Barang']}' sedang kosong!")
            else:
                jumlah = number(f"\nMasukkan jumlah yang ingin dibeli (Stok tersedia: {item['Stok']}): ")
                if jumlah > item["Stok"]:
                    print("\nJumlah melebihi stok yang tersedia!")
                else:
                    item["Stok"] -= jumlah
                    print(f"\nBerhasil membeli {jumlah} '{item['Nama Barang']}'!")
                    daftar(data)
        else:
            print("\nKode barang tidak ditemukan!")
        while True:
            lanjut = input("\nApakah ingin membeli barang lain? (y/n): ").lower()
            if lanjut in ('y', 'n'):
                break
            print("Masukkan hanya 'y' untuk lanjut atau 'n' untuk kembali ke menu.")
        if lanjut == 'n':
            break

cart = []

def tambah_ke_keranjang(data, cart):
    while True:
        daftar(data)
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
                jumlah = number(f"\nMasukkan jumlah yang ingin dibeli (Stok tersedia: {item['Stok']}): ")
                if jumlah > item["Stok"]:
                    print("\nJumlah melebihi stok yang tersedia!")
                else:
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
            lanjut = input("\nIngin menambahkan barang lain ke keranjang? (y/n): ").lower()
            if lanjut in ('y', 'n'):
                break
            print("Masukkan hanya 'y' untuk lanjut atau 'n' untuk kembali ke menu.")
        if lanjut != 'y':
            break

def lihat_keranjang(cart):
    if not cart:
        print("\nKeranjang belanja kosong.")
    else:
        print("\nIsi Keranjang Belanja:")
        print(tabulate(cart, headers="keys", tablefmt="fancy_grid"))

def hapus_dari_keranjang(cart):
    if not cart:
        print("\nKeranjang masih kosong!")
        return
    lihat_keranjang(cart)
    kode = number("\nMasukkan kode barang yang ingin dihapus dari keranjang: ")
    for item in cart:
        if item["Kode"] == kode:
            cart.remove(item)
            print(f"\nBarang '{item['Nama Barang']}' berhasil dihapus dari keranjang.")
            return
    print("\nKode barang tidak ditemukan di keranjang!")

def checkout(data, cart):
    if not cart:
        print("\nKeranjang masih kosong! Tambahkan barang terlebih dahulu.")
        return
    total = 0
    for item in cart:
        total += item["Harga"] * item["Jumlah"]
        for barang in data:
            if barang["Kode"] == item["Kode"]:
                barang["Stok"] -= item["Jumlah"]
    print("\nCheckout berhasil! Berikut barang yang dibeli:")
    lihat_keranjang(cart)
    print(f"\nTotal yang harus dibayar: Rp. {total:,}")
    while True:
        uang = number("\nMasukkan jumlah uang yang dibayarkan: Rp. ")
        if uang < total:
            print("\nUang tidak cukup! Silakan masukkan jumlah yang sesuai atau lebih.")
        else:
            kembalian = uang - total
            if kembalian > 0:
                print(f"\nPembayaran berhasil! Kembalian Anda: Rp. {kembalian:,}")
            else:
                print("\nPembayaran berhasil! Uang pas, tidak ada kembalian.")
            cart.clear()
            break

def login():
    while True:
        print("\n======= LOGIN =======")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Customer")
        print("3. Keluar")
        pilihan = number("\nMasukkan pilihan: ")
        if pilihan == 1:
            print("\nLogin")
            username = input("Username Admin: ")
            password = input("Password Admin: ")
            if username == "admin" and password == "admin":
                print("\nLogin berhasil! Selamat datang, Admin.\n")
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

def main_admin():
    print("\nDaftar Barang Saat Ini:")
    daftar(data)
    while True:
        print('\n======= MENU ADMIN =======')
        print('1. Tambahkan Barang')
        print('2. Ubah Barang')
        print('3. Hapus Barang')
        print('4. Daftar Barang')
        print('5. Recycle (Kembalikan Barang)')
        print('6. Keluar')
        pilihan = number('\nMasukkan Nomor: ')
        if pilihan == 1:
            create(data)
        elif pilihan == 2:
            update(data)
        elif pilihan == 3:
            delete(data)
        elif pilihan == 4:
            daftar(data)
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
        print('2. Tambah ke Keranjang')
        print('3. Lihat Keranjang')
        print('4. Hapus Barang dari Keranjang')
        print('5. Checkout')
        print('6. Keluar')
        pilihan = number('\nMasukkan Nomor: ')
        if pilihan == 1:
            daftar(data)
        elif pilihan == 2:
            tambah_ke_keranjang(data, cart)
        elif pilihan == 3:
            lihat_keranjang(cart)
        elif pilihan == 4:
            hapus_dari_keranjang(cart)
        elif pilihan == 5:
            checkout(data, cart)
        elif pilihan == 6:
            print('\n======== Terima Kasih, Customer ========')
            break
        else:
            print('\nPilihan tidak valid! Silakan coba lagi.')

login()