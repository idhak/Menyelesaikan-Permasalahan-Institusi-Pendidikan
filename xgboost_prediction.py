# === Library Umum ===
import xgboost as xgb
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')  # Nonaktifkan peringatan runtime

class StudentDropoutPredictor:
    def __init__(self, model_path='xgboost_model/xgboost_model.joblib', feature_order_path='xgboost_model/feature_order.joblib'):
        """
        Inisialisasi prediktor dengan model yang sudah dilatih dan urutan fitur

        Args:
            model_path (str): Path ke model XGBoost yang sudah disimpan
            feature_order_path (str): Path ke file urutan fitur yang disimpan
        """
        try:
            self.model = joblib.load(model_path)
            self.feature_order = joblib.load(feature_order_path)
            print("Model dan urutan fitur berhasil dimuat.")
        except FileNotFoundError as e:
            print(f"Error: File tidak ditemukan - {e}")
            raise
        except Exception as e:
            print(f"Error saat memuat model: {e}")
            raise

    def preprocess_input(self, input_data):
        """
        Melakukan praproses data input agar sesuai dengan format data pelatihan

        Args:
            input_data (dict): Dictionary berisi informasi siswa

        Returns:
            pd.DataFrame: Data yang telah diproses dan siap digunakan untuk prediksi
        """
        # Konversi input menjadi DataFrame
        df = pd.DataFrame([input_data])

        # One-hot encoding untuk variabel kategorikal
        categorical_cols = [
            'Marital_status', 'Application_mode', 'Course', 'Daytime_evening_attendance',
            'Displaced', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date',
            'Gender', 'Scholarship_holder', 'International'
        ]

        # Terapkan one-hot encoding
        df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=False)

        # Pastikan semua fitur dari pelatihan tersedia
        for feature in self.feature_order:
            if feature not in df_encoded.columns:
                df_encoded[feature] = 0

        # Susun ulang kolom agar sesuai dengan urutan fitur pelatihan
        df_encoded = df_encoded.reindex(columns=self.feature_order, fill_value=0)

        return df_encoded

    def predict_dropout(self, input_data):
        """
        Memprediksi probabilitas dropout untuk seorang siswa

        Args:
            input_data (dict): Dictionary berisi informasi siswa

        Returns:
            dict: Dictionary berisi hasil prediksi
        """
        try:
            # Praproses data input
            processed_data = self.preprocess_input(input_data)

            # Lakukan prediksi
            dropout_probability = self.model.predict_proba(processed_data)[0][1]
            dropout_prediction = self.model.predict(processed_data)[0]

            # Tentukan tingkat risiko
            if dropout_probability >= 0.7:
                risk_level = "Tinggi"
                risk_color = "🔴"
            elif dropout_probability >= 0.4:
                risk_level = "Sedang"
                risk_color = "🟡"
            else:
                risk_level = "Rendah"
                risk_color = "🟢"

            return {
                'dropout_probability': dropout_probability,
                'dropout_prediction': dropout_prediction,
                'risk_level': risk_level,
                'risk_color': risk_color,
                'recommendation': self._get_recommendation(dropout_probability, input_data)
            }

        except Exception as e:
            print(f"Error saat melakukan prediksi: {e}")
            raise

    def _get_recommendation(self, probability, input_data):
        """
        Memberikan rekomendasi berdasarkan hasil prediksi

        Args:
            probability (float): Probabilitas dropout
            input_data (dict): Data input asli

        Returns:
            list: Daftar rekomendasi
        """
        recommendations = []

        if probability >= 0.7:
            recommendations.append("🚨 Perlu intervensi segera!")
            recommendations.append("📞 Hubungi konselor akademik")
            recommendations.append("💰 Periksa status pembayaran dan bantuan keuangan")

        elif probability >= 0.4:
            recommendations.append("⚠️ Monitoring lebih ketat diperlukan")
            recommendations.append("📚 Berikan dukungan akademik tambahan")

        else:
            recommendations.append("✅ Siswa dalam kondisi baik")
            recommendations.append("📈 Pertahankan performa akademik")

        # Rekomendasi khusus berdasarkan fitur input
        if input_data.get('Tuition_fees_up_to_date', 1) == 0:
            recommendations.append("💳 Segera atur pembayaran biaya kuliah")

        if input_data.get('Scholarship_holder', 0) == 0 and probability > 0.3:
            recommendations.append("🎓 Pertimbangkan aplikasi beasiswa")

        return recommendations

def create_sample_input():
    """
    Membuat data input contoh untuk pengujian

    Returns:
        dict: Data siswa contoh
    """
    return {
        'Marital_status': 1,  # Belum menikah
        'Application_mode': 1,
        'Course': 33,
        'Daytime_evening_attendance': 1,
        'Previous_qualification': 1,
        'Nationality': 1,
        'Mother_qualification': 19,
        'Father_qualification': 13,
        'Mother_occupation': 4,
        'Father_occupation': 10,
        'Displaced': 1,
        'Educational_special_needs': 0,
        'Debtor': 0,
        'Tuition_fees_up_to_date': 1,
        'Gender': 1,
        'Scholarship_holder': 0,
        'Age_at_enrollment': 20,
        'International': 0,
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': 6,
        'Curricular_units_1st_sem_evaluations': 6,
        'Curricular_units_1st_sem_approved': 6,
        'Curricular_units_1st_sem_grade': 13.9,
        'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': 6,
        'Curricular_units_2nd_sem_evaluations': 6,
        'Curricular_units_2nd_sem_approved': 6,
        'Curricular_units_2nd_sem_grade': 13.9,
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Target': 13.9,
        'Inflation_rate': 0.3,
        'Unemployment_rate': 10.8,
        'GDP': 1.74
    }

# Contoh penggunaan
if __name__ == "__main__":
    try:
        # Inisialisasi prediktor
        predictor = StudentDropoutPredictor()

        # Buat input contoh
        sample_data = create_sample_input()

        # Lakukan prediksi
        result = predictor.predict_dropout(sample_data)

        # Tampilkan hasil
        print("=== HASIL PREDIKSI DROPOUT SISWA ===")
        print(f"Probabilitas Dropout: {result['dropout_probability']:.4f} ({result['dropout_probability']*100:.2f}%)")
        print(f"Prediksi: {'Dropout' if result['dropout_prediction'] == 1 else 'Tidak Dropout'}")
        print(f"Tingkat Risiko: {result['risk_color']} {result['risk_level']}")
        print("\nRekomendasi:")
        for rec in result['recommendation']:
            print(f"  {rec}")

    except Exception as e:
        print(f"Error: {e}")
