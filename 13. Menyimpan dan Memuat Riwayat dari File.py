import readline

def save_history_to_file(history_file):
    readline.write_history_file(history_file)
    print(f"Riwayat disimpan ke {history_file}.")

def load_history_from_file(history_file):
    readline.read_history_file(history_file)
    print(f"Riwayat dimuat dari {history_file}.")

if __name__ == "__main__":
    load_history_from_file('hist.txt')
    try:
        while True:
            input("Input sesuatu: ")
    except KeyboardInterrupt:
        save_history_to_file('hist.txt')