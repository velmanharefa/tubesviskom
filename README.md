# Fruits Ripeness or Rottenness Detection Using YOLOv11

## Penulis
- **Nama:** Velman Noeli Harefa  
  **NIM:** 1301213264  
- **Nama:** Benaya Obed Sinaga  
  **NIM:** 1301213178  

## Deskripsi Proyek
Proyek ini bertujuan untuk mendeteksi dan mengklasifikasikan buah-buahan ke dalam delapan kategori berdasarkan kondisi **baik** (good) dan **buruk** (bad). Model yang digunakan adalah **YOLOv11**, yang diterapkan dalam sebuah aplikasi berbasis web menggunakan **Streamlit** untuk mendukung proses penilaian kualitas otomatis dan penyortiran dalam sektor agrikultur dan ritel.

## Dataset
Dataset terdiri dari 4,399 gambar dengan proporsi:
- **70%** untuk data pelatihan (training)
- **20%** untuk data validasi (validation)
- **10%** untuk data pengujian (testing)

Dataset mencakup 8 kategori:
1. Apel (baik dan buruk)
2. Pisang (baik dan buruk)
3. Jeruk (baik dan buruk)
4. Delima (baik dan buruk)

## Model dan Eksperimen
Model YOLOv11 dilatih menggunakan **SGD optimizer** dengan konfigurasi hyperparameter sebagai berikut:
- **Learning Rate (lr0):** 0.01
- **Momentum:** 0.9
- **Weight Decay:** 0.0005
- **Image Size:** 640x640 piksel

### Epoch yang Digunakan
Model diuji pada tiga jumlah epoch:
1. **50 epochs:** Memberikan hasil awal dengan presisi dan recall di atas 0.98.
2. **100 epochs:** Menunjukkan keseimbangan terbaik antara akurasi dan efisiensi dengan:
   - Precision: **0.988**
   - Recall: **0.993**
   - mAP50: **0.993**
3. **150 epochs:** Memberikan performa tinggi dengan peningkatan kecil pada mAP50:95.

## Implementasi
Model ini diimplementasikan dalam aplikasi berbasis web yang memungkinkan pengguna untuk mengunggah gambar buah dan mendapatkan hasil deteksi secara real-time, termasuk:
- Bounding box
- Label kategori
- Tingkat kepercayaan prediksi

Aplikasi ini dirancang untuk mempermudah penyortiran dan evaluasi kualitas buah di industri agrikultur dan ritel.

## Teknologi yang Digunakan
- **Framework Model:** YOLOv11
- **Framework Aplikasi:** Streamlit
- **Bahasa Pemrograman:** Python
