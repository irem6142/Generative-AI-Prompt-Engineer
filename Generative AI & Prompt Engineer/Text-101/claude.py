import os
import anthropic 
from dotenv import load_dotenv,find_dotenv
import streamlit as st


load_dotenv()
my_key=os.environ.get("anthropic_key")

client=anthropic.Anthropic(api_key=my_key)

model_name= "claude-3-haiku-20240307"


if "messages" not in st.session_state:
    st.session_state.messages=[]
    st.session_state.messages.append({"role":"system","content":"Sen komik yardımsever bir botsun."})

def generate_response(prompt):

    AI_Response=client.messages.create(
        model=model_name,
        temperature=0.9,
        max_tokens=256,
        messages=[
            {
                "role":"user","content":prompt
            }
        ]

    )
    return AI_Response.content[0].text

import streamlit as st

st.header("Claude ile ilk botum")
st.divider()

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt :=st.chat_input("Mesajınızı giriniz"):
    st.chat_message("user").markdown(prompt)
    response=generate_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role":"assistant","content":response})

   


