# Generative AI & Prompt Engineer - Projeler

Bu repository, **Generative AI & Prompt Engineer** eğitimim sürecinde geliştirdiğim projeleri ve uygulamaları içerir. Eğitimde, çeşitli yapay zeka tekniklerini kullanarak görsel üretme, metin tabanlı işlemler ve chatbot geliştirme üzerine çalışmalar yaptım.

## Projeler

### 1. Görsel Üretme Uygulaması

Bu proje, iki farklı yapay zeka modelini kullanarak görsel üretme işlevselliği sağlar:

- **DALL-E 3**: OpenAI'nin DALL-E 3 modelini kullanarak metin tabanlı görsel üretimi sağlar.
- **Stable Diffusion**: Stability AI'nin Stable Diffusion modelini kullanarak görsel üretimi sağlar.

#### Kullanım

1. **DALL-E 3 ile Görsel Oluşturma**: 
   - Metin tabanlı bir açıklama girerek yüksek kaliteli görseller oluşturabilirsiniz.
   - Kodu kullanarak API'den görsel URL'sini alabilir ve görüntüyü kullanıcıya gösterebilirsiniz.

2. **Stable Diffusion ile Görsel Oluşturma**:
   - Metin tabanlı bir açıklama girerek görsel oluşturabilirsiniz.
   - Görsel, base64 formatında döner ve Streamlit ile görseli görüntüleyebilirsiniz.


### 3. Chatbot

Bu proje, Streamlit ile geliştirilmiş bir chatbot uygulamasını içerir. Kullanıcılar, metin tabanlı sohbetler gerçekleştirebilir ve yapay zeka destekli cevaplar alabilir.

#### Özellikler

- Kullanıcıların metin tabanlı sorularını alır ve yapay zeka tarafından işlenen cevaplar sağlar.
- Streamlit ile kullanıcı dostu bir arayüz sunar.

## Kurulum

1. Gereksinimleri yükleyin:

    ```bash
    pip install streamlit openai requests python-dotenv
    ```

2. `.env` dosyanızda API anahtarlarınızı tanımlayın:

    ```env
    stability_key=YOUR_STABILITY_API_KEY
    api_key=YOUR_OPENAI_API_KEY
    ```

3. Streamlit uygulamasını başlatın:

    ```bash
    streamlit run app.py
    ```







https://github.com/user-attachments/assets/dc8ae601-7df8-48cb-a733-88a8e9b2a7b2

