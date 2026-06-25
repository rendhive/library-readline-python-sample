import readline

try:
    while True:
        line = input("Input (Ctrl+C to exit): ")
        readline.add_history(line)
except KeyboardInterrupt:
    print("\nKeluar dari program.")
# Fungsi: Menghentikan input saat pengguna menekan Ctrl+C.
# Kondisi: Ketika Anda ingin memberikan pengguna kontrol untuk keluar dari program interaktif.