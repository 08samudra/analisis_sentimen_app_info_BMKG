# Analisis Sentimen Aplikasi Info BMKG

Proyek ini melakukan analisis sentimen terhadap ulasan pengguna aplikasi **Info BMKG** yang diambil dari Google Play Store. Sentimen dikategorikan menjadi tiga kelas: `positif`, `netral`, dan `negatif`.

### 🚀 Instalasi dan Setup Proyek
```

### 1. Clone Repository
```bash
git clone https://github.com/08samudra/analisis_sentimen_app_info_BMKG.git
cd analisis_sentimen_app_info_BMKG
```

### 2. Setup Virtual Environment (Windows/macOS)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Jalankan File Scraper

Untuk mendapatkan dataset ulasan aplikasi Info BMKG:

```bash
python scraping_playstore.py
```

### 5. Jalankan Notebook

Buka `model_training.ipynb` di VS Code atau Jupyter Notebook, kemudian jalankan sel untuk:

* Eksplorasi dan visualisasi data
* Pelatihan model dan visualisasi (Logistic Regression, SVM, dan Random Forest)

## 📊 Hasil Evaluasi Model

Model pelatihan dilakukan dengan pembagian data `train:test = 80:20` dan `70:30`. Hasil evaluasi tiga model terbaik:

| Model               | Akurasi |
| ------------------- | ------- |
| Logistic Regression | 0.99    |
| SVM (LinearSVC)     | 0.986   |
| Random Forest       | 0.98    |

## 📌 Output Inferensi

Inferensi dilakukan dengan memberikan input review baru dan menghasilkan kelas sentimen (positif, netral, negatif). Contoh output tersedia di dalam notebook `model_training.ipynb`.

````