# src/output.py
import os

def simpan_laporan_file(path_output, statistik, ketuntasan, kkm=75.0):
    """Menuliskan hasil laporan ringkas ke dalam file teks di folder output."""
    os.makedirs(os.path.dirname(path_output), exist_ok=True)
    
    with open(path_output, mode="w", encoding="utf-8") as file:
        file.write("==================================================\n")
        file.write("       LAPORAN REKAP & ANALISIS NILAI KELAS       \n")
        file.write("==================================================\n\n")
        
        file.write("--- RINGKASAN STATISTIK ---\n")
        file.write(f"Total Siswa Valid  : {statistik['jumlah']}\n")
        file.write(f"Nilai Rata-rata    : {statistik['rata_rata']:.2f}\n")
        file.write(f"Nilai Minimum      : {statistik['minimum']}\n")
        file.write(f"Nilai Maksimum     : {statistik['maksimum']}\n\n")
        
        file.write(f"--- STATUS KETUNTASAN (KKM = {kkm}) ---\n")
        file.write(f"Jumlah Tuntas       : {ketuntasan['jumlah_tuntas']}\n")
        file.write(f"Jumlah Belum Tuntas : {ketuntasan['jumlah_belum_tuntas']}\n\n")
        
        file.write("--- DETAIL DAFTAR NILAI SISWA ---\n")
        file.write(f"{'No.':<4} {'Nama Siswa':<20} {'Nilai':<10} {'Status':<15}\n")
        file.write("-" * 50 + "\n")
        
        for idx, item in enumerate(ketuntasan["detail"], start=1):
            file.write(f"{idx:<4} {item['nama']:<20} {item['nilai']:<10.1f} {item['status']:<15}\n")
            
        file.write("\n==================================================\n")