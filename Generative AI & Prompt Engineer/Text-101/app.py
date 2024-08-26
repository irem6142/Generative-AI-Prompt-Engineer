from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
my_key=os.getenv("api_key") #Api key ücretli :(
print(my_key)
client=OpenAI(api_key=my_key)

AI_Response=client.chat.completions.create(
       model="gpt-3.5-turbo-16k",
       temperature=0,
       max_tokens=256,
       messages=[
           {"role":"system","content":"Sen coğrafya öğretmenisin."},
           {"role":"user","content":"Mevsimler neden oluşur"}
       ]
)

print(AI_Response.choices[0].message.content)

