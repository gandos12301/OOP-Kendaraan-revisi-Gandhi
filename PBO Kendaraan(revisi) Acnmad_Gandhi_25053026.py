

# CLASS INDUK 
class Kendaraan:
    def __init__(self, merk, tahun, warna):
        self.merk  = merk
        self.tahun = tahun
        self.warna = warna

    def tampil_spesifikasi(self):
        print(f"  Merk  : {self.merk}")
        print(f"  Tahun : {self.tahun}")
        print(f"  Warna : {self.warna}")


# ─────────────── CLASS TURUNAN ───────────────
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, warna, jumlah_pintu):
        super().__init__(merk, tahun, warna)
        self.jumlah_pintu = jumlah_pintu

    def tampil_spesifikasi(self):          # override
        print(f"  [MOBIL]")
        super().tampil_spesifikasi()
        print(f"  Pintu : {self.jumlah_pintu}")


class Motor(Kendaraan):
    def __init__(self, merk, tahun, warna, jenis_motor):
        super().__init__(merk, tahun, warna)
        self.jenis_motor = jenis_motor

    def tampil_spesifikasi(self):          # override
        print(f"  [MOTOR]")
        super().tampil_spesifikasi()
        print(f"  Jenis : {self.jenis_motor}")


class Bus(Kendaraan):
    def __init__(self, merk, tahun, warna, kapasitas_penumpang):
        super().__init__(merk, tahun, warna)
        self.kapasitas_penumpang = kapasitas_penumpang

    def tampil_spesifikasi(self):          # override
        print(f"  [BUS]")
        super().tampil_spesifikasi()
        print(f"  Kapasitas: {self.kapasitas_penumpang} penumpang")


# ─────────────── FUNGSI UTILITAS ───────────────
GARIS = "=" * 45

def cetak_header(judul):
    print(f"\n{GARIS}")
    print(f"  {judul}")
    print(GARIS)

def tampilkan_semua(daftar):
    cetak_header("SEMUA KENDARAAN")
    if not daftar:
        print("  (Belum ada data kendaraan.)")
        return
    for i, k in enumerate(daftar, 1):
        print(f"\n  --- Data #{i} ---")
        k.tampil_spesifikasi()

def cari_merk(daftar):
    cetak_header("CARI KENDARAAN")
    kata = input("  Masukkan merk yang dicari : ").strip()
    hasil = [k for k in daftar if kata.lower() in k.merk.lower()]
    if not hasil:
        print(f"  Tidak ditemukan kendaraan dengan merk '{kata}'.")
    else:
        print(f"\n  Ditemukan {len(hasil)} kendaraan:\n")
        for i, k in enumerate(hasil, 1):
            print(f"  --- Hasil #{i} ---")
            k.tampil_spesifikasi()

def urutkan_tahun(daftar):
    cetak_header("URUTKAN BERDASARKAN TAHUN TERBARU")
    if not daftar:
        print("  (Belum ada data kendaraan.)")
        return
    terurut = sorted(daftar, key=lambda k: k.tahun, reverse=True)
    for i, k in enumerate(terurut, 1):
        print(f"\n  --- #{i} ---")
        k.tampil_spesifikasi()

def input_int(prompt, min_val=None, max_val=None):
    """Input integer dengan validasi."""
    while True:
        try:
            nilai = int(input(prompt).strip())
            if min_val is not None and nilai < min_val:
                print(f"  [!] Nilai minimal {min_val}.")
                continue
            if max_val is not None and nilai > max_val:
                print(f"  [!] Nilai maksimal {max_val}.")
                continue
            return nilai
        except ValueError:
            print("  [!] Masukkan angka yang valid.")

def input_str(prompt):
    """Input string non-kosong."""
    while True:
        nilai = input(prompt).strip()
        if nilai:
            return nilai
        print("  [!] Input tidak boleh kosong.")

def tambah_kendaraan(daftar):
    cetak_header("TAMBAH KENDARAAN")
    print("  Pilih jenis kendaraan:")
    print("  1. Mobil")
    print("  2. Motor")
    print("  3. Bus")
    jenis = input_int("  Pilihan (1-3) : ", 1, 3)

    merk  = input_str("  Merk          : ")
    tahun = input_int("  Tahun         : ", 1900, 2026)
    warna = input_str("  Warna         : ")

    if jenis == 1:
        pintu = input_int("  Jumlah Pintu  : ", 1, 10)
        daftar.append(Mobil(merk, tahun, warna, pintu))
    elif jenis == 2:
        jenis_motor = input_str("  Jenis Motor   : ")
        daftar.append(Motor(merk, tahun, warna, jenis_motor))
    else:
        kapasitas = input_int("  Kapasitas Penumpang : ", 1, 200)
        daftar.append(Bus(merk, tahun, warna, kapasitas))

    print("  [✓] Kendaraan berhasil ditambahkan!")


# ─────────────── DATA AWAL (8 OBJEK) ───────────────
def init_data():
    return [
        Mobil ("Toyota",   2022, "Putih",  4),
        Mobil ("Honda",    2020, "Hitam",  2),
        Mobil ("BMW",      2023, "Silver", 4),
        Motor ("Yamaha",   2021, "Biru",   "Sport"),
        Motor ("Honda",    2019, "Merah",  "Matic"),
        Motor ("Kawasaki", 2023, "Hijau",  "Naked"),
        Bus   ("Hino",     2018, "Orange", 40),
        Bus   ("Mercedes", 2022, "Putih",  60),
    ]


# ─────────────── MENU UTAMA ───────────────
def menu():
    daftar_kendaraan = init_data()

    while True:
        cetak_header("SISTEM MANAJEMEN KENDARAAN")
        print("  1. Tambah Kendaraan")
        print("  2. Cari Kendaraan berdasarkan Merk")
        print("  3. Tampilkan Semua Kendaraan")
        print("  4. Urutkan berdasarkan Tahun Terbaru")
        print("  0. Keluar")
        print(GARIS)

        pilihan = input("  Pilih menu : ").strip()

        if pilihan == "1":
            tambah_kendaraan(daftar_kendaraan)
        elif pilihan == "2":
            cari_merk(daftar_kendaraan)
        elif pilihan == "3":
            tampilkan_semua(daftar_kendaraan)
        elif pilihan == "4":
            urutkan_tahun(daftar_kendaraan)
        elif pilihan == "0":
            print("\n  Terima kasih! Program selesai.\n")
            break
        else:
            print("  [!] Pilihan tidak valid. Coba lagi.")

        input("\n  Tekan Enter untuk lanjut...")


# ─────────────── ENTRY POINT ───────────────
if __name__ == "__main__":
    menu()
