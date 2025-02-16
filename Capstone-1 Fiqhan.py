# Data awal siswa
data_siswa = {
    1: {"nama": "Andi", "nilai": 85},
    2: {"nama": "Budi", "nilai": 90},
    3: {"nama": "Cindy", "nilai": 78},
}
#function untuk validasi input huruf
def validasi_input_alfabet(prompt):
    while True:
        inputan = input(prompt)
        if inputan.isalpha():
            return inputan
        else:
            print('inputan harus huruf')
# function untuk validasi input angka
def validasi_input_angka(prompt):
    while True:
        inputan = input(prompt)
        if inputan.isdigit():
            return int(inputan)
        else:
            print('inputan harus angka')
#function untuk password            
PASSWORD_BENAR ='Admin'
def cek_password():
    percobaan = 3
    while percobaan > 0:
        password = input()
        if password == PASSWORD_BENAR:
            return True
        else:
            percobaan -= 1
            print(f"Password salah! Sisa percobaan: {percobaan}")
    print("Anda telah melebihi batas percobaan. Program keluar.")
    return False
# Fungsi untuk menampilkan data siswa
def tampilkan_data():
    print("\nData Siswa:")
    for id_siswa, info in data_siswa.items():
        print(f"ID: {id_siswa}, Nama: {info['nama']}, Nilai: {info['nilai']}")
# Fungsi untuk menambahkan data siswa baru
def tambah_data():
    nama = validasi_input_alfabet("Masukkan nama siswa: ")
    nilai = validasi_input_angka("Masukkan nilai siswa: ")
    id_baru = max(data_siswa.keys()) + 1 if data_siswa else 1  # Generate ID baru
    data_siswa[id_baru] = {"nama": nama, "nilai": nilai}
    print(f"Data siswa {nama} berhasil ditambahkan dengan ID {id_baru}!")
# Fungsi untuk update nilai siswa
def update_nilai():
    tampilkan_data()
    id_siswa = int(input("\nMasukkan ID siswa yang ingin diupdate: "))
    if id_siswa in data_siswa:
        nilai_baru = validasi_input_angka("Masukkan nilai baru: ")
        data_siswa[id_siswa]["nilai"] = nilai_baru
        print("Nilai berhasil diupdate!")
    else:
        print("ID siswa tidak ditemukan!")
# Fungsi untuk menghapus data siswa
def hapus_data():
    tampilkan_data()
    id_siswa = int(input("\nMasukkan ID siswa yang ingin dihapus: "))
    if id_siswa in data_siswa:
        nama_siswa = data_siswa[id_siswa]["nama"]
        del data_siswa[id_siswa]
        print(f"Data siswa {nama_siswa} berhasil dihapus!")
    else:
        print("ID siswa tidak ditemukan!")
# menu edit data
def edit():
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa Baru")
        print("2. update data siswa")
        print("3. Hapus Data")
        print("4. kembali")

        pilih = input("Pilih menu (1/2/3/4): ")
        if pilih == '1':
            tambah_data()
        elif pilih == '2':
            update_nilai()     
        elif pilih == '3':
            hapus_data()
        elif pilih == '4':    
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
# Menu utama
while True:
    print("\nMenu:")
    print("1. Tampilkan Data Siswa")
    print("2. Edit Data Siswa")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        print("masukkan password: ")
        if cek_password():
            edit()
        else:
            print("Akses ditolak")
    elif pilihan == "3":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")