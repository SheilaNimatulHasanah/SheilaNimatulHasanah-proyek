# src/proses.py

def hitung_rata_rata(nilai_list):
    """Mengembalikan rata-rata list numerik (mencegah ZeroDivisionError)."""
    if not nilai_list:
        return 0.0
    return sum(nilai_list) / len(nilai_list)

def hitung_statistik(data_siswa):
    """Menghitung ringkasan statistik kelas: jumlah, rata-rata, min, dan max."""
    if not data_siswa:
        return {
            "jumlah": 0,
            "rata_rata": 0.0,
            "minimum": None,
            "maksimum": None
        }
    
    nilai_list = [siswa["nilai"] for siswa in data_siswa]
    return {
        "jumlah": len(nilai_list),
        "rata_rata": hitung_rata_rata(nilai_list),
        "minimum": min(nilai_list),
        "maksimum": max(nilai_list)
    }

def tentukan_ketuntasan(data_siswa, kkm=75.0):
    """Menentukan status tuntas atau belum tuntas berdasarkan KKM."""
    hasil_ketuntasan = []
    jumlah_tuntas = 0
    jumlah_belum = 0

    for siswa in data_siswa:
        status = "Tuntas" if siswa["nilai"] >= kkm else "Belum Tuntas"
        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_belum += 1
            
        hasil_ketuntasan.append({
            "nama": siswa["nama"],
            "nilai": siswa["nilai"],
            "status": status
        })
        
    return {
        "detail": hasil_ketuntasan,
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum
    }