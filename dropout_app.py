import sys
import streamlit as st
import pandas as pd
import numpy as np
from xgboost_prediction import StudentDropoutPredictor
from mappings import (
    marital_status_dict,
    application_mode_dict,
    nacionality_dict,
    course_dict,
    previous_qualification_dict,
    mothers_qualification_dict,
    fathers_qualification_dict,
    mothers_occupation_dict,
    fathers_occupation_dict
)
import warnings
warnings.filterwarnings('ignore')

# Konfigurasi halaman
st.set_page_config(
    page_title="Sistem Prediksi Dropout Siswa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS untuk styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .risk-high {
        background-color: #ffebee;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #f44336;
        color: #000000;
    }
    .risk-medium {
        background-color: #fff8e1;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ff9800;
        color: #000000;
    }
    .risk-low {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎓 Sistem Prediksi Dropout Siswa<br>Jaya Jaya Institut</div>', unsafe_allow_html=True)

# Input dari sidebar
# Input dari sidebar
st.sidebar.header("📊 Input Data Siswa")
marital_status = st.sidebar.selectbox("Status Pernikahan", list(marital_status_dict.keys()))
gender_label = st.sidebar.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
gender = 1 if gender_label == "Laki-laki" else 0
age = st.sidebar.slider("Usia saat Mendaftar", 17, 70, 20)
nacionality = st.sidebar.selectbox("Kewarganegaraan", list(nacionality_dict.keys()))
application_mode = st.sidebar.selectbox("Mode Aplikasi", list(application_mode_dict.keys()))
application_order = st.sidebar.slider("Urutan Aplikasi", 0, 9, 1)
course = st.sidebar.selectbox("Program Studi", list(course_dict.keys()))
daytime_label = st.sidebar.selectbox("Waktu Kuliah", ["Malam", "Siang"])
daytime_evening = 1 if daytime_label == "Siang" else 0
prev_qualification = st.sidebar.selectbox("Kualifikasi Sebelumnya", list(previous_qualification_dict.keys()))
prev_qual_grade = st.sidebar.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 150.0, 1.0)
admission_grade = st.sidebar.slider("Nilai Penerimaan", 0.0, 200.0, 150.0, 1.0)
mothers_qual = st.sidebar.selectbox("Kualifikasi Ibu", list(mothers_qualification_dict.keys()))
fathers_qual = st.sidebar.selectbox("Kualifikasi Ayah", list(fathers_qualification_dict.keys()))
mothers_occ = st.sidebar.selectbox("Pekerjaan Ibu", list(mothers_occupation_dict.keys()))
fathers_occ = st.sidebar.selectbox("Pekerjaan Ayah", list(fathers_occupation_dict.keys()))

displaced_label = st.sidebar.selectbox("Status Pengungsi", ["Tidak", "Ya"])
displaced = 1 if displaced_label == "Ya" else 0

ed_needs_label = st.sidebar.selectbox("Kebutuhan Khusus", ["Tidak", "Ya"])
ed_special_needs = 1 if ed_needs_label == "Ya" else 0

debtor_label = st.sidebar.selectbox("Status Hutang", ["Tidak", "Ya"])
debtor = 1 if debtor_label == "Ya" else 0

tu_fee_label = st.sidebar.selectbox("Status SPP", ["Belum Diperbarui", "Terkini"])
tu_fee_up = 1 if tu_fee_label == "Terkini" else 0

scholar_label = st.sidebar.selectbox("Penerima Beasiswa", ["Tidak", "Ya"])
scholarship = 1 if scholar_label == "Ya" else 0

intl_label = st.sidebar.selectbox("Mahasiswa Internasional", ["Tidak", "Ya"])
international = 1 if intl_label == "Ya" else 0

unemployment = st.sidebar.number_input("Tingkat Pengangguran", 0.0, 50.0, 10.8)
gdp = st.sidebar.number_input("GDP", -10.0, 10.0, 1.74)


# Input tambahan fitur penting
st.sidebar.subheader("📘 Data Akademik Tambahan (Fitur Penting)")
cu_1st_credited = st.sidebar.slider("SKS Semester 1 (Credited)", 0, 100, 6)
cu_1st_enrolled = st.sidebar.slider("Mata Kuliah Semester 1 (Enrolled)", 0, 100, 6)
cu_1st_approved = st.sidebar.slider("Mata Kuliah Lulus Semester 1 (Approved)", 0, 100, 6)
cu_1st_wo_eval = st.sidebar.slider("Tanpa Evaluasi Semester 1", 0, 10, 0)
cu_2nd_credited = st.sidebar.slider("SKS Semester 2 (Credited)", 0, 100, 6)
cu_2nd_enrolled = st.sidebar.slider("Mata Kuliah Semester 2 (Enrolled)", 0, 100, 6)
cu_2nd_approved = st.sidebar.slider("Mata Kuliah Lulus Semester 2 (Approved)", 0, 100, 6)
cu_2nd_grade = st.sidebar.slider("Rata-rata Nilai Semester 2", 0.0, 20.0, 13.9, 0.1)

# Tombol prediksi
if st.sidebar.button("🔮 Prediksi Dropout"):
    input_data = {
        'Marital_status': marital_status_dict[marital_status],
        'Application_mode': application_mode_dict[application_mode],
        'Application_order': application_order,
        'Course': course_dict[course],
        'Daytime_evening_attendance': daytime_evening,
        'Previous_qualification': previous_qualification_dict[prev_qualification],
        'Previous_qualification_grade': prev_qual_grade,
        'Admission_grade': admission_grade,
        'Nacionality': nacionality_dict[nacionality],
        'Mothers_qualification': mothers_qualification_dict[mothers_qual],
        'Fathers_qualification': fathers_qualification_dict[fathers_qual],
        'Mothers_occupation': mothers_occupation_dict[mothers_occ],
        'Fathers_occupation': fathers_occupation_dict[fathers_occ],
        'Displaced': displaced,
        'Educational_special_needs': ed_special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tu_fee_up,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age,
        'International': international,
        'Curricular_units_1st_sem_credited': cu_1st_credited,
        'Curricular_units_1st_sem_enrolled': cu_1st_enrolled,
        'Curricular_units_1st_sem_approved': cu_1st_approved,
        'Curricular_units_1st_sem_without_evaluations': cu_1st_wo_eval,
        'Curricular_units_1st_sem_grade': 13.9,
        'Curricular_units_2nd_sem_credited': cu_2nd_credited,
        'Curricular_units_2nd_sem_enrolled': cu_2nd_enrolled,
        'Curricular_units_2nd_sem_approved': cu_2nd_approved,
        'Curricular_units_2nd_sem_grade': cu_2nd_grade,
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Target': 13.9,
        'Inflation_rate': 0.3,
        'Unemployment_rate': unemployment,
        'GDP': gdp
    }

    try:
        predictor = StudentDropoutPredictor()
        result = predictor.predict_dropout(input_data)
        prob = result['dropout_probability']
        label = 'Dropout' if result['dropout_prediction'] == 1 else 'Not Dropout'

        if prob >= 0.7:
            risk_level = "Tinggi"
            risk_color = "🔴"
            risk_class = 'risk-high'
            recommendations = [
                "Segera hubungi konselor akademik untuk penanganan awal.",
                "Jadwalkan sesi konseling rutin dan intensif.",
                "Tinjau status pembayaran dan bantu ajukan beasiswa atau keringanan biaya.",
                "Evaluasi kembali beban studi dan adaptasi kurikulum jika perlu.",
                "Libatkan wali/orang tua dalam pemantauan akademik.",
                "Identifikasi kendala psikososial (stres, isolasi, dll.) dan rujuk ke layanan psikolog kampus."
            ]
        elif prob >= 0.4:
            risk_level = "Sedang"
            risk_color = "🟡"
            risk_class = 'risk-medium'
            recommendations = [
                "Dorong untuk mengikuti kelas tambahan atau remedial.",
                "Tetapkan mentor atau pembimbing akademik.",
                "Pantau nilai dan kehadiran secara mingguan.",
                "Berikan notifikasi motivasi dan pengingat belajar.",
                "Tetapkan target belajar jangka pendek yang realistis.",
                "Ajak bergabung ke komunitas belajar atau kelompok studi."
            ]
        else:
            risk_level = "Rendah"
            risk_color = "🟢"
            risk_class = 'risk-low'
            recommendations = [
                "Pertahankan semangat belajar dengan dukungan positif.",
                "Berikan penghargaan atau pengakuan untuk capaian akademik.",
                "Tetap pantau performa secara berkala (bulanan).",
                "Libatkan dalam program pengembangan diri atau leadership.",
                "Jadikan role model bagi siswa lain melalui testimoni atau kegiatan mentoring.",
                "Sediakan forum untuk feedback dan masukan dari siswa."
            ]

        # Tampilkan hasil dan rekomendasi
        st.markdown(f"""
        <div class="{risk_class}">
            <h3>{risk_color} Tingkat Risiko: {risk_level}</h3>
            <p><strong>Probabilitas Dropout:</strong> {prob:.2%}</p>
            <p><strong>Prediksi:</strong> {label}</p>
            <hr>
            <h4>🛠️ Rekomendasi Tindakan:</h4>
            <ul>
                {''.join(f"<li>{rec}</li>" for rec in recommendations)}
            </ul>
        </div>
        """, unsafe_allow_html=True)


    except Exception as e:
        st.error(f"Error saat prediksi: {e}")

else:
    st.info("Masukkan data dan klik tombol prediksi untuk melihat hasil.")