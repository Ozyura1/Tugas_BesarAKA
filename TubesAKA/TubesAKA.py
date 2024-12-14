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
