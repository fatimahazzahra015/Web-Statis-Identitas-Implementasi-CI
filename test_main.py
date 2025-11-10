import os

def test_html_file_exists():
    """Pastikan file index.html ada di direktori proyek"""
    assert os.path.exists("index.html"), "❌ File index.html tidak ditemukan"

def test_html_not_empty():
    """Pastikan file index.html tidak kosong"""
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read().strip()
    assert len(content) > 0, "❌ File index.html kosong"

def test_html_contains_name_and_nim():
    """Periksa apakah nama dan NIM mahasiswa ada di dalam index.html"""
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "Fatimah Azzahra" in content, "❌ Nama tidak ditemukan di index.html"
    assert "230411100015" in content, "❌ NIM tidak ditemukan di index.html"

