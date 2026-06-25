import readline

readline.add_history("Masukan 1")  # Menambahkan input ke sejarah
readline.add_history("Masukan 2")

history_length = readline.get_current_history_length()
print(f"Jumlah input dalam sejarah: {history_length}")
# Fungsi: Mengambil jumlah total input yang telah disimpan dalam sejarah.
# Kondisi: Ketika Anda ingin melacak berapa banyak entri yang telah disimpan.