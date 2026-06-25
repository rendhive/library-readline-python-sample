import readline

def get_multiline_input():
    lines = []
    while True:
        line = input("Masukkan kalimat (atau 'selesai' untuk mengakhiri): ")
        if line == "selesai":
            break
        lines.append(line)
    return lines

user_input = get_multiline_input()
print("Input yang diterima:", user_input)
# Fungsi: Menerima input beberapa baris dari pengguna.
# Kondisi: Ketika Anda ingin pengguna dapat membuat input yang lebih panjang dan terpisah.