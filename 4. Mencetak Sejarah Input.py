import readline

readline.add_history("Input Pertama")
readline.add_history("Input Kedua")

for i in range(readline.get_current_history_length()):
    print(readline.get_history_item(i + 1))  # History items are indexed from 1
# Fungsi: Menampilkan semua input yang telah dicatat dalam sejarah.
# Kondisi: Ketika Anda ingin memberikan kepada pengguna akses ke semua input sebelumnya.