from tabulate import tabulate
import random

data = [
    {"Kode": 5729, "Nama Barang": "Kitty Cozy Hoodie", "Harga": 185000, "Kategori": "Jaket", "Stok": 7},
    {"Kode": 8391, "Nama Barang": "Whisker Fluffy Shirt", "Harga": 180000, "Kategori": "Kemeja", "Stok": 5},
    {"Kode": 2468, "Nama Barang": "Meow Mochi Tote", "Harga": 110000, "Kategori": "Tas", "Stok": 0},
    {"Kode": 9135, "Nama Barang": "Soft Paws Tee", "Harga": 145000, "Kategori": "Kaos", "Stok": 12},
    {"Kode": 6852, "Nama Barang": "Pawsteps Sneakers", "Harga": 310000, "Kategori": "Sepatu", "Stok": 3},
    {"Kode": 4973, "Nama Barang": "Kawaii Paw Bracelet", "Harga": 95000, "Kategori": "Aksesoris", "Stok": 15},
    {"Kode": 7284, "Nama Barang": "Sakura Cat Sling Bag", "Harga": 155000, "Kategori": "Tas", "Stok": 2},
    {"Kode": 3691, "Nama Barang": "Snowy Whiskers Shirt", "Harga": 165000, "Kategori": "Kemeja", "Stok": 0},
    {"Kode": 1027, "Nama Barang": "Shadow Kitty Cargo Pants", "Harga": 160000, "Kategori": "Celana", "Stok": 10},
    {"Kode": 8316, "Nama Barang": "Meowster Denim Jacket", "Harga": 275000, "Kategori": "Jaket", "Stok": 4},
    {"Kode": 2745, "Nama Barang": "Purrfect Marshmallow Tee", "Harga": 125000, "Kategori": "Kaos", "Stok": 0},
    {"Kode": 9163, "Nama Barang": "Meow-chan Leather Belt", "Harga": 130000, "Kategori": "Aksesoris", "Stok": 11},
    {"Kode": 6048, "Nama Barang": "Zoomie Cat Sneakers", "Harga": 280000, "Kategori": "Sepatu", "Stok": 0},
    {"Kode": 3157, "Nama Barang": "Furry Meow Sweatpants", "Harga": 140000, "Kategori": "Celana", "Stok": 20},
]

headers = ["Kode", "Nama Barang", "Harga", "Kategori", "Stok"]

dictkategori = {
    1: "Kaos",
    2: "Kemeja",
    3: "Celana",
    4: "Sepatu",
    5: "Tas",
    6: "Aksesoris"
}

def generate_unique_code(data):
    while True:
        kode = random.randint(1000, 9999)
        if kode not in [item["Kode"] for item in data]:
            return kode

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

def yesno(prompt):
    while True:
        lanjut = letters(prompt).strip().lower()
        if lanjut in ("yes", "y"):
            return True
        elif lanjut in ("no", "n"):
            return False
        print("Masukkan hanya 'Yes' atau 'No' (atau 'Y' / 'N').")

def get_harga(item):
    return item.get("Harga", float('inf'))
def LowestPrice(data):
    if not data:
        print("\nTidak ada barang yang tersedia.")
        return
    sorted_data = sorted(data, key=get_harga)
    print("\n===== Barang dari Harga Terendah =====")
    print(tabulate(sorted_data, headers="keys", tablefmt="fancy_grid"))

def get_stok(item):
    return item.get("Stok", 0)
def HighestStok(data):
    if not data:
        print("\nTidak ada barang yang tersedia.")
        return
    sorted_data = sorted(data, key=get_stok, reverse=True)
    print("\n===== Barang dari Stok Terbanyak =====")
    print(tabulate(sorted_data, headers="keys", tablefmt="fancy_grid"))

def PriceRange(data):
    if not data:
        print("\nTidak ada barang yang tersedia.")
        return
    min_price = number("Masukkan harga minimum: ")
    max_price = number("Masukkan harga maksimum: ")
    if min_price > max_price:
        print("\nHarga minimum tidak boleh lebih besar dari harga maksimum!")
        return
    filtered_data = [item for item in data if min_price <= item.get("Harga", float('inf')) <= max_price]
    if filtered_data:
        print(f"\n===== Barang dengan Harga {min_price} - {max_price} =====")
        print(tabulate(filtered_data, headers="keys", tablefmt="fancy_grid"))
    else:
        print(f"\nTidak ada barang dalam rentang harga {min_price} - {max_price}.")

def byname(data):
    if not data:
        print("\nDaftar barang kosong!")
        return
    keyword = input("\nMasukkan nama barang yang ingin dicari: ").strip().lower()
    hasil_pencarian = [barang for barang in data if keyword in barang["Nama Barang"].lower()]
    if hasil_pencarian:
        print("\nBarang ditemukan:")
        print(tabulate(hasil_pencarian, headers="keys", tablefmt="fancy_grid"))
    else:
        print("\nBarang tidak ditemukan!")

def KategoriFilt(data):
    print("\n===== Filter Barang Berdasarkan Kategori =====")
    while True:
        for key, value in dictkategori.items():
            print(f"{key}. {value}")
        print("7. Keluar")
        pilihan = number("\nMasukkan nomor kategori: ")
        if pilihan == 7:
            print("\nKembali ke menu sebelumnya.")
            return
        Kategori_dicari = dictkategori.get(pilihan)
        if not Kategori_dicari:
            print("Pilihan tidak valid, silakan coba lagi.")
            continue
        hasil_filter = [item for item in data if item["Kategori"].lower() == Kategori_dicari.lower()]
        print("\n===== Hasil Filter =====")
        if hasil_filter:
            print(tabulate(hasil_filter, headers="keys", tablefmt="fancy_grid"))
        else:
            print("\nBarang dengan kategori tersebut tidak ditemukan.")
        if not yesno("\nIngin memilih kategori lain? (Yes/No): "):
            print("\nKembali ke menu sebelumnya.")
            return

def read_items(data):
    print("\n===== Daftar Barang =====")
    if not data:
        print("\nTidak ada barang yang tersedia.")
        return
    print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
    while True:
        print("\n===== Opsi Filter & Pencarian =====")
        print("1. Cari berdasarkan nama barang")
        print("2. Filter berdasarkan kategori")
        print("3. Urutkan dari harga terendah")
        print("4. Urutkan dari stok terbanyak")
        print("5. Cari berdasarkan rentang harga")
        print("6. Keluar")
        pilihan = number("Masukkan pilihan: ")
        if pilihan == 1:
            byname(data)
        elif pilihan == 2:
            KategoriFilt(data)
        elif pilihan == 3:
            LowestPrice(data)
        elif pilihan == 4:
            HighestStok(data)
        elif pilihan == 5:
            PriceRange(data)
        elif pilihan == 6:
            print("\nKeluar dari menu filter.")
            break
        else:
            print("\nPilihan tidak valid, coba lagi.")

def create(data):
    print("\n===== Tambahkan Barang Baru =====")
    while True:
        kode = generate_unique_code(data)
        while True:
            nama = input("\nMasukkan Nama Barang (Masukkan 0 jika batal): ").title().strip()
            if nama == "0":
                print("\nTambah barang dibatalkan.")
                return
            if any(barang["Nama Barang"].lower() == nama.lower() for barang in data):
                print("\nNama barang sudah ada! Silakan masukkan nama lain.")
            else:
                break
        harga = number("Masukkan Harga: ")
        print("\nPilih kategori barang:")
        for key, value in dictkategori.items():
            print(f"{key}. {value}")
        while True:
            pilihan = number("Masukkan nomor kategori: ")
            Kategori = dictkategori.get(pilihan)
            if Kategori:
                break
            print("Pilihan tidak valid, silakan masukkan angka yang sesuai.")
        stok = number("Masukkan Stok Barang: ")
        data.append({
            "Kode": kode,
            "Nama Barang": nama,
            "Harga": harga,
            "Kategori": Kategori,
            "Stok": stok
        })
        print("\nBarang berhasil ditambahkan!\n")
        daftar(data)
        if not yesno("\nApakah ingin menambahkan barang lagi? (Yes/No): "):
            print("\nKembali ke menu utama.")
            break

def update(data):
    while True:
        daftar(data)
        print("\n===== Ubah Daftar Barang =====")
        kode = number("\nMasukkan kode barang yang ingin diubah (Masukkan 0 jika batal): ")
        if kode == 0:
            print("\nUbah barang dibatalkan.")
            break
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
                print("5. Selesai mengubah barang ini")
                pilihan = number("\nMasukkan nomor pilihan: ")
                if pilihan == 1:
                    item["Nama Barang"] = input("\nMasukkan Nama Barang Baru: ").title().strip()
                elif pilihan == 2:
                    item["Harga"] = number("\nMasukkan Harga Baru: ")
                elif pilihan == 3:
                    print("\nPilih Kategori Barang Baru:")
                    for key, value in dictkategori.items():
                        print(f"{key}. {value}")
                    while True:
                        kategori_pilihan = number("\nMasukkan nomor kategori: ")
                        if kategori_pilihan in dictkategori:
                            item["Kategori"] = dictkategori[kategori_pilihan]
                            break
                        print("\nPilihan tidak valid, silakan masukkan angka yang sesuai.")
                elif pilihan == 4:
                    item["Stok"] = number("\nMasukkan Stok Baru: ")
                elif pilihan == 5:
                    print("\nSelesai mengubah barang ini.")
                    break
                else:
                    print("\nPilihan tidak valid! Coba lagi.")
                    continue
                print("\nData berhasil diperbarui!")
                daftar(data)
            if not yesno("\nApakah ingin mengubah barang lain? (Yes/No): "):
                print("\nKembali ke menu utama.")
                return
        else:
            print("\nKode barang tidak ditemukan!")

recycle_bin = []

def delete(data):
    while True:
        if not data:
            print("\nDaftar barang kosong! Tidak ada yang bisa dihapus.")
            return
        daftar(data)
        print("\n===== Hapus Daftar Barang =====")
        kode = number("\nMasukkan kode barang yang ingin dihapus (Masukkan 0 jika batal): ")
        if kode == 0:
            print("\nHapus barang dibatalkan.")
            return
        item = next((barang for barang in data if barang["Kode"] == kode), None)
        if item:
            if yesno("\nApakah Anda yakin ingin menghapus barang ini? (Yes/No): "):
                recycle_bin.append(item)
                data.remove(item)
                print("\nBarang berhasil dipindahkan ke Recycle Bin!")
                daftar(data)
            else:
                print("\nPenghapusan dibatalkan.")
        else:
            print("\nKode barang tidak ditemukan!")
        if not yesno("\nApakah ingin menghapus barang lain? (Yes/No): "):
            return

def restore(data):
    print("\n===== Restore Barang / Hapus Permanen =====")
    if not recycle_bin:
        print("\nRecycle Bin kosong! Tidak ada barang untuk diproses.")
        return
    while True:
        if not recycle_bin:
            print("\nRecycle Bin kosong! Tidak ada barang untuk diproses.")
            return
        print("\nBarang dalam Recycle Bin:")
        print(tabulate(recycle_bin, headers="keys", tablefmt="fancy_grid"))
        kode = number("\nMasukkan kode barang yang ingin diproses (Masukkan 0 jika batal): ")
        if kode == 0:
            print("\nOperasi dibatalkan.")
            return
        item = None
        for barang in recycle_bin:
            if barang["Kode"] == kode:
                item = barang
                break
        if item is None:
            print("\nKode barang tidak ditemukan dalam Recycle Bin. Coba lagi.")
            continue
        print("\nPilih tindakan:")
        print("1. Restore barang ke daftar")
        print("2. Hapus barang secara permanen")
        pilihan = number("\nMasukkan pilihan: ")
        if pilihan == 1:
            data.append(item)
            recycle_bin.remove(item)
            print(f"\nBarang '{item['Nama Barang']}' berhasil dipulihkan ke daftar barang!")
        elif pilihan == 2:
            if yesno("\nApakah Anda yakin ingin menghapus barang ini secara permanen? (Yes/No): "):
                recycle_bin.remove(item)
                print(f"\nBarang '{item['Nama Barang']}' telah dihapus secara permanen.")
            else:
                print("\nPenghapusan dibatalkan.")
        else:
            print("\nPilihan tidak valid! Silakan pilih 1 atau 2.")
            continue
        if not recycle_bin:
            print("\nSemua barang telah diproses. Recycle Bin kosong.")
            return
        if not yesno("\nApakah ingin memproses barang lain? (Yes/No): "):
            return

cart = []

def to_cart(data, cart):
    while True:
        daftar(data)
        print("\n===== Tambah ke Keranjang =====")
        kode = number("\nMasukkan kode barang yang ingin dimasukkan ke keranjang (Masukkan 0 jika batal): ")
        if kode == 0:
            print("\nTambah ke keranjang dibatalkan.")
            return
        item = None
        for barang in data:
            if barang["Kode"] == kode:
                item = barang
                break
        if not item:
            print("\nKode barang tidak ditemukan! Silakan coba lagi.")
            continue
        if item["Stok"] == 0:
            print(f"\nMaaf, stok '{item['Nama Barang']}' sedang kosong!")
            continue
        while True:
            jumlah = number(f"\nMasukkan jumlah yang ingin dibeli (Stok tersedia: {item['Stok']}, Masukkan 0 jika batal): ")
            if jumlah == 0:
                print("\nTambah ke keranjang dibatalkan.")
                return
            if jumlah > item["Stok"]:
                print("\nJumlah melebihi stok yang tersedia! Silakan masukkan jumlah yang valid.")
            else:
                break
        item["Stok"] -= jumlah
        for produk in cart:
            if produk["Kode"] == item["Kode"]:
                produk["Jumlah"] += jumlah
                break
        else:
            cart.append({
                "Kode": item["Kode"],
                "Nama Barang": item["Nama Barang"],
                "Harga": item["Harga"],
                "Jumlah": jumlah
            })
        print(f"\n'{item['Nama Barang']}' sebanyak {jumlah} ditambahkan ke keranjang!")
        print("\n===== Isi Keranjang Saat Ini =====")
        print(tabulate(cart, headers="keys", tablefmt="fancy_grid"))
        if not yesno("\nApakah ingin menambah barang ke keranjang lagi? (Yes/No): "):
            return

def remove_cart(cart):
    print("\n===== Hapus Barang =====")
    if not cart:
        print("\nKeranjang masih kosong!")
        return
    while True:
        print(tabulate(cart, headers="keys", tablefmt="fancy_grid"))
        kode = number("\nMasukkan kode barang yang ingin dihapus dari keranjang (Masukkan 0 untuk batal): ")
        if kode == 0:
            print("\nHapus barang dibatalkan.")
            return
        item_dihapus = None
        for item in cart:
            if item["Kode"] == kode:
                item_dihapus = item
                break
        if item_dihapus:
            if yesno(f"\nApakah Anda yakin ingin menghapus '{item_dihapus['Nama Barang']}' dari keranjang? (Yes/No): "):
                cart.remove(item_dihapus)
                print(f"\nBarang '{item_dihapus['Nama Barang']}' berhasil dihapus dari keranjang.")
                for barang in data:
                    if barang["Kode"] == item_dihapus["Kode"]:
                        barang["Stok"] += item_dihapus["Jumlah"]
                        print(f"Stok '{barang['Nama Barang']}' dikembalikan. Stok sekarang: {barang['Stok']}")
                        break
                if not cart:
                    print("\nKeranjang sekarang kosong.")
                    return
            else:
                print("\nPenghapusan barang dibatalkan.")
        else:
            print("\nKode barang tidak ditemukan di keranjang!")
        if not yesno("\nApakah ingin menghapus barang lain dari keranjang? (Yes/No): "):
            return

def see_cart(cart, data):
    if not cart:
        print("\nKeranjang belanja kosong.")
        return
    while True:
        print("\n===== Keranjang =====")
        print(tabulate(cart, headers="keys", tablefmt="fancy_grid"))
        print("\nPilihan:")
        print("1. Hapus barang dari keranjang")
        print("2. Hapus semua barang di keranjang")
        print("3. Checkout")
        print("4. Keluar")
        pilihan = number("\nMasukkan pilihan: ")
        if pilihan == 1:
            remove_cart(cart, data)
        elif pilihan == 2:
            if yesno("\nApakah Anda yakin ingin menghapus semua barang di keranjang? (Yes/No): "):
                for item in cart:
                    for barang in data:
                        if barang["Kode"] == item["Kode"]:
                            barang["Stok"] += item["Jumlah"]
                            break
                cart.clear()
                print("\nKeranjang telah dikosongkan, barang telah dikembalikan ke stok!")
                return
        elif pilihan == 3:
            checkout(cart)
            return
        elif pilihan == 4:
            return
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def checkout(cart):
    print("\n===== CHECKOUT!! =====")
    if not cart:
        print("\nKeranjang masih kosong! Tambahkan barang terlebih dahulu.")
        return
    total = sum(item["Harga"] * item["Jumlah"] for item in cart)
    diskon = 0.25 if total > 1000000 else 0.10 if total > 500000 else 0
    total_diskon = int(total * diskon)
    total_setelah_diskon = total - total_diskon
    print("\nCheckout berhasil! Berikut barang yang dibeli:")
    print(tabulate(cart, headers="keys", tablefmt="fancy_grid"))
    print(f"\nTotal: Rp. {total:,}")
    if diskon > 0:
        print(f"Selamat! Anda mendapatkan diskon sebesar {int(diskon * 100)}%!")  
        print(f"Diskon: Rp. {total_diskon:,}")
        print(f"Total yang harus dibayar: Rp. {total_setelah_diskon:,}")
    else:
        print("Tidak ada diskon yang diterapkan.")
    while True:
        uang = number("\nMasukkan jumlah uang yang dibayarkan: Rp. ")
        if uang < total_setelah_diskon:
            print("\nUang tidak cukup! Silakan masukkan jumlah yang sesuai atau lebih.")
        elif uang < 0:
            print("\nJumlah uang tidak boleh negatif! Silakan masukkan jumlah yang valid.")
        else:
            kembalian = uang - total_setelah_diskon
            print("\nPembayaran berhasil!")
            if kembalian > 0:
                print(f"Kembalian Anda: Rp. {kembalian:,}")
            else:
                print("Uang pas, tidak ada kembalian.")
            cart.clear()
            break

def main_admin():
    while True:
        print('\n======= MENU ADMIN =======')
        print('1. Lihat Daftar Barang')
        print('2. Tambahkan Barang')
        print('3. Ubah Barang')
        print('4. Hapus Barang')
        print('5. Restore Barang')
        print('6. Keluar')
        pilihan = number('\nMasukkan Nomor: ')
        if pilihan == 1:
            read_items(data)
        elif pilihan == 2:
            create(data)
        elif pilihan == 3:
            update(data)
        elif pilihan == 4:
            delete(data)
        elif pilihan == 5:
            restore(data)
        elif pilihan == 6:
            print('\n======== Terima Kasih, Admin ========')
            break
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")

        print("\nKembali ke menu admin...")

def main_customer():
    cart = [] 
    while True:
        print('\n======= MENU CUSTOMER =======')
        print('1. Lihat Daftar Barang')
        print('2. Filter Barang Berdasarkan Kategori')
        print('3. Tambahkan Barang ke Keranjang')
        print('4. Lihat & Kelola Keranjang')
        print('5. Checkout')
        print('6. Keluar')
        pilihan = number('\nMasukkan Nomor: ')
        if pilihan == 1:
            read_items(data)
        elif pilihan == 2:
            KategoriFilt(data)
        elif pilihan == 3:
            to_cart(data, cart)
        elif pilihan == 4:
            see_cart(cart, data)
        elif pilihan == 5:
            checkout(cart)
        elif pilihan == 6:
            print('\n======== Terima Kasih, Customer ========')
            break
        else:
            print('\nPilihan tidak valid! Silakan coba lagi.')

        print("\nKembali ke menu customer...")

def login():
    while True:
        print("\n======= LOGIN =======")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Customer")
        print("3. Keluar")
        pilihan = number("\nMasukkan pilihan: ")
        if pilihan == 1:
            attempts = 3
            while attempts > 0:
                print("\nMasukkan Username dan Password (Percobaan tersisa:", attempts, ")")
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                if username == "admin" and password == "admin":
                    print("\nLogin berhasil! Selamat datang, Admin.")
                    main_admin()
                    break
                else:
                    attempts -= 1
                    print("\nLogin gagal! Username atau password salah.")
                    if attempts == 0:
                        print("\nTerlalu banyak percobaan gagal. Kembali ke menu utama.")
        elif pilihan == 2:
            print("\nLogin berhasil sebagai Customer.\n")
            main_customer()
        elif pilihan == 3:
            print("\nTerima kasih telah menggunakan aplikasi. Sampai jumpa!\n")
            break
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")

login()