import streamlit as st

st.subheader("METODE PENELITIAN")

st.markdown(
    """
    <div style="text-align: justify; line-height: 1.6;">
    Data yang digunakan dalam makalah ini adalah data sekunder time series yang berasal dari Badan Pusat Statistik (BPS)
    dengan judul “Statistik Indonesia” dan “ Indikator Ekonomi” dari tahun 2000 sampai 2013.
    </div>


    """,
    unsafe_allow_html=True
)

st.subheader("METODE ANALISIS")

st.markdown(
    """
    <div style="text-align: justify; line-height: 1.6;">
    Analisis yang digunakan adalah analisis deskriptif kuantitatif, kualitatif dan analisis inferensial. Analisis deskriptif bertujuan untuk menggambarkan variabel-variabel terkait dengan pendapatan nasional,
    pembentukan modal serta karakteristik tenaga kerja di Indonesia (model endogenius). Analisis inferensial dilakukan dengan menggunakan model fungsi Cobb-Douglas yang dilinierisasikan menjadi model regresi linear berganda.
    Model tersebut akan menjelaskan hubungan antara variabel bebas (X) terhadap variabel tak bebas (Y).
    </div>

    """,
    unsafe_allow_html=True
)
