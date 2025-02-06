from tabulate import tabulate

data = [
    {"No": 1, "Nama Barang": "Martin 00010E Road Series Acoustic Guitar", "Harga": 18000000, "Jenis": "Guitar"},
    {"No": 2, "Nama Barang": "Gibson Montana G-45 Standard Acoustic/Electric", "Harga": 15000000, "Jenis": "Guitar"},
    {"No": 3, "Nama Barang": "Yamaha JU109 PW Upright Piano", "Harga": 43460000, "Jenis": "Piano"}
]

headers = ["No", "Nama Barang", "Harga", "Jenis"]

def daftar(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid'))

def huruf(prompt):
    while True:
        inp = input(prompt).title()
        if all(i.isalpha() or i.isspace() for i in inp):
            return inp
        else:
            print('Inputan harus huruf')

def number(prompt):
    while True:
        inp = input(prompt)
        if inp.isdigit():
            return int(inp)
        else:
            print('Inputan harus angka')

def create(data):
    while True:
        nomor = len(data) + 1
        nama = input('\nMasukkan Nama Barang: ').title()
        harga = number('\nMasukkan Harga: ')
        jenis = huruf('\nMasukkan Jenis Barang: ').title()
        data.append({"No": nomor, "Nama Barang": nama, "Harga": harga, "Jenis": jenis})
        print("\nBarang berhasil ditambahkan!")
        daftar(data)
        lanjut = input("\nApakah ingin menambah data lagi? (y/n): ").lower()
        if lanjut != 'y':
            return

def update(data):
    while True:
        daftar(data)  
        idx = number("\nMasukkan nomor barang yang ingin diubah: ") - 1  
        if 0 <= idx < len(data):  
            while True:
                print("\n1. Ubah Nama Barang")
                print("2. Ubah Harga")
                print("3. Ubah Jenis Barang")
                pilihan = number("\nMasukkan nomor pilihan: ")
                if pilihan == 1:
                    data[idx]["Nama Barang"] = input("\nMasukkan Nama Barang Baru: ").title()
                elif pilihan == 2:
                    data[idx]["Harga"] = number("\nMasukkan Harga Baru: ")
                elif pilihan == 3:
                    data[idx]["Jenis"] = huruf("\nMasukkan Jenis Barang Baru: ").title()
                else:
                    print("\nPilihan tidak valid!")
                    continue
                print("\nData berhasil diperbarui!")
                daftar(data)
                lanjut = input("\nApakah ingin mengubah data lagi? (y/n): ").lower()
                if lanjut != 'y':
                    return
        else:
            print("\nNomor barang tidak ditemukan!")

def hapus(data):
    while True:
        daftar(data)
        idx = number("\nMasukkan nomor barang yang ingin dihapus: ") - 1  
        if 0 <= idx < len(data):  
            konfirmasi = input(f"\nApakah Anda yakin ingin menghapus '{data[idx]['Nama Barang']}'? (y/n): ").lower()
            if konfirmasi == 'y':
                del data[idx]
                for i, barang in enumerate(data):
                    barang["No"] = i + 1  
                print("\nBarang berhasil dihapus!")
                daftar(data)
                
            else:
                print("\nPenghapusan dibatalkan.")
        else:
            print("\nNomor barang tidak ditemukan!")

        lanjut = input("\nApakah ingin menghapus data lagi? (y/n): ").lower()
        if lanjut != 'y':
            return

def main():
    while True:
        print('\n======= MENU =======')
        print('\n1. Tambahkan Barang')
        print('2. Ubah Barang')
        print('3. Hapus Barang')
        print('4. Daftar Barang')
        print('5. Keluar App')
        pilihan = number('\nMasukkan Nomor: ')
        
        if pilihan == 1:
            create(data)
        elif pilihan == 2:
            update(data)
        elif pilihan == 3:
            hapus(data)
        elif pilihan == 4:
            daftar(data)
        elif pilihan == 5:
            print('\n======== Terima Kasih ========')
            break
print("                                 ==Welcome==")
print("                              ==Daftar Barang==")
daftar(data)
main()
