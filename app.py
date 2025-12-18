import streamlit as st 

pages = [
    st.Page(page="pages/page1.py", title="Pendahuluan"),
    st.Page(page="pages/page2.py", title="Isi"),
    st.Page(page="pages/page3.py", title="Penutup"),
    st.Page(page="pages/page4.py", title="Kesimpulan dan Saran")
]
pg = st.navigation(
     pages,
     position="sidebar",
     expanded=True
     )
pg.run()