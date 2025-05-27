from google_play_scraper import reviews, Sort
import pandas as pd

# Ganti ini dengan ID aplikasi Info BMKG
app_id = 'com.Info_BMKG'

# Ambil 3000 review (maks 200 per panggilan, jadi pakai loop)
all_reviews = []
count = 0
batch_size = 200

while count < 3000:
    rvws, _ = reviews(
        app_id,
        lang='id',
        country='id',
        sort=Sort.NEWEST,
        count=batch_size,
        filter_score_with=None
    )
    all_reviews.extend(rvws)
    count = len(all_reviews)
    print(f"Total reviews terkumpul: {count}")

    # Hentikan jika review sudah tidak bertambah
    if len(rvws) < batch_size:
        break

# Konversi ke DataFrame
df = pd.DataFrame(all_reviews)

# Ambil kolom yang penting saja
df = df[['userName', 'score', 'content', 'at']]

# Simpan ke CSV
df.to_csv('dataset/reviews.csv', index=False, encoding='utf-8-sig')

print("✅ Scraping selesai. Data disimpan di dataset/reviews.csv")
