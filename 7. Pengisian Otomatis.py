import readline

def completer(text, state):
    options = [s for s in ['apple', 'banana', 'pear'] if s.startswith(text)]
    return options[state]

readline.set_completer(completer)
readline.parse_and_bind('tab: complete')  # Mengatur tombol tab untuk menyelesaikan
input("Coba ketik buah: ")
# Fungsi: Menambahkan fungsionalitas autocompletion menggunakan tombol Tab.
# Kondisi: Ketika Anda ingin meningkatkan UX input baris perintah.