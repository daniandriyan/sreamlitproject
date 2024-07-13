import streamlit as st
from datetime import datetime

# Fungsi untuk mendapatkan tanggal saat ini
def get_current_date():
    return datetime.now().strftime("%d/%m/%Y")

# Fungsi untuk menghitung total gaji dokter
def hitung_gaji(nama_dokter, pasien_umum, go, skbs, nebu, au, chol, gds, wts, fee_tindakan, wtb, uang_makan, potongan):
    try:
        pasien_umum = int(pasien_umum or 0)
        go = int(go or 0)
        skbs = int(skbs or 0)
        nebu = int(nebu or 0)
        au = int(au or 0)
        chol = int(chol or 0)
        gds = int(gds or 0)
        wts = int(wts or 0)
        fee_tindakan = int(fee_tindakan or 0)
        wtb = int(wtb or 0)
        uang_makan = int(uang_makan or 0)
        potongan = int(potongan or 0)
        
        total_gaji_sebelum_potongan = (
            pasien_umum * 10000 +
            go * 100000 +
            skbs * 10000 +
            nebu * 15000 +
            au * 3000 +
            chol * 3000 +
            gds * 3000 +
            wts * 15000 +
            fee_tindakan * 30000 +
            wtb * 20000 +
            uang_makan * 15000
        )

        total_gaji = total_gaji_sebelum_potongan - potongan

        hasil = f"""
        Nama Dokter: {nama_dokter}\n
        Tanggal: {get_current_date()}\n
        Total Gaji Sebelum Potongan: Rp. {total_gaji_sebelum_potongan:,}\n
        Potongan: Rp. {potongan:,}\n
        Total Gaji: Rp. {total_gaji:,}
        """

        return hasil

    except ValueError:
        return "Semua input harus berupa angka"

# Membuat antarmuka menggunakan Streamlit
st.title("Aplikasi Perhitungan Gaji Dokter")

nama_dokter = st.text_input("Nama Dokter")
pasien_umum = st.number_input("Pasien Umum", min_value=0, value=0)
go = st.number_input("GO", min_value=0, value=0)
skbs = st.number_input("SKBS", min_value=0, value=0)
nebu = st.number_input("NEBU", min_value=0, value=0)
au = st.number_input("AU", min_value=0, value=0)
chol = st.number_input("CHOL", min_value=0, value=0)
gds = st.number_input("GDS", min_value=0, value=0)
wts = st.number_input("WTS", min_value=0, value=0)
fee_tindakan = st.number_input("Fee Tindakan", min_value=0, value=0)
wtb = st.number_input("WTB", min_value=0, value=0)
uang_makan = st.number_input("Uang Makan", min_value=0, value=0)
potongan = st.number_input("Potongan", min_value=0, value=0)

if st.button("Hitung Gaji"):
    hasil = hitung_gaji(nama_dokter, pasien_umum, go, skbs, nebu, au, chol, gds, wts, fee_tindakan, wtb, uang_makan, potongan)
    st.text_area("Total Gaji Dokter", hasil)
