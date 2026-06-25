import readline

def handle_large_text_input(prompt):
    print(f"{prompt} (ketik 'exit' untuk keluar)")
    lines = []
    while True:
        line = input()
        if line.lower() == "exit":
            break
        lines.append(line)
    return ' '.join(lines)

if __name__ == "__main__":
    full_text = handle_large_text_input("Masukkan teks besar:")
    print("Teks yang dimasukkan:", full_text)
# Fungsi: Menangani input teks besar dari pengguna.
# Kondisi: Ketika Anda ingin memungkinkan pengguna menulis teks panjang di command line.