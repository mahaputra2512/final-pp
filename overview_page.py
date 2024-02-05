import streamlit as st

def overview_page():
    st.title("Overview: Cataract Prediction App")
    st.write("Selamat datang di Aplikasi Prediksi Katarak. Aplikasi ini memungkinkan Anda untuk memprediksi apakah "
             "suatu gambar mata mengandung katarak atau tidak.")

    # Informasi lebih lanjut tentang cara menggunakan aplikasi
    st.header("Cara Menggunakan Aplikasi")
    st.write("1. **Unggah Gambar Mata**: Pilih tombol 'Unggah Gambar' untuk mengunggah gambar mata yang ingin Anda "
             "deteksi kataraknya. Pastikan gambar tersebut jelas dan fokus pada mata.")

    st.write("2. **Proses Prediksi**: Setelah mengunggah gambar, aplikasi akan memprosesnya menggunakan model deteksi "
             "katarak. Proses ini biasanya membutuhkan beberapa detik.")

    st.write("3. **Hasil Prediksi**: Setelah selesai, hasil prediksi akan ditampilkan. Anda akan mengetahui apakah gambar "
             "mata tersebut diperkirakan mengandung katarak atau tidak.")

    st.header("Catatan Penting")
    st.write("Aplikasi ini bersifat informatif dan bukan sebagai pengganti diagnosis medis profesional. Jika Anda "
             "mengalami gejala mata yang mengkhawatirkan, disarankan untuk berkonsultasi dengan dokter mata.")

    st.header("Tentang Model Deteksi Katarak")
    st.write("Model yang digunakan dalam aplikasi ini telah dilatih dengan dataset gambar mata yang mengandung dan tidak "
             "mengandung katarak. Namun, hasil prediksi tidak selalu 100% akurat, dan interpretasi hasil sebaiknya "
             "dilakukan oleh profesional kesehatan.")

    st.write("Jangan ragu untuk mencoba aplikasi ini dan melihat sejauh mana akurasinya! Ingatlah untuk tetap konsultasi "
             "dengan dokter jika Anda memiliki kekhawatiran kesehatan mata.")

    # Menambahkan logo aplikasi dan gambar mata dari assets
    st.image("logo.jpeg", use_column_width=True)
    st.image("katarak.jpg", use_column_width=True)

if __name__ == "__main__":
    overview_page()
