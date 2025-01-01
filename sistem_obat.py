class Pasien:
    def __init__(self, nama, gejala):
        self.nama = nama
        self.gejala = gejala

class PenetapanObat:
    def __init__(self):
        self.obat_rekomendasi = {
            "demam": "Paracetamol",
            "batuk": "Bisolvon",
            "flu": "Panadol"
        }

    def rekomendasi_obat(self, pasien):
        obat = []
        for gejala in pasien.gejala:
            if gejala in self.obat_rekomendasi:
                obat.append(self.obat_rekomendasi[gejala])
        return obat

def main():
    print("Sistem Penetapan Obat untuk Pasien")
    nama = input("Masukkan Nama Pasien: ")
    gejala_input = input("Masukkan gejala pasien (pisahkan dengan koma, misal: demam, batuk, flu): ")
    gejala = [g.strip() for g in gejala_input.split(",")]

    pasien = Pasien(nama, gejala)
    penetapan_obat = PenetapanObat()

    obat = penetapan_obat.rekomendasi_obat(pasien)

    if obat:
        print(f"\nRekomendasi obat untuk {pasien.nama}:")
        for o in obat:
            print(f"- {o}")
    else:
        print(f"Tidak ada rekomendasi obat untuk gejala yang dimasukkan.")

if __name__ == "__main__":
    main()