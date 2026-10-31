# Program Rekap dan Analisis Nilai Matematika Kelas

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Deskripsi
Guru matematika membutuhkan program sederhana untuk membaca data nilai dari file teks, melakukan validasi, menghitung statistik kelas, menentukan status ketuntasan, dan menyimpan laporan ringkas secara otomatis.

## Fitur
- Membaca file data nilai dari `data/contoh_data.txt`
- Memvalidasi rentang nilai (0 - 100)
- Menghitung rata-rata, nilai minimum, dan nilai maksimum
- Menentukan status tuntas atau belum tuntas berdasarkan KKM
- Menyimpan hasil laporan ke file teks

## Persyaratan
- Python 3.x

## Cara Menjalankan
python main.py

## Struktur Folder
- `main.py`: File utama pengatur alur program
- `src/input_data.py`: Modul untuk membaca file dan validasi nilai
- `src/proses.py`: Modul untuk perhitungan statistik dan ketuntasan
- `src/output.py`: Modul untuk mencetak hasil ke file laporan
- `data/contoh_data.txt`: File masukan data mentah
- `tests/test_case.md`: Dokumen pengujian dan bug log

## Test Case
| ID | Fitur | Input | Expected | Actual | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC01 | Rata-rata | [85, 78, 60] | Rata-rata 74.33 | Rata-rata 74.33 | PASS |
| TC02 | Batas Bawah | Nilai: 0 | Valid | Valid | PASS |
| TC03 | Batas Atas | Nilai: 100 | Valid | Valid | PASS |
| TC04 | Invalid | Nilai: 105 | Ditolak | Ditolak | PASS |

## Known Issues
- Pastikan format file teks masukan menggunakan pemisah koma (Nama,Nilai) agar tidak terjadi kesalahan baca data.

## Referensi/Bantuan
- Modul Bahan Ajar Algoritma dan Pemrograman Pertemuan 14 & 15 Universitas Sultan Ageng Tirtayasa (Untirta).