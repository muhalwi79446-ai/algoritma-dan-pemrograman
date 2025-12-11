# dictionary.py

# Membuat dictionary
mahasiswa = {
    "nama": "Alwi",
    "nim": "D0425007",
    "jurusan": "sistem Informasi",
    "nilai": 95
}

# Menampilkan dictionary
print("Data Mahasiswa:")
print(mahasiswa)

# Mengakses nilai berdasarkan key
print("\nNama:", mahasiswa["nama"])
print("NIM :", mahasiswa["nim"])

# Menambah key dan value baru
mahasiswa["angkatan"] = 2023
print("\nSetelah menambah angkatan:")
print(mahasiswa)

# Mengubah value di dictionary
mahasiswa["nilai"] = 95
print("\nSetelah mengubah nilai:")
print(mahasiswa)

# Menghapus salah satu data
del mahasiswa["jurusan"]
print("\nSetelah menghapus jurusan:")
print(mahasiswa)

# Menggunakan loop untuk menampilkan isi dictionary
print("\nMenampilkan semua key dan value:")
for key, value in mahasiswa.items():
    print(f"{key} : {value}")

# Mengecek apakah key ada dalam dictionary
if "nama" in mahasiswa:
    print("\nKey 'nama' ditemukan!")

# Mendapatkan semua key
print("\nSemua key:", list(mahasiswa.keys()))

# Mendapatkan semua value
print("Semua value:", list(mahasiswa.values()))

