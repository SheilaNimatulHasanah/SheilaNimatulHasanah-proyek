import os

def validasi_nilai(nilai):
    """Memvalidasi rentang nilai valid (0-100)."""
    try:
        val = float(nilai)
        return 0 <= val <= 100
    except ValueError:
        return False

def baca_data_file(path_file):
    """Membaca data dari file teks dengan format 'Nama,Nilai'."""
    if not os.path.exists(path_file):
        print(f"[ERROR] File tidak ditemukan di path: {path_file}")
        return []

    data_valid = []
    with open(path_file, mode="r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue
            
            bagian = baris.split(",")
            if len(bagian) == 2:
                nama = bagian[0].strip()
                nilai_str = bagian[1].strip()
                
                if validasi_nilai(nilai_str):
                    data_valid.append({
                        "nama": nama,
                        "nilai": float(nilai_str)
                    })
                else:
                    print(f"[PERINGATAN] Data diabaikan (invalid): {baris}")
                    
    return data_valid