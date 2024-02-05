import streamlit as st

def cataract_info_page():
    st.title("Informasi Katarak")

    st.header("Apa itu Katarak?")
    st.write("Katarak adalah kondisi dimana lensa mata yang seharusnya bening menjadi keruh. "
             "Ini dapat menyebabkan penglihatan kabur dan menghambat kemampuan melihat dengan jelas. "
             "Katarak biasanya berkembang perlahan seiring bertambahnya usia, tetapi juga dapat disebabkan "
             "oleh faktor-faktor lain seperti cedera mata, penyakit tertentu, atau penggunaan obat-obatan tertentu.")


    cataract_image_url = "katarak.jpg"
    st.image(cataract_image_url, caption="Gambar: Apa itu Katarak?", use_column_width=True)


    st.header("Penyebab Katarak")
    st.write("Katarak dapat disebabkan oleh berbagai faktor. Beberapa di antaranya melibatkan penuaan, "
             "paparan radiasi ultraviolet dari matahari, cedera mata, penggunaan obat-obatan tertentu, atau "
             "kehadiran penyakit tertentu seperti diabetes. Terkadang, faktor genetik juga dapat memainkan peran.")


    causes_image_url = "sinaruv.jpg"  
    st.image(causes_image_url, caption="Gambar: Penyebab Katarak", use_column_width=True)

    st.header("Pencegahan Katarak")
    st.write("Meskipun penuaan adalah faktor risiko utama, ada beberapa langkah yang dapat diambil untuk "
             "mencegah atau memperlambat perkembangan katarak. Ini melibatkan menjaga kesehatan mata dengan "
             "menggunakan kacamata hitam dengan perlindungan UV saat berada di bawah sinar matahari, menjaga pola "
             "makan sehat dengan memasukkan makanan bergizi, dan menghindari kebiasaan merokok.")


    prevention_image_url = "pencegahan.jpg"  
    st.image(prevention_image_url, caption="Gambar: Pencegahan Katarak", use_column_width=True)

if __name__ == "__main__":
    cataract_info_page()
