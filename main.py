# main.py
import os
import sys

# Mendapatkan direktori utama tempat file main.py berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from src.input_data import baca_data_file
from src.proses import hitung_statistik, tentukan_ketuntasan
from src.output import simpan_laporan_file

def main():
    print("=" * 50)
    print(" PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS 3B")
    print("=" * 50)

    # Jalur absolut aman dari error file tidak ditemukan
    path_input = os.path.join(BASE_DIR, "data", "contoh_data.txt")
    path_output = os.path.join(BASE_DIR, "output", "laporan_rekap.txt")

    print(f"Membaca data dari: {path_input} ...")
    data_siswa = baca_data_file(path_input)

    if not data_siswa:
        print("\n[ERROR] Tidak ada data nilai yang valid untuk diproses.")
        return

    # Proses Logika & Statistik
    statistik = hitung_statistik(data_siswa)
    ketuntasan = tentukan_ketuntasan(data_siswa, kkm=75.0)

    # Tampilkan di Terminal
    print("\n[HASIL RINGKASAN STATISTIK]")
    print(f"- Total Siswa Valid : {statistik['jumlah']}")
    print(f"- Rata-rata Nilai   : {statistik['rata_rata']:.2f}")
    print(f"- Nilai Terendah    : {statistik['minimum']}")
    print(f"- Nilai Tertinggi   : {statistik['maksimum']}")

    print("\n[STATUS KETUNTASAN (KKM 75)]")
    print(f"- Tuntas            : {ketuntasan['jumlah_tuntas']} siswa")
    print(f"- Belum Tuntas      : {ketuntasan['jumlah_belum_tuntas']} siswa")

    # Simpan ke File Output
    simpan_laporan_file(path_output, statistik, ketuntasan, kkm=75.0)
    print(f"\n[BERHASIL] Laporan berhasil disimpan ke '{path_output}'")
    print("=" * 50)

if __name__ == "__main__":
    main()