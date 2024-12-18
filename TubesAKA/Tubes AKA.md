# <h1 align="center">Laporan Tugas Besar Analisis Kompleksitas Algoritma</h1>
<p align="center">
    Adam Nur Cahya Putra (2311102118)
- Nandana Tsany Farrel Arkananta (2311102143)
</p>


## Poster

![Salinan dari Poster Tugas Besar Analisis Kompleksitas Algoritma](https://github.com/user-attachments/assets/93cade61-78fa-4097-b9f7-ccf2d563b948)


## Dasar Teori
Algoritma yang mengelola antrian pelanggan di kasir dengan memilih kasir yang paling efisien berdasarkan kecepatan dan jumlah barang yang dibeli oleh pelanggan. Setiap kasir memiliki estimasi waktu total yang dihitung berdasarkan kecepatan dan jumlah barang pelanggan dalam antrian. Proses ini bertujuan mengurangi kemacetan dan memastikan pelanggan dilayani dengan efisien, sehingga meningkatkan kepuasan pelanggan dengan waktu tunggu yang lebih singkat.

## Source Code 

### Mengoptimalkan waktu tunggu di supermarket

```Python
from queue import Queue

# Kelas untuk mengelola informasi kasir
class Kasir:
    def __init__(self, id_kasir, kecepatan):
        self.id = id_kasir
        self.kecepatan = kecepatan  # Waktu per barang (detik)
        self.antrian = Queue()

    def estimasi_waktu_total(self):
        # Hitung total waktu estimasi untuk semua pelanggan di antrian
        return sum(p.jumlah_barang * self.kecepatan for p in list(self.antrian.queue))

# Kelas untuk mengelola informasi pelanggan
class Pelanggan:
    def __init__(self, id_pelanggan, jumlah_barang):
        self.id = id_pelanggan
        self.jumlah_barang = jumlah_barang

def pilih_kasir_terbaik(kasir_list, pelanggan):
    # Pilih kasir dengan estimasi waktu total paling kecil setelah menambahkan pelanggan
    return min(kasir_list, key=lambda k: k.estimasi_waktu_total() + pelanggan.jumlah_barang * k.kecepatan)

def tambahkan_pelanggan_ke_kasir(kasir_list, pelanggan):
    kasir_terbaik = pilih_kasir_terbaik(kasir_list, pelanggan)
    kasir_terbaik.antrian.put(pelanggan)
    print(f"{pelanggan.id} ditempatkan ke {kasir_terbaik.id}")

def main():
    # Inisialisasi daftar kasir
    kasir_list = [
        Kasir("Kasir 1", kecepatan=3),  # 3 detik per barang
        Kasir("Kasir 2", kecepatan=2),  # 2 detik per barang
        Kasir("Kasir 3", kecepatan=1),  # 1 detik per barang
    ]

    # Inisialisasi daftar pelanggan
    pelanggan_list = [
        Pelanggan("Pelanggan 1", jumlah_barang=5),
        Pelanggan("Pelanggan 2", jumlah_barang=10),
        Pelanggan("Pelanggan 3", jumlah_barang=2),
    ]

    # Proses setiap pelanggan
    for pelanggan in pelanggan_list:
        tambahkan_pelanggan_ke_kasir(kasir_list, pelanggan)

    # Tampilkan hasil akhir
    print("\nStatus Antrian Akhir:")
    for kasir in kasir_list:
        print(f"{kasir.id} memiliki {kasir.antrian.qsize()} pelanggan.")

# Menjalankan program
if __name__ == "__main__":
    main()

```

#### Output:
![image](https://github.com/user-attachments/assets/1d3817a1-a917-4bbe-b77e-7ab68a81bab3)

## Kesimpulan
Pada program pengurutan kasir di supermarket menggunakan 2 algoritma queue dan bubble sort yang Bertujuan untuk mengelola antrian kasir dengan cara menempatkan pelanggan ke kasir yang memberikan estimasi waktu paling efisien berdasarkan dan kecepatan kasir. Program ini berhasil mengelola distribusi antrian pelanggan ke kasir secara optimal. Berdasarkan distribusi pelanggan dan estimasi waktu pada tabel, pelanggan ditempatkan ke kasir dengan mempertimbangkan efisiensi waktu pelayanan, menunjukkan bahwa metode iteratif dan rekursif memberikan hasil yang konsisten dan dapat digunakan secara bergantian.
