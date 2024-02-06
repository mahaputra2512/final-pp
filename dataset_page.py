import streamlit as st

def dataset_page():
    st.title("Informasi Dataset")
    st.title("Link Dataset : https://www.kaggle.com/datasets/nandanp6/cataract-image-dataset")
    st.write("""
        **Dataset Mata Katarak**

        Dataset ini dibuat untuk aplikasi praktis dari pembelajaran mendalam dalam bidang medis. Semua dataset katarak yang ada berupa laporan medis dan bukan gambar langsung. Namun, untuk membuat aplikasi seperti detektor katarak dengan gambar mata, dataset ini dapt digunakan.

        Dataset ini berisi jumlah gambar yang cukup untuk melatih jaringan saraf. Dataset ini berhasil mencapai akurasi 90% atau lebih dengan arsitektur CNN dasar untuk klasifikasi.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("gambar1.png", caption="Gambar 1", use_column_width=True)

    with col2:
        st.image("gambar2.png", caption="Gambar 2", use_column_width=True)

    with col3:
        st.image("gambar3.png", caption="Gambar 3", use_column_width=True)

if __name__ == "__main__":
    dataset_page()
