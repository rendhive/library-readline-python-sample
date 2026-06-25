import readline

def set_interactive_mode(mode):
    readline.set_startup_hook(lambda: print(f"Mode interaktif: {mode}"))
    
if __name__ == "__main__":
    set_interactive_mode("Testing")
    input("Tekan enter untuk melanjutkan...")
# Fungsi: Mengubah pengaturan untuk menampilkan mode interaktif saat memulai.
# Kondisi: Ketika Anda ingin memberikan informasi langsung kepada pengguna saat memulai aplikasi.