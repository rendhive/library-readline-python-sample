import readline

def categorize_input_prompt():
    category = input("Masukkan kategori (work/home): ")
    readline.add_history(category)
    # Anda dapat menambah logika lebih jauh untuk menyimpan kategori ini ke dalam struktur data
    print(f"Kategori '{category}' telah disimpan dalam riwayat.")

if __name__ == "__main__":
    categorize_input_prompt()
# Fungsi: Mengelola dan menyimpan kategori input untuk pemrosesan di masa mendatang.
# Kondisi: Ketika Anda ingin pengguna dapat mengelompokkan input berdasarkan kategori tertentu.