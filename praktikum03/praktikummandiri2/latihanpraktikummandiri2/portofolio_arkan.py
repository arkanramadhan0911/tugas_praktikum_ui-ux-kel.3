import streamlit as st

st.set_page_config(
    page_title="Portofolio Arkan Zahran Ramadhan",
    page_icon="👨‍💻",
    layout="wide",
)

with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120
    )
    st.title("Arkan Zahran R.")
    st.caption("Teknik Informatika - STT NF")
    st.write("📍 Setiabudi / Jakarta, Indonesia")
    st.markdown("---")
    st.write("📫 **Kontak & Sosial Media:**")
    st.write("📧 Email: arkan@example.com")
    st.write("🔗 LinkedIn: [linkedin.com/in/arkan](#)")
    st.write("🐙 GitHub: [github.com/arkan](#)")

st.title("⚡ Portofolio Interaktif & Profil Profesional")
st.subheader("Network Engineering Enthusiast & Python Developer")
st.write(
    "Selamat datang di portofolio web saya! Halaman ini dibangun murni"
    " menggunakan Python dan Streamlit."
)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Mata Kuliah", value="TI Semester 1")
with col2:
    st.metric(label="Fokus", value="Network & Coding")
with col3:
    st.metric(label="Sertifikasi", value="BNSP Network")
with col4:
    st.metric(label="Status", value="Aktif BEM PPI")

st.markdown("---")

tab1, tab2, tab3 = st.tabs([
    "👤 Tentang Saya",
    "🚀 Proyek & Keahlian",
    "💬 Pesan Interaktif",
])

with tab1:
    st.header("Pengalaman & Latar Belakang")
    st.write("""
    Saya adalah mahasiswa Teknik Informatika di **STT Terpadu Nurul Fikri** yang memiliki ketertarikan mendalam pada 
    **Home Network Architecture**, **Enterprise Routing (Cisco Packet Tracer)**, serta pengembangan logika program menggunakan **Python**.
    Selain fokus akademis, saya juga aktif di divisi **Publikasi, Penyiaran, dan Informasi (PPI) BEM STT NF**.
    """)

    st.subheader("💡 Tingkat Penguasaan Skill:")
    st.write("Python Logic & Control Flow")
    st.progress(85)
    st.write("Network Engineering (OSPF, BGP, VLAN)")
    st.progress(90)
    st.write("Team working, management waktu, problem solving, organization")
    st.progress(95)

with tab2:
    st.header("Kumpulan Proyek Unggulan")
    col_proj1, col_proj2 = st.columns(2)

    with col_proj1:
        with st.expander("🌐 1. Topologi Jaringan (Cisco)", expanded=True):
            st.write(
                "Merancang dan mengonfigurasi jaringan multi-router menggunakan"
                " protokol routing OSPF, BGP, EtherChannel LACP, dan VLAN ACL."
            )
            st.caption("Tools: Cisco Packet Tracer, Mikrotik hAP Lite, Huawei B311B")

    with col_proj2:
        with st.expander(
            "🐍 2. Sistem Keamanan PIN ATM & Detector Prima", expanded=True):
            st.write(
                "Mengembangkan logika perulangan Python (`while` & `for...else`)"
                " untuk sistem autentikasi PIN serta penyaring bilangan prima."
            )
            st.caption("Tools: Python, VS Code, Google Colab")

with tab3:
    st.header("Tinggalkan Pesan")
    nama = st.text_input("Nama Kamu:")
    pesan = st.text_area("Pesan / Masukan:")

    if st.button("Kirim Pesan 🚀"):
        if nama and pesan:
            st.balloons()
            st.success(
                f"Terima kasih {nama}! Pesan kamu berhasil terkirim dengan efek balon 🎉"
            )
        else:
            st.warning("Silakan isi nama dan pesan terlebih dahulu ya!")