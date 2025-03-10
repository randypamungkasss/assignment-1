import streamlit as st
import pandas as pd
import random
import time
from libs.daftar_kota import daftar_kota

st.title("Tugas Week-1")
st.write("Disini saya akan membuat aplikasi sebuah tiket pelaporan gangguan")

nama = st.text_input("Nama")
no_hp = st.text_input("Nomor Handphone")
kota = st.selectbox("Kota", [""] + daftar_kota)
kendala = st.text_area("Kendala")

submit_button = st.button("Input Tiket")

csv = pd.read_csv("data.csv", dtype={"no hp": str})

if submit_button:
    if not nama and not no_hp and not kota and not kendala:
        st.error(
            "Terus aku mok kongkon nginput opo iki blokkk goblokkkk gak mikir utek e!"
        )
    elif not nama:
        st.error("Kolom Nama harus diisi")
    elif not no_hp:
        st.error("Kolom Nomor Handphone harus di isi")
    elif not kota:
        st.error("Kolom Kota Harus di pilih")
    elif not kendala:
        st.error("Kolom Kendala harus di isi")
    else:
        st.toast("Pelaporan anda berhasil di input dengan status Tiket Open")
        time.sleep(5)
        new_tiket = f"DV{random.randint(10000,99999)}"
        new_id = csv["id"].max() + 1 if not csv.empty else 1
        new_data = pd.DataFrame(
            [[new_id, new_tiket, nama, no_hp, kota, kendala, "Open"]],
            columns=["id", "tiket", "nama", "no hp", "kota", "kendala", "status"],
        )
        csv = pd.concat([csv, new_data], ignore_index=True)
        csv.to_csv("data.csv", index=False)
        st.rerun()

csv.columns = [col.upper() for col in csv.columns]

st.write("### Data Ticketing")
edited_df = st.data_editor(csv, hide_index=True)

save_button = st.button("Save Changes")

if save_button:
    edited_df.to_csv("data.csv", index=False)
    st.rerun()
