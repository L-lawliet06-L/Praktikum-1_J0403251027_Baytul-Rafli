#================================================================
# Praktikum 2 : ADT dan File Handling (Studi Kasus)
#================================================================

# Nama file yang digunakan untuk menyimpan data mahasiswa
nama_file = "mahasiswa.txt"

#---------------------------------------------------------------
# Latihan 1 : Membaca data mahasiswa dari file
#---------------------------------------------------------------
def baca_data_mahasiswa(nama_file):
    data_dict = {}  # inisialisasi dictionary kosong

    # buka file dalam mode baca
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # hilangkan newline
            nim, nama, nilai = baris.split(",")  # pecah data berdasarkan koma
            # simpan data ke dictionary dengan key = NIM
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai)
            }
    return data_dict


#---------------------------------------------------------------
# Latihan 2 : Menampilkan data mahasiswa
#---------------------------------------------------------------
def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("Data kosong")
        return

    # header tabel
    print("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32)

    # tampilkan data mahasiswa dengan urutan NIM
    for nim in sorted(data_dict):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")


#---------------------------------------------------------------
# Latihan 3 : Mencari data mahasiswa berdasarkan NIM
#---------------------------------------------------------------
def cari_data(data_dict):
    nim_cari = input("Masukkan NIM yang dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("\nData mahasiswa tidak ditemukan.")


#---------------------------------------------------------------
# Latihan 4 : Update nilai mahasiswa
#---------------------------------------------------------------
def update_nilai(data_dict):
    nim = input("Masukkan NIM Mahasiswa yang akan diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return

    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return

    # validasi nilai harus antara 0-100
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus di antara 0 sampai 100. Update dibatalkan")
        return

    # kalau valid, lakukan update
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")


#---------------------------------------------------------------
# Latihan 5 : Menyimpan data ke file
#---------------------------------------------------------------
def simpan_data(nama_file, data_dict):
    # buka file dalam mode tulis (write), menimpa isi lama
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
    print("Data berhasil disimpan ke file.")


#---------------------------------------------------------------
# Latihan 6 : Menu Program
#---------------------------------------------------------------
def main():
    # load data mahasiswa dari file
    buka_data = baca_data_mahasiswa(nama_file)

    # loop menu utama
    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan semua data")
        print("2. Cari data Mahasiswa NIM")
        print("3. Update nilai Mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilihan menu : ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


# eksekusi program utama
if __name__ == "__main__":
    main()