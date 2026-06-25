import readline

readline.set_history_length(5)  # Maksimal 5 sejarah
for i in range(10):
    readline.add_history(f"Input {i + 1}")

print(f"Panjang sejarah saat ini: {readline.get_current_history_length()}")
# Fungsi: Mengatur batas panjang berapa banyak entri sejarah yang disimpan.
# Kondisi: Ketika Anda ingin membatasi berapa lama sejarah input yang disimpan.