# Program Manajemen Stok Kantin
# Baytul Rafli
# Tugas: Membuat program untuk mengelola stok barang di kantin sekolah.

# Struktur data: dictionary dengan kode barang sebagai key dan nama serta stok sebagai value
nama_file = "barang.txt"
def baca_file(nama_file):
    data = {}
    try: # Membaca data dari file
        with open(nama_file, "r", encoding="utf-8") as f: # Membuka file dalam mode baca
            for line in f: # Membaca setiap baris
                kode, nama, stok = line.strip().split(",") # Memisahkan data berdasarkan koma
                data[kode] = {"nama": nama, "stok": int(stok)} # Menyimpan data dalam dictionary 
    except FileNotFoundError: # Jika file tidak ditemukan
        print("File tidak ditemukan, mulai dengan data kosong.") # Memulai dengan data kosong
    return data # Mengembalikan data yang dibaca

# Menyimpan data ke file
def simpan_file(nama_file, data): 
    with open(nama_file, "w", encoding="utf-8") as f: # Membuka file dalam mode tulis 
        for kode, info in data.items(): # Menulis setiap item ke file
            f.write(f"{kode},{info['nama']},{info['stok']}\n") # Format penulisan data
    print("Data berhasil disimpan ke file.") # Konfirmasi penyimpanan

   
# Menampilkan semua barang
def tampilkan_semua(data): 
    print("\n=== Daftar Stok Barang ===") # Header tampilan
    for kode, info in data.items(): # Menampilkan setiap item
        print(f"{kode} - {info['nama']} - Stok: {info['stok']}") # Format tampilan item
    print("==========================") # Footer tampilan


# Mencari barang berdasarkan kode
def cari_barang(data):
    kode = input("Masukkan kode barang: ") # Input kode barang
    if kode in data: # Jika barang ditemukan
        info = data[kode] # Mendapatkan info barang
        print(f"Ditemukan: {kode} - {info['nama']} - Stok: {info['stok']}") # Menampilkan info barang
    else:
        print("Barang tidak ditemukan.") # Jika barang tidak ditemukan


# Menambah barang baru
def tambah_barang(data):
    kode = input("Masukkan kode barang baru: ") # Input kode barang baru
    if kode in data: # Jika kode sudah ada
        print("Kode sudah digunakan.") 
        return
    nama = input("Masukkan nama barang: ") # Input nama barang
    stok = int(input("Masukkan stok awal: ")) # Input stok awal
    data[kode] = {"nama": nama, "stok": stok} # Menyimpan barang baru ke data
    print("Barang berhasil ditambahkan.") # Konfirmasi penambahan barang


# Update stok barang
def update_stok(data):
    kode = input("Masukkan kode barang: ") # Input kode barang
    if kode not in data: # Jika barang tidak ditemukan
        print("Barang tidak ditemukan.") 
        return
    pilihan = input("Tambah stok (+) atau kurangi stok (-)? ") # Pilihan operasi stok
    jumlah = int(input("Masukkan jumlah: ")) # Input jumlah perubahan stok
    if pilihan == "+": # Menambah stok 
        data[kode]["stok"] += jumlah # Menambahkan jumlah ke stok 
    elif pilihan == "-": # Mengurangi stok
        if data[kode]["stok"] - jumlah < 0: # Cek stok tidak negatif
            print("Stok tidak boleh negatif.") # Pesan error
        else:
            data[kode]["stok"] -= jumlah # Mengurangi jumlah dari stok
    print("Stok berhasil diperbarui.") # Konfirmasi pembaruan stok


# Menu utama
def main():
    nama_file = "barang.txt" # Nama file data
    data = baca_file(nama_file) # Membaca data dari file
# Menu loop
    while True:
        print("\n=== Menu Kantin ===") # Header menu
        print("1. Tampilkan semua barang") # Menu 1
        print("2. Cari barang berdasarkan kode") # Menu 2
        print("3. Tambah barang baru") # Menu 3
        print("4. Update stok barang") # Menu 4
        print("5. Simpan ke file") # Menu 5
        print("0. Keluar") # Menu 0

        pilihan = input("Pilih menu: ")
# Eksekusi pilihan
        if pilihan == "1": 
            tampilkan_semua(data) # Menampilkan semua barang
        elif pilihan == "2": # Mencari barang
            cari_barang(data) # Mencari barang berdasarkan kode
        elif pilihan == "3": # Menambah barang baru
            tambah_barang(data) # Menambah barang baru 
        elif pilihan == "4": # Update stok barang
            update_stok(data) # Update stok barang
        elif pilihan == "5": # Simpan ke file
            simpan_file(nama_file, data) # Menyimpan data ke file
        elif pilihan == "0": # Keluar dari program
            print("Program selesai.") # Pesan keluar
            break
        else:
            print("Pilihan tidak valid.")
# Akhir program
if __name__ == "__main__":
    main()