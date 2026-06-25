import readline

readline.add_history("Input 1")
readline.add_history("Input 2")
print("Sebelum penghapusan:", readline.get_current_history_length())

readline.clear_history()  # Menghilangkan semua item dalam sejarah
print("Setelah penghapusan:", readline.get_current_history_length())
# Fungsi: Menghapus semua entri dalam sejarah input.
# Kondisi: Ketika Anda ingin membuat aplikasi yang tidak menyimpan input sebelumnya.