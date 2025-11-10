# Web Identitas Mahasiswa (Contoh)

Projek ini berisi halaman statis `index.html` yang menampilkan identitas mahasiswa
dan sebuah workflow GitHub Actions untuk menjalankan pengujian otomatis (pytest).

## File penting
- `index.html` : Halaman web statis
- `test_main.py` : Tes pytest sederhana untuk memeriksa keberadaan file dan isinya
- `.github/workflows/ci.yml` : Konfigurasi GitHub Actions

## Cara pakai (local)
1. Clone atau unduh repositori.
2. Pastikan Python terinstal, lalu install pytest: `pip install pytest`
3. Jalankan `pytest` di root folder (akan mendeteksi `test_main.py`).

## Cara pakai (GitHub)
1. Buat repository baru di GitHub (public).
2. Upload semua file ke branch `main`.
3. Buka tab **Actions** untuk melihat workflow berjalan otomatis setelah push.
