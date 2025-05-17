nilai_mahasiswa = {
    "Andi": 85,
    "Budi": 70,
    "Citra": 90,
    "Dina": 40,
    "Eka": 75,
    "Fajar": 40
}

def cari_nilai_minimum(data):
    return min(data.values())

def cari_pemilik_nilai_minimum(data, nilai_min):
    return [nama for nama, nilai in data.items() if nilai == nilai_min]

def tampilkan_hasil(nilai_min, pemilik):
    print("="*40)
    print(f"Nilai minimum dari dictionary adalah: {nilai_min}")
    print("Dimiliki oleh:")
    for nama in pemilik:
        print(f"- {nama}")
    print("="*40)

def main():
    nilai_min = cari_nilai_minimum(nilai_mahasiswa)
    pemilik = cari_pemilik_nilai_minimum(nilai_mahasiswa, nilai_min)
    tampilkan_hasil(nilai_min, pemilik)

main()
