# Dokumen Pengujian Proyek (Test Case & Bug Log)

## Tabel Hasil Pengujian (Test Case)
| ID | Fitur / Kategori | Input | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC01 | Rata-rata (Normal) | [85, 78, 60] | Rata-rata: 74.33, Min: 60, Max: 85 | Rata-rata: 74.33, Min: 60.0, Max: 85.0 | PASS |
| TC02 | Batas Bawah | Nilai: 0 | Diterima sebagai nilai valid | Nilai 0.0 diproses sebagai valid | PASS |
| TC03 | Batas Atas | Nilai: 100 | Diterima sebagai nilai valid | Nilai 100.0 diproses sebagai valid | PASS |
| TC04 | Invalid | Nilai: 105 atau -5 | Ditolak dengan peringatan validasi | Pesan peringatan muncul, data diabaikan | PASS |
| TC05 | File Handling | File tidak ada | Ditangani tanpa program crash | Pesan error file tidak ditemukan muncul | PASS |
| TC06 | Ketuntasan | Nilai: [85, 78, 60] KKM 75 | Tuntas: 2, Belum Tuntas: 1 | Tuntas: 2, Belum Tuntas: 1 | PASS |

## Bug Log
| ID Bug | Gejala Masalah | Penyebab | Perbaikan Kode | Status |
| :--- | :--- | :--- | :--- | :--- |
| BUG-01 | ZeroDivisionError saat data kosong | Pembagian dengan len(data) = 0 | Menambahkan pengecekan kondisi list kosong pada modul proses.py | Closed |
| BUG-02 | Program error saat membaca huruf ("abc") | Fungsi float() gagal konversi teks | Membungkus konversi dengan blok try-except pada input_data.py | Closed |