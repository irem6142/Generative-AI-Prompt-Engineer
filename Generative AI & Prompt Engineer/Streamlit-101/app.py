#Kütüphane eklemek
import streamlit as st
import json
# Başlık ve logoyu değiştirmek.İlk burayı yazmamız lazım yoksa hata alırız.

st.set_page_config(page_title="Streamlit-101",page_icon=":skier:")

# Metin gösterme

# st.write("Hello world!")

# st.markdown("_Markdown_")

# st.code("for i in range(10):my_funciton()")

# st.header("Büyük Başlık")

# st.subheader("Alt başlık")


tab1,tab2=st.tabs(["Kullancı Bilgileri","Kullanım Tercihleri"])

with tab1:
    eposta=st.text_input(label="E posta adresini giriniz",type="default")
    sifre=st.text_input(label="Şifrenizi giriniz",type="password")
    st.checkbox(label="Şifremi unuttum")
    st.divider()
    kaydet_btn=st.button(label="İndir")

with tab2:
    hesap_turu=st.radio(label="Hesap Türü",options=["Öğrenci","Mezun"])
    st.slider("Tecrübe yılınız",min_value=3,max_value=30)
    st.file_uploader(label="Güncel özgeçmiş yükleyiniz")

if kaydet_btn:
    data=[]
    data.append({"eposta":eposta})
    data.append({"sifre":sifre})

    if hesap_turu=="Öğrenci":
        gecerlilik_suresi=365
    elif hesap_turu=="Mezun":
        gecerlilik_suresi=30
    
    data.append({"Geçerilik süresi":gecerlilik_suresi})

    with open("kullanici.txt","w",encoding="utf-8") as file:
        file.write(json.dumps(data))

    st.balloons()
    st.success("Dosyanız başarıyla indirildi.")
    st.write(f"Geçerlilik süresi :{gecerlilik_suresi}")