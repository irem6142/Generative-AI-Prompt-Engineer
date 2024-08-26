from openai import OpenAI
import requests
import streamlit as st
import os
from dotenv import load_dotenv
import base64
import openai

# Çevre değişkenlerini yükle
load_dotenv()

# API anahtarlarını al
my_key_stability = os.getenv("stability_key")
my_api = os.getenv("api_key")

# OpenAI istemcisini oluştur
openai.api_key = my_api

# DALL-E 3 ile görsel üretimi Fonksiyonu
def generate_with_DALL_E(prompt):
    try:
        AI_Response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            n=1,
            response_format="url"
        )
        # DALL-E API yanıtından URL'yi döndür
        image_url = AI_Response['data'][0]['url']
        return image_url
    except Exception as e:
        st.error(f"DALL-E API isteği başarısız oldu: {str(e)}")
        return None

# DALL-E 3 ile görsel varyasyonu oluşturma Fonksiyonu
def create_variation(image_file):
    try:
        # Görseli base64 formatında encode et
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
        AI_Response = openai.Image.create_variation(
            image=image_base64,
            n=1
        )
        # Varyasyonların URL'lerini döndür
        image_url = AI_Response['data'][0]['url']
        return image_url
    except Exception as e:
        st.error(f"DALL-E varyasyon isteği başarısız oldu: {str(e)}")
        return None

# Stable Diffusion Görsel Üretimi Fonksiyonu
def generate_with_SD(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_key_stability}"
    }
    body = {
        "steps": 40,
        "width": 1024,
        "height": 1024,
        "seed": 42,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": prompt,
                "weight": 1
            },
            {
                "text": "blurry,bad",
                "weight": -1
            }
        ]
    }
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Stable Diffusion API isteği başarısız oldu: {response.status_code} - {response.text}")
        return None

# Streamlit Uygulaması
tab_generation, tab_variation, sd_tabs = st.tabs(["Fotoğraf Üret", "Varyasyon Oluştur", "Stable Diffusion"])

with tab_generation:
    st.subheader("DALL-E 3 ile görsel Oluşturma")
    st.divider()
    prompt_dalle = st.text_input("Oluşturmak istediğiniz görseli tarif ediniz", key="dalle_prompt")
    generate_btn_dalle = st.button("Oluştur", key="dalle_btn")

    if generate_btn_dalle and prompt_dalle:
        image_url = generate_with_DALL_E(prompt_dalle)
        if image_url:
            st.image(image_url)

with tab_variation:
    st.subheader("DALL-E 3 ile görsel varyasyonu Oluşturma")
    st.divider()
    selected_file = st.file_uploader("Png formatındaki görseli yükleyiniz.", type=["png"])
    variation_btn = st.button("Varyasyon oluştur", key="variation_btn")

    if variation_btn and selected_file:
        image_url = create_variation(selected_file)
        if image_url:
            st.image(image_url)

with sd_tabs:
    st.subheader("Stable Diffusion görsel Oluşturma")
    st.divider()
    prompt_sd = st.text_input("Oluşturmak istediğiniz görseli tarif ediniz", key="sd_prompt")
    generate_btn_sd = st.button("Oluştur", key="sd_btn")

    if generate_btn_sd and prompt_sd:
        data_sd = generate_with_SD(prompt_sd)
        if data_sd:
            for image in data_sd.get("artifacts", []):
                if "base64" in image:
                    image_byte = base64.b64decode(image["base64"])
                    st.image(image_byte)
