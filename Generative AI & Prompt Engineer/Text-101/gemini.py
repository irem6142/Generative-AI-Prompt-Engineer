import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

my_key=os.getenv("gemini_api")

genai.configure(
    api_key=my_key
)

client=genai.GenerativeModel(model_name="gemini-pro")
def generate_response(prompt):
    chat=client.start_chat(history=[])

    AI_Response=chat.send_message(
     prompt,
     generation_config=genai.GenerationConfig(
         temperature=0.9,
         max_output_tokens=256
     )
)
    return AI_Response.text


st.header("Gemini ile ilk botum")
st.divider()

prompt=st.text_input("Mesajınızı giriniz")
submit_btn=st.button("Gönder")

if submit_btn:
    response=generate_response(prompt)
    st.markdown(response)


    
# client=genai.GenerativeModel(
#     model_name="gemini-pro"
# )
# AI_Response=client.generate_content(
#      "Mevsimler neden oluşur?",
#         generation_config=genai.GenerationConfig(
#         tempature=0.9,
#         max_output_tokens=256
#     )
# )

# print(AI_Response.text)