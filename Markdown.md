# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Institut Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan berkualitas. Meskipun demikian, institusi ini menghadapi tantangan serius yaitu tingginya angka dropout mahasiswa, yang mengganggu reputasi akademik, efisiensi operasional, dan kualitas layanan pendidikan.

Berdasarkan data yang tersedia, dari total 3.630 mahasiswa, sekitar 39% di antaranya mengalami dropout. Angka ini tergolong cukup tinggi dan menunjukkan perlunya strategi pencegahan yang tepat.

Manajemen ingin mengetahui faktor-faktor yang berkontribusi terhadap dropout dan mengembangkan sistem berbasis data untuk mendeteksi mahasiswa berisiko agar dapat dilakukan intervensi lebih awal.

### Permasalahan Bisnis

1. Tingginya tingkat dropout mahasiswa (39%), yang berdampak negatif pada citra dan keberlanjutan institusi.

2. Kurangnya Visualisasi dashboard analitik yang mampu menyajikan visualisasi dari variabel-variabel seperti performa akademik, status keuangan, dan latar belakang pendidikan, untuk mengidentifikasi penyebab mahasiswa dropout.

3. Belum adanya sistem prediktif untuk mendeteksi mahasiswa yang berisiko dropout secara dini.

### Cakupan Proyek

1. Eksplorasi dan analisis data mahasiswa (EDA) untuk memahami karakteristik mahasiswa berdasarkan status (dropout dan graduated).

2. Visualisasi data berupa diagram untuk menggambarkan dropout berdasarkan variabel-variabel tersebut.

3. Pembuatan business dashboard menggunakan Metabase agar tim akademik dapat memonitor mahasiswa secara berkelanjutan.

4. Pengembangan model Machine Learning untuk memprediksi status mahasiswa berdasarkan data demografis dan akademik.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Platform dan Tools : 
1. Google Colab : Sebagai Platform utama untuk eksplorasi dan analisis data.
2. Metabase : Sebagai Platform BI (Business Intelligence) untuk membuat dashboard interaktif.
3. Supabase : Untuk menampung data hasil analisis yang akan digunakan dalam visualisasi di pada metabase.
4. Streamlit : Sebagai Library yang menampilkan hasil Sistem Machine Learning yang telah dibuat dalam bentuk seperti web.

Library : 
- pandas versi 2.2.3
- matplotlib versi 3.10.1
- seaborn versi 0.13.2
- sqlalchemy versi 2.0.36
- scikit-learn versi 1.6.1
- numpy versi 2.2.5
- joblib versi 1.4.2

Setup environment:

Agar proyek dapat dijalankan oleh orang lain tanpa hambatan, berikut adalah langkah-langkah setup environment secara lengkap dan sistematis:

1. Membuat dan Mengaktifkan Virtual Environment (venv): 

Jalankan perintah berikut di terminal:
```
python -m venv venv
```
Untuk pengguna Windows, aktifkan environment dengan perintah:
```
venv\\Scripts\\activate
```
2. Menginstal Dependensi dari requirements.txt:
Pastikan semua library terinstal dengan menjalankan perintah berikut:
```
pip install -r requirements.txt
```
3. Cara Menjalankan Skrip Python (.py)
File utama proyek ini adalah app.py. Untuk menjalankan aplikasi, gunakan perintah:
```
streamlit run app.py
```

## Business Dashboard
Link Dashboard: https://drive.google.com/file/d/1KU_JYbNmebpsb62w5CFEr12HqIIMI8ui/view?usp=drive_link

Login ke Metabase dengan URL : http://localhost:3000/setup
- Username : msyordan56@gmail.com
- Password : sultan134

Dalam dashboard yang telah dibuat, terdapat satu diagram untuk melihat persentase jumlah mahasiswa dropout dan graduate serta lima diagram yang masing-masing menggambarkan tingkat dropout berdasarkan variabel tertentu.

1. Dropout Ratio menampilkan persentase jumlah mahasiswa yang dropout dan graduate.
2. Dropout by Scholarship menampilkan perbandingan jumlah persentase mahasiswa dropout dengan perbandingan penerima beasiswa atau tidak.
3. Dropout by Marital Status menampilakn jumlah persentase perbandingan mahasiswa dropout berdasarkan status pernikahnnya.
4. Dropout by Course menampilkan jumlah persentase dropout pada tiap jurusan.
5. Dropout by Admission Grade menampilkan jumlah persentase dropout berdasarkan admission grade atau nilai ketika masuk kampus.
6. Dropout by Grade sem1 menampilkan jumlah persentase mahasiswa dropout berdasarakan nilai pada semester 1 yang telah dikategorikan ke dalam beberapa nilai.
7. Dropout by Grade sem2 menampilkan jumlah persentase mahasiswa dropout berdasarakan nilai pada semester 2 yang telah dikategorikan ke dalam beberapa nilai.



## Menjalankan Sistem Machine Learning

Model yang digunakan adalah decision tree denagn hasil akurasi 80% pada testing.

Langkah menjalankan sistem prediksi di streamlit website (Deploy):
1. Klik link berikut: https://student-gfopdyqgocfp9rcgnzj2ga.streamlit.app/
2. Lalu Masukkan beberapa input
3. Hasil prediksi akan keluar sesuai dengan inputan


## Conclusion

1. Melalui dashboard visual yang dibangun di Metabase, ditemukan beberapa variabel yang memiliki korelasi kuat terhadap kemungkinan mahasiswa untuk dropout, antara lain:
   
- Status beasiswa: Mahasiswa tanpa beasiswa cenderung memiliki tingkat dropout yang lebih tinggi.

- Status pernikahan: Mahasiswa yang berstatus legally separated atau menikah memiliki kecenderungan dropout yang tinggi.

- Jurusan Biofuel menunjukkan tingkat dropout lebih tinggi.

- Mahasiswa dengan Admission grade 90-120 cenderung memiliki tingkat dropout yang tinggi.

- Mahasiswa dengan nilai sem1 dan sem2 dalam rentang nilai 0-10 memiliki tingkat dropout yang tinggi.

2. Dashboard interaktif yang telah dibangun di Metabase memungkinkan tim akademik untuk secara mudah memantau dan menganalisis karakteristik mahasiswa yang berisiko tinggi mengalami dropout, sehingga dapat mendukung pengambilan keputusan berbasis data.

3. Sistem Prediktif Berbasis Machine Learning yang telah dikembangkan menunjukkan akurasi sebesar 80% pada data testing. Model ini diimplementasikan ke dalam aplikasi web menggunakan Streamlit, sehingga dapat digunakan secara praktis untuk memprediksi status mahasiswa (dropout atau graduate) berdasarkan input karakteristiknya.


### Rekomendasi Action Items

- Action Item 1: Intervensi Dini untuk Mahasiswa Berisiko Tinggi
Gunakan sistem prediksi berbasis machine learning yang telah dikembangkan untuk menyaring mahasiswa yang menunjukkan potensi dropout. Mahasiswa ini dapat menjadi prioritas untuk program bimbingan akademik, konseling, atau dukungan finansial.

- Action Item 2: Tinjau Kembali Kebijakan Beasiswa dan Dukungan Finansial
Mengingat bahwa mahasiswa tanpa beasiswa memiliki kecenderungan dropout yang lebih tinggi, pertimbangkan untuk memperluas akses terhadap program bantuan pendidikan atau beasiswa berbasis kebutuhan.

- Action Item 3: Penguatan Dukungan Akademik untuk Jurusan dan Nilai Masuk Rendah
Fokuskan program peningkatan kapasitas belajar (seperti mentoring, remedial, atau kelas tambahan) pada jurusan dan kelompok mahasiswa yang memiliki admission grade rendah serta nilai akademik yang buruk di semester awal.
