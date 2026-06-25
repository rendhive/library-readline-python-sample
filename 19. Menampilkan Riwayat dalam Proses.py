import readline

def display_history():
    history_count = readline.get_current_history_length()
    print("Riwayat input:")
    for i in range(history_count):
        print(f"{i + 1}: {readline.get_history_item(i + 1)}")

if __name__ == "__main__":
    display_history()
# Fungsi: Menampilkan riwayat input secara langsung di terminal.
# Kondisi: Ketika Anda ingin memberikan pengguna akses ke riwayat input tanpa memasukkan perintah tambahan.