marital_status_dict = {
    "lajang": 1,
    "menikah": 2,
    "duda/janda": 3,
    "cerai": 4,
    "kumpul kebo": 5,
    "pisah hukum": 6
}

application_mode_dict = {
    "fase ke-1 - kontingen umum": 1,
    "Ordonansi No. 612/93": 2,
    "fase ke-1 - kontingen khusus (Kepulauan Azores)": 5,
    "Pemegang kursus tinggi lainnya": 7,
    "Ordonansi No. 854-B/99": 10,
    "Mahasiswa internasional (sarjana)": 15,
    "fase ke-1 - kontingen khusus (Pulau Madeira)": 16,
    "fase ke-2 - kontingen umum": 17,
    "fase ke-3 - kontingen umum": 18,
    "Ordonansi No. 533-A/99, item b2) (Rencana Berbeda)": 26,
    "Ordonansi No. 533-A/99, item b3 (Institusi Lain)": 27,
    "Di atas 23 tahun": 39,
    "Transfer": 42,
    "Ganti jurusan": 43,
    "Pemegang diploma spesialisasi teknologi": 44,
    "Ganti institusi/jurusan": 51,
    "Pemegang diploma siklus pendek": 53,
    "Ganti institusi/jurusan (Internasional)": 57
}

course_dict = {
    "Teknologi Produksi Biofuel": 33,
    "Desain Animasi dan Multimedia": 171,
    "Layanan Sosial (kehadiran malam)": 8014,
    "Agronomi": 9003,
    "Desain Komunikasi": 9070,
    "Keperawatan Veteriner": 9085,
    "Teknik Informatika": 9119,
    "Equinkultur": 9130,
    "Manajemen": 9147,
    "Layanan Sosial": 9238,
    "Pariwisata": 9254,
    "Keperawatan": 9500,
    "Kebersihan Mulut": 9556,
    "Manajemen Periklanan dan Pemasaran": 9670,
    "Jurnalisme dan Komunikasi": 9773,
    "Pendidikan Dasar": 9853,
    "Manajemen (kehadiran malam)": 9991
}

daytime_evening_dict = {
    "siang hari": 1,
    "malam hari": 0
}

previous_qualification_dict = {
    "Pendidikan menengah": 1,
    "Pendidikan tinggi - gelar sarjana": 2,
    "Pendidikan tinggi - gelar": 3,
    "Pendidikan tinggi - master": 4,
    "Pendidikan tinggi - doktor": 5,
    "Frekuensi pendidikan tinggi": 6,
    "Tahun ke-12 sekolah - tidak selesai": 9,
    "Tahun ke-11 sekolah - tidak selesai": 10,
    "Lainnya - tahun ke-11 sekolah": 12,
    "Tahun ke-10 sekolah": 14,
    "Tahun ke-10 sekolah - tidak selesai": 15,
    "Pendidikan dasar siklus ke-3 (tahun ke-9/10/11) atau setara": 19,
    "Pendidikan dasar siklus ke-2 (tahun ke-6/7/8) atau setara": 38,
    "Kursus spesialisasi teknologi": 39,
    "Pendidikan tinggi - gelar (siklus ke-1)": 40,
    "Kursus teknis tinggi profesional": 42,
    "Pendidikan tinggi - master (siklus ke-2)": 43
}

nacionality_dict = {
    "Portugis": 1, "Jerman": 2, "Spanyol": 6, "Italia": 11, "Belanda": 13, "Inggris": 14,
    "Lithuania": 17, "Angola": 21, "Cape Verde": 22, "Guinea": 24, "Mozambik": 25,
    "Santome": 26, "Turki": 32, "Brasil": 41, "Rumania": 62, "Moldova (Republik)": 100,
    "Meksiko": 101, "Ukraina": 103, "Rusia": 105, "Kuba": 108, "Kolombia": 109
}

# Untuk mother_qualification dan father_qualification kita bisa pakai mapping yang sama
mothers_qualification_dict = fathers_qualification_dict = {
    "Pendidikan Menengah - Tahun ke-12 Sekolah atau Setara": 1,
    "Pendidikan Tinggi - Gelar Sarjana": 2,
    "Pendidikan Tinggi - Gelar": 3,
    "Pendidikan Tinggi - Master": 4,
    "Pendidikan Tinggi - Doktor": 5,
    "Frekuensi Pendidikan Tinggi": 6,
    "Tahun ke-12 Sekolah - Tidak Selesai": 9,
    "Tahun ke-11 Sekolah - Tidak Selesai": 10,
    "Tahun ke-7 (Lama)": 11,
    "Lainnya - Tahun ke-11 Sekolah": 12,
    "Tahun ke-10 Sekolah": 14,
    "Kursus perdagangan umum": 18,
    "Pendidikan Dasar Siklus ke-3 (Tahun ke-9/10/11) atau Setara": 19,
    "Kursus teknis-profesional": 22,
    "Tahun ke-7 sekolah": 26,
    "Siklus ke-2 kursus sekolah menengah umum": 27,
    "Tahun ke-9 Sekolah - Tidak Selesai": 29,
    "Tahun ke-8 sekolah": 30,
    "Tidak diketahui": 34,
    "Tidak bisa baca tulis": 35,
    "Bisa baca tanpa tahun ke-4 sekolah": 36,
    "Pendidikan dasar siklus ke-1 (tahun ke-4/5) atau setara": 37,
    "Pendidikan Dasar Siklus ke-2 (Tahun ke-6/7/8) atau Setara": 38,
    "Kursus spesialisasi teknologi": 39,
    "Pendidikan tinggi - gelar (siklus ke-1)": 40,
    "Kursus studi tinggi khusus": 41,
    "Kursus teknis tinggi profesional": 42,
    "Pendidikan Tinggi - Master (siklus ke-2)": 43,
    "Pendidikan Tinggi - Doktor (siklus ke-3)": 44
}

# Mother/father occupation: disarankan import dari file CSV jika ingin lengkap
# Disini ditampilkan sebagian saja untuk contoh
mothers_occupation_dict = fathers_occupation_dict = {
    "Mahasiswa": 0,
    "Perwakilan Kekuasaan Legislatif dan Badan Eksekutif, Direktur, Direktur dan Manajer Eksekutif": 1,
    "Spesialis dalam Kegiatan Intelektual dan Ilmiah": 2,
    "Teknisi Tingkat Menengah dan Profesi": 3,
    "Staf administratif": 4,
    "Layanan Pribadi, Pekerja Keamanan dan Keselamatan dan Penjual": 5,
    "Petani dan Pekerja Terampil di Pertanian, Perikanan dan Kehutanan": 6,
    "Pekerja Terampil di Industri, Konstruksi dan Pengrajin": 7,
    "Operator Instalasi dan Mesin dan Pekerja Perakitan": 8,
    "Pekerja Tidak Terampil": 9,
    "Profesi Angkatan Bersenjata": 10,
    "Profesional kesehatan": 122,
    "Guru": 123,
    "Spesialis dalam teknologi informasi dan komunikasi (TIK)": 125,
    "Teknisi dan profesi tingkat menengah sains dan teknik": 131,
    "Teknisi dan profesional, tingkat menengah kesehatan": 132,
    "Teknisi tingkat menengah dari layanan hukum, sosial, olahraga, budaya dan serupa": 134,
    "Pekerja kantor, sekretaris secara umum dan operator pemrosesan data": 141,
    "Operator terkait data, akuntansi, statistik, layanan keuangan dan registri": 143,
    "Pekerja layanan pribadi": 151,
    "Penjual": 152,
    "Pekerja kebersihan": 191,
    "Asisten persiapan makanan": 194
}