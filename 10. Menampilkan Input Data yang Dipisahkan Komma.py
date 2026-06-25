import readline

def get_csv_input(prompt):
    line = input(prompt)
    return line.split(',')

csv_data = get_csv_input("Masukkan data (pisahkan dengan koma): ")
print("Data yang dimasukkan:", csv_data)
# Fungsi: Menerima dan memisahkan input dengan koma untuk pemrosesan lebih lanjut.
# Kondisi: Ketika Anda ingin memudahkan pengguna untuk memasukkan data daftar.