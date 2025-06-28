#  Proyek Data Science: Analitik Prediktif untuk Deteksi Dini Mahasiswa Berpotensi Putus Kuliah di Jaya Jaya Institut

## 🏢 Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias *dropout*.

Jumlah *dropout* yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan *dropout* sehingga dapat diberi bimbingan khusus.



### Permasalahan Bisnis❗

Berikut adalah poin-poin masalah yang dihadapi oleh perusahaan Jaya Jaya Institut:

1. Jaya Jaya Institut mengalami tingkat *dropout* siswa yang tinggi.
2. Tidak ada sistem deteksi dini untuk mengidentifikasi siswa berisiko *dropout*.
3. Intervensi dilakukan setelah siswa sudah terlambat atau sudah *dropout*.
4. Keterbatasan *monitoring* dan visualisasi data siswa *dropout*.


### Cakupan Proyek 🎯 

1. Mengembangkan sistem prediksi berbasis data untuk mengidentifikasi siswa Jaya Jaya Institut yang memiliki risiko tinggi untuk *dropout*.
2. Menemukan faktor-faktor utama yang berkontribusi terhadap keputusan mahasiswa untuk *dropout*.
3. Menyediakan rekomendasi strategis bagi manajemen untuk menyusun program bimbingan khusus yang efektif dan tepat sasaran.
4. Memberikan dashboard interaktif di Metabase untuk *monitoring* performa mahasiswa secara real-time.


Agar proyek dapat terlaksana dengan baik dan lancar, berikut beberapa poin yang perlu dilakukan.
1. Menganalisis dataset "students' performance" untuk memahami karakteristik siswa.
2. Melatih berbagai model untuk memprediksi probabilitas *dropout* seorang mahasiswa, dengan fokus pada variabel target `Status` (khususnya kategori "Dropout").
3. Menganalisis fitur-fitur yang paling berpengaruh dalam model prediksi untuk memahami pemicu utama *dropout*.
4. Mengevaluasi performa model menggunakan metrik seperti *accuracy*, *precision*, *recall*, dan *F1-score*.
5. Menganalisis *feature importance* untuk mengidentifikasi faktor-faktor utama yang mempengaruhi *dropout*.
6. Membuat *dashboard* interaktif menggunakan Metabase untuk *monitoring* faktor-faktor *dropout*.

### Persiapan 🗂️

Sumber data: data yang digunakan dalam proyek adalah [Students' Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv). Berikut adalah deskripsi variabel-variabel yang terdapat dalam dataset:

Setup environment:

```
# Membuat virtual environment
python -m venv venv

# Aktivasi environment
# Windows
venv\Scripts\activate

# MacOS/Linux
source venv/bin/activate

# Install dependensi
pip install -r requirements.txt
```

**Menjalankan Script Prediksi**
```
python xgboost_prediction.py
```

## Business Dashboard

Tautan ke dashboard : [Dashboard Metabase](http://localhost:3000/public/dashboard/3f7efcc5-8cdd-4c58-b309-197fce2c33a4)


Dasbord ini dibangun menggunakan Metabase yang terhubung ke database PostgreSQL, dirancang khusus untuk menganalisis dan mendeteksi faktor-faktor kunci yang memengaruhi tingkat putus sekolah (dropout) mahasiswa. Dashboard dapat melakukan filter beberapa visualisasi yang dibutuhkan berdasarkan `Course`, `Status`, `Gender`, dan `Scholarship`.

Secara visual, dasbor ini menyajikan informasi yang terbagi dalam beberapa area analisis utama:

- Ringkasan eksekutif : Menampilkan metrik tingkat tinggi seperti total populasi mahasiswa, jumlah yang masih terdaftar, serta persentase angka kelulusan dan putus sekolah secara keseluruhan.
- Analisis top fitur pada feature importance : Menampilkan visualisasi fitur yang memiliki tingkat feature importance yang tinggi. Memantau persebaran, jumlah, dan persentase tiap top fitur.
- Analisis faktor akademik: Memberikan wawasan mendalam tentang bagaimana performa akademik, seperti kategori nilai, jumlah unit yang diselesaikan, dan kualifikasi pendidikan sebelumnya yang mana berkorelasi kuat dengan status akhir mahasiswa (lulus atau putus sekolah).
- Analisis demografis dan sosioekonomi: Membedah profil mahasiswa berdasarkan berbagai faktor seperti gender, usia, status perkawinan, kondisi finansial (penerima beasiswa dan status pembayaran), serta faktor personal lainnya (misalnya status "displaced").



![image](https://github.com/user-attachments/assets/990db6e5-8a2e-43f3-bb95-e618ab4f7075)




Berdasarkan potongan dashboard di atas, terdapat empat Key Performance Indicator (KPI) yang menunjukkan: 
- Total Students: 4,424
- Currently Enrolled: 794
- Dropout Rate: 32.12%
- Graduate Rate: 49.93%


![image](https://github.com/user-attachments/assets/20eef896-9dc2-41ff-93a8-15d72618c7b1)


Berdasarkan potongan dashboard di atas, terdapat visualisasi top variabel penting terhadap dropout berdasarkan tingginya nilai dalam feature importance. Diagram visualisasi di atas terdiri dari:
1. Diagram batang yang menampilkan rata-rata jumlah kurikular yang disetujui pada semester 1 dan 2 berdasarkan status,
2. Diagram lingkaran yang menampilkan proporsi data uang SPP berdasarkan kategori, yaitu yang sudah diperbarui (Up To Date) dan yang belum diprbarui (Not Up To Date),
3. Diagram batang yang menampilkan distribusi nilai penerimaan siswa berdasarkan status,
4. Diagram kombinasi yang menampilkan diagram batang dan garis untuk melihat distribusi mahasiswa terhadap jurusan yang diambil beserta tingkat rating mahasiswa yang dropout berdasarkan jurusan yang diambil.

![image](https://github.com/user-attachments/assets/9d9af235-9bc0-4fa0-8032-3737c8d59255)

Berdasarkan potongan dashboard di atas, terdapat visualisasi digram bar (bar stack) yang menampilkan visualisasi mengenai distribusi nilai berdasarkan status, distribusi kualifikasi yang diperoleh mahasiswa sebelum mendaftar berdasarkan status, dan distribusi umur berdasarkan status. Anda dapat mengeyuaikan digram dengan mengaplikasikan filter yang ada.

![image](https://github.com/user-attachments/assets/2f5e14d5-c557-461f-8817-64d4fbf248b4)

Berdasarkan potongan dashboard di atas, terdapat visualisasi faktor sosial ekonomi yang terdiri dari diagram garis dan digram batang (bar stack). Pada diagram garis menjelasakan tentang pengaruh ekonomi, seperti GDP, tingkat pengaguran, dan tingkat inflasi terhadap jumlah siswa yang menempuh pendidikan di Jaya Jaya Institut. Selain itu, pada diagram bar menampilkan proporsi status perkawinan siswa. Kedua visualisasi di atas dapat dilakukan filter, misal jika Anda ingin melihat grafik hubungan dropout dengan indikator ekononi, Anda dapat melakukan filter `Status` dan memilih kategori *Dropout*.

![image](https://github.com/user-attachments/assets/c7eda65c-7d61-49b2-8b19-e94fd8b258dc)

Berdasarkan potongan dashboard di atas, terdapat visualisasi pie (diagram lingkaran) untuk beberapa fitur sosial ekonomi untuk menganalisis proporsi tiap kategori, seperti beasiswa, gender, pengungsi, debtor (status hutang), jam kuliah (pagi/malam), dan mahasiswa internasional. Tiap visualisasi dapat disesuaikan dengan filter sesuai kebutuhan.

### ▶️ Akun Metabase

- Email: `root@mail.com`
- Password: `root123`

### ▶️ Running a Machine Learning System From ZIP File

#### 1. Prasyarat Sistem
Sebelum memulai, pastikan sistem Anda telah memenuhi persyaratan berikut:
1.  **Python**: Versi 3.9.2 atau yang lebih baru.
    - Untuk memeriksa, buka terminal dan jalankan: `python --version`
2.  **PIP**: Manajer paket Python, yang biasanya sudah terinstal bersama Python.
3.  **Koneksi Internet**: Diperlukan untuk mengunduh pustaka (library) yang dibutuhkan.
4.  **Aplikasi Pengekstrak File**: Kemampuan untuk mengekstrak atau "unzip" file (biasanya sudah bawaan sistem operasi).

#### 2. Unzip Berkas Submission

1.  Temukan file ZIP yang telah Anda terima, yaitu `submission.zip`.
2.  Klik kanan pada file tersebut dan pilih **"Extract All..."**, **"Unzip"**, atau opsi serupa yang tersedia di sistem operasi Anda.
3.  Proses ini akan menghasilkan sebuah folder baru yang berisi semua file proyek. Folder inilah yang akan kita sebut sebagai **folder proyek**.


#### 3. Buka Terminal atau Command Prompt

-   **Di Windows**: Buka Start Menu, cari **"Command Prompt"** atau **"PowerShell"**, lalu buka aplikasi tersebut.
-   **Di MacOS atau Linux**: Buka aplikasi **"Terminal"**

#### 4. Navigasi ke Folder Proyek

Setelah terminal terbuka, Anda harus masuk ke dalam folder proyek yang telah diekstrak pada Langkah 1.

-   Gunakan perintah `cd` (change directory) untuk berpindah direktori.

    **Contoh:** Jika Anda mengekstrak folder proyek di **Desktop**, perintahnya akan terlihat seperti ini:

    -   *Di Windows:*
        ```bash
        cd C:\Users\NamaAnda\Desktop\proyek_prediksi_dropout
        ```
    -   *Di MacOS/Linux:*
        ```bash
        cd /Users/NamaAnda/Desktop/proyek_prediksi_dropout
        ```
    > **Tips**: Anda juga bisa mengetik `cd` (diikuti spasi), lalu seret (drag and drop) folder proyek dari File Explorer/Finder ke jendela terminal dan tekan Enter.

#### 5. Buat dan Aktifkan Lingkungan Virtual (Virtual Environment)


1.  **Buat Lingkungan Virtual**:
    ```bash
    python -m venv [nama environment Anda]
    ```
2.  **Aktifkan Lingkungan Virtual**:
    -   *Di Windows:*
        ```bash
        [nama environment Anda]\Scripts\activate
        ```
    -   *Di MacOS/Linux:*
        ```bash
        source v[nama environment Anda]/bin/activate
        ```
    > Anda akan melihat tulisan `[nama environment Anda]` di awal baris terminal, menandakan bahwa lingkungan virtual telah aktif.

#### 6. Instal Pustaka yang Dibutuhkan

- Pastikan Anda masih berada di dalam folder proyek dan lingkungan virtual sudah aktif, lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```
-   Tunggu beberapa saat hingga proses pengunduhan dan instalasi selesai.

#### 7. Jalankan Aplikasi Streamlit

- Setelah semua persiapan selesai, Anda siap untuk menjalankan aplikasi. Jalankan perintah berikut di terminal:
    ```bash
    streamlit run dropout_app.py
    ```
- Setelah menjalankan perintah di atas, browser web default Anda akan terbuka secara otomatis dan menampilkan antarmuka aplikasi. Jika tidak terbuka, buka browser Anda secara manual dan kunjungi alamat URL yang ditampilkan di terminal (biasanya **Local URL**).
    ```
    http://localhost:8501
    ```

### ▶️ Running a Machine Learning System From GitHub

#### 1. Verifikasi Instalasi Python
Sistem ini memerlukan Python minimal versi 3.9.2 atau yang lebih baru. Untuk memverifikasi versi yang terinstal, gunakan perintah berikut.
```
python --version
```

#### 2. Unduh atau Salin Repositori
Jika Anda belum memiliki direktori proyek, Anda bisa mengunduhnya dari GitHub atau menyalinnya menggunakan perintah berikut.
```
git clone https://github.com/idhak/Menyelesaikan-Permasalahan-Institusi-Pendidikan.git
cd Menyelesaikan-Permasalahan-Institusi-Pendidikan
```

#### 3. Buat Virtual Environment dan Aktifkan (Direkomendasikan)
Buat environment terpisah untuk menghindari konflik dependensi dengan perintah berikut.
```
python -m venv venv
```
Aktivasi environment sesuai sistem operasi:

- Linux/macOS:
    ```
    source venv/bin/activate
    ```

- Windows:
    ```
    venv\Scripts\activate
    ```

#### 4. Instalasi Paket Dependensi
Dengan environment yang telah aktif, install semua library yang dibutuhkan:
```
pip install -r requirements.txt
```
#### 5. Verifikasi Keberadaan File Model
Periksa apakah file `dropout_app.py` dan model berikut tersedia di folder model/:

- Model terlatih: xgboost_model.joblib
- Konfigurasi fitur: feature_order.joblib

#### 6. Eksekusi Server Streamlit
Luncurkan aplikasi web dengan perintah:
```
streamlit run dropout_app.py
```

#### 7. Mengakses Interface Web
Aplikasi akan terbuka otomatis di browser. Jika tidak, buka secara manual di:
```
http://localhost:8501
```

> Catatan: Pastikan semua langkah diikuti secara berurutan untuk memastikan aplikasi berjalan dengan optimal.

### 🔗 Akses Prototipe

Anda dapat mengakses dan menguji prototipe yang telah dideploy secara langsung melalui tautan berikut, tanpa memerlukan proses instalasi apa pun.

🌐 [Dropout Guardian](https://dropout-guardian.streamlit.app/)

---

## 🏁 Conclusion

Berdasarkan permasalahan yang dihadapi oleh Jaya Jaya Institut, yaitu tingginya tingkat *dropout* siswa dan ketiadaan sistem deteksi dini yang efektif, proyek ini memberikan sebuah solusi berbasis data yang strategis. Melalui penerapan model pembelajaran mesin, khususnya XGBoost sebagai model terbaik, sistem yang dibangun mampu memprediksi siswa yang berisiko mengalami *dropout* secara lebih awal dan akurat, dengan nilai recall sebesar 89,42%. Hal ini sangat penting karena memungkinkan pihak institusi melakukan intervensi lebih cepat dan tepat sasaran, sehingga potensi kehilangan siswa dapat ditekan secara signifikan.

Sebelumnya, intervensi baru dilakukan setelah siswa benar-benar keluar dari sistem pendidikan, yang tentu saja sudah terlambat. Dengan adanya sistem ini, intervensi kini dapat diarahkan kepada siswa yang sudah terdeteksi berisiko bahkan sebelum mereka memutuskan untuk keluar, memungkinkan adanya pendekatan proaktif berbasis data.

Tidak hanya itu, sistem prediktif ini telah diintegrasikan dengan *dashboard monitoring* menggunakan Metabase, sehingga pihak sekolah kini dapat melakukan pemantauan terhadap status risiko siswa secara visual dan terstruktur. Dashboard ini mempermudah pelacakan tren, distribusi risiko berdasarkan kelas, hingga identifikasi kelompok siswa yang memerlukan perhatian lebih.

Secara keseluruhan, penerapan sistem ini tidak hanya berkontribusi pada penurunan potensi angka *dropout*, tetapi juga mengubah pendekatan institusi dari yang semula reaktif menjadi proaktif dan berbasis data. Ini menjadi tonggak penting dalam transformasi digital pengelolaan pendidikan di Jaya Jaya Institut, serta memberikan fondasi kuat untuk pengembangan sistem manajemen siswa yang lebih cerdas dan adaptif ke depannya.

---

## 💼 Action Items

Berikut adalah rekomendasi *action items* yang dapat di    lakukan Jaya Jaya Institut dalam menekan tingginya tingkat *dropout* siswa berdasarkan hasil analis feature importance.

### 1. Fokus Intervensi pada Capaian Akademik Semester 2
**Fitur Paling Penting:** `Curricular_units_2nd_sem_approved` (0.256)  
**Tindakan:**
- Lakukan pemantauan ketat terhadap mata kuliah yang belum disetujui (tidak lulus) pada semester kedua.
- Implementasikan program remedial atau bimbingan akademik bagi siswa dengan performa rendah.
- Buat sistem notifikasi dini jika nilai di bawah ambang batas kelulusan.


### 2. Optimalisasi Pengelolaan Pembayaran Biaya Kuliah
**Fitur Penting:** `Tuition_fees_up_to_date` (0.212)  
**Tindakan:**
- Berikan informasi dan reminder rutin mengenai tenggat waktu pembayaran biaya kuliah.
- Tawarkan skema cicilan atau bantuan keuangan bagi siswa yang sering menunggak pembayaran.
- Integrasikan status keuangan siswa dalam sistem *dashboard* agar dapat dipantau oleh akademik.


### 3. Perhatikan Jumlah SKS yang Diambil dan Diselesaikan
**Fitur Terkait:**
- `Curricular_units_1st_sem_enrolled` (0.054)
- `Curricular_units_2nd_sem_enrolled` (0.025)
- `Curricular_units_1st_sem_credited` (0.022)
- `Curricular_units_2nd_sem_credited` (0.019)

**Tindakan:**
- Evaluasi apakah jumlah SKS yang diambil terlalu banyak atau sedikit.
- Sediakan konsultasi akademik saat KRS (pengisian mata kuliah) berlangsung.
- Identifikasi dan intervensi jika mahasiswa mengambil banyak mata kuliah namun lulus sedikit.


### 4. Perkuat Dukungan Beasiswa
**Fitur Penting:** `Scholarship_holder` (0.042)  
**Tindakan:**
- Prioritaskan pemberian beasiswa kepada siswa berisiko tinggi *dropout*.
- Evaluasi efektivitas program beasiswa yang sudah ada dalam mencegah *dropout*.

### 5. Pertimbangkan Faktor Sosial-Ekonomi
**Fitur Terkait:**  `Unemployment_rate`, `GDP`, `Inflation_rate`, `Debtor` (0.015–0.019)  

**Tindakan:**
- Data eksternal tentang ekonomi siswa atau keluarganya dapat dipertimbangkan dalam kebijakan bantuan.
- Lakukan pendekatan holistik yang tidak hanya berbasis akademik.


### 6. Kembangkan Layanan Bimbingan Konseling Proaktif
**Fitur Pendukung:** 
`Daytime_evening_attendance`, `Application_mode`, `Age_at_enrollment` 

**Tindakan:**
- Lacak pola kehadiran dan deteksi perubahan mencolok.
- Konseling akademik dan psikologis bagi siswa yang terlihat pasif atau jarang hadir.


### 7. Kaji Peran Faktor Orang Tua dan Latar Belakang Keluarga
**Fitur Relevan:** `Mothers_qualification`, `Fathers_occupation`, `Marital_status`  

**Tindakan:**
- Libatkan orang tua dalam seminar atau sesi bimbingan mengenai peran mereka dalam kesuksesan pendidikan anak.
- Data ini dapat membantu penyusunan kebijakan beasiswa berbasis kebutuhan.




[def]: image.png
[def2]: image-1.png
