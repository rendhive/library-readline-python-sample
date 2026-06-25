import readline

def save_client_data(client_name):
    readline.add_history(client_name)
    print(f"Data klien '{client_name}' disimpan.")

if __name__ == "__main__":
    save_client_data("Klien A")
# Fungsi: Menyimpan data klien ke dalam riwayat untuk digunakan di masa mendatang.
# Kondisi: Ketika Anda perlu mencatat interaksi tertentu dengan klien.