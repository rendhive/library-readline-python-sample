import readline

def save_history(filename):
    readline.write_history_file(filename)

def load_history(filename):
    readline.read_history_file(filename)

if __name__ == "__main__":
    load_history('history.txt')
    try:
        while True:
            input("Input something: ")
    except KeyboardInterrupt:
        save_history('history.txt')
# Fungsi: Menyimpan dan memuat sejarah input dari file.
# Kondisi: Ketika Anda ingin mempertahankan sejarah pengguna antara sesi.