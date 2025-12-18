import streamlit as st

st.title("Kesimpulan dan Saran")
st.subheader("Dari hasil penelitian maka dapat di simpulkan bahwa:")

st.markdown(
    """
    <div style="text-align: justify; line-height: 1.6;">
    <b>Kesimpulan</b>

    <br><br>
    1. Variabel bebas yang dianalisis menunjukkan bahwa variabel yang berpengaruh
    signifikan terhadap output (PDB) adalah variabel modal (K). Sementara itu,
    variabel tenaga kerja (L), baik secara total maupun berdasarkan tingkat
    pendidikan—tenaga kerja dengan pendidikan di bawah diploma (non-sarjana)
    maupun tenaga kerja dengan pendidikan minimal diploma (sarjana)—menunjukkan
    pengaruh yang tidak signifikan terhadap PDB, baik atas dasar harga berlaku
    maupun atas dasar harga konstan. Pengecualian terdapat pada tenaga kerja
    sarjana atas dasar harga konstan yang menunjukkan pengaruh positif, namun
    tetap tidak signifikan secara statistik.
    
    <br><br>
    2. Hasil pengujian terhadap empat model menunjukkan bahwa jumlah seluruh
    koefisien regresi lebih kecil dari satu. Pada perhitungan atas dasar harga
    berlaku, masing-masing koefisien bernilai sebesar 0,7292 dan 0,3527.
    Sementara itu, pada perhitungan atas dasar harga konstan, jumlah koefisien
    regresi masing-masing sebesar 0,1078 dan 0,2002. Dengan demikian, hasil ini
    menunjukkan bahwa tingkat pengembalian skala bersifat menurun (decreasing
    return to scale).
    
    <br><br>
    3. Berdasarkan dua hasil analisis tersebut, dapat disimpulkan bahwa Indonesia
    saat ini berada pada tahap awal menuju Era Long Run Economic Growth.
    
    <br><br>
    <b>Saran</b>

    <br><br>
    Dalam upaya mempercepat Indonesia menuju Era Long Run Economic Growth,
    terdapat beberapa kebijakan yang dapat dijadikan sebagai masukan, antara lain:
    
    <br><br>
    1. Meningkatkan anggaran investasi di bidang pendidikan, khususnya dalam
    pengembangan keterampilan (skill) dan kegiatan penelitian serta pengembangan
    (R&D).
    
    <br><br>
    2. Memperbaiki mutu dan kualitas pendidikan, baik dari segi infrastruktur
    sarana dan prasarana maupun kualitas tenaga pengajar yang berbasis pada
    keahlian serta kebutuhan pasar global, guna menciptakan tenaga kerja terampil
    yang baru.
    
    <br><br>
    3. Meningkatkan keterampilan tenaga kerja melalui jalur pendidikan nonformal
    dalam bentuk pelatihan-pelatihan untuk meningkatkan kualitas tenaga kerja
    yang sudah ada.
    
    <br><br>
    4. Meningkatkan jumlah tenaga kerja terdidik dan terampil dengan tingkat
    pendidikan tinggi.
    
    <br><br>
    5. Meningkatkan kerja sama dengan perguruan tinggi dalam menciptakan inovasi
    terbaru, khususnya di bidang riset dan pengembangan teknologi serta
    peningkatan kualitas kelembagaan.
    </div>
    """,
    unsafe_allow_html=True
)
