# MeowCloth

MeowCloth adalah aplikasi manajemen inventaris berbasis Python untuk toko pakaian bertema kucing. Aplikasi ini memungkinkan pengguna untuk melihat daftar barang, menambahkan ke keranjang, checkout, serta memiliki fitur login sebagai Admin atau Customer.

## Fitur Utama
- **Admin**
  - Melihat daftar barang
  - Menambahkan barang baru
  - Mengubah informasi barang
  - Menghapus barang (dengan fitur Recycle Bin)
  - Mengembalikan barang dari Recycle Bin
- **Customer**
  - Melihat daftar barang dan menyaring berdasarkan kategori
  - Menambahkan barang ke keranjang
  - Mengelola keranjang belanja
  - Checkout dengan sistem diskon

## Instalasi
### Prasyarat
Pastikan Python telah terinstal di sistem Anda. Aplikasi ini menggunakan pustaka `tabulate`, yang dapat diinstal dengan perintah berikut:

```bash
pip install tabulate
```

### Menjalankan Aplikasi
Jalankan aplikasi dengan perintah berikut:

```bash
python MeowCloth.py
```

## Cara Penggunaan
1. Pilih login sebagai Admin atau Customer.
2. Jika login sebagai **Admin**, Anda dapat menambah, mengubah, menghapus, dan mengembalikan barang.
3. Jika login sebagai **Customer**, Anda dapat mencari barang, menyaring berdasarkan kategori, menambah ke keranjang, dan checkout.
4. Checkout akan memberikan diskon 10% untuk pembelian di atas Rp500.000 dan 25% untuk pembelian di atas Rp1.000.000.

## Struktur Kode
- **`data`**: Menyimpan daftar barang.
- **`cart`**: Menyimpan daftar belanja customer.
- **`recycle_bin`**: Menyimpan barang yang dihapus oleh admin.
- **Fungsi utama**:
  - `login()`: Menu utama untuk login sebagai Admin atau Customer.
  - `main_admin()`: Menu utama Admin.
  - `main_customer()`: Menu utama Customer.
  - `create()`, `update()`, `delete()`, `restore()`: Operasi CRUD untuk Admin.
  - `to_cart()`, `remove_cart()`, `see_cart()`, `checkout()`: Pengelolaan keranjang untuk Customer.

## Kontributor
- **Dikembangkan oleh**: Dimas Maulidin Firdaus

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

