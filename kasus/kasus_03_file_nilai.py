def baca_dan_hitung(nama_file):
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            data = []
            for baris in file:
                baris = baris.strip()
                if baris:
                    try:
                        data.append(float(baris))
                    except ValueError:
                        continue
            if not data:
                return 0
            return sum(data) / len(data)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return None

print(baca_dan_hitung("data_contoh.txt"))