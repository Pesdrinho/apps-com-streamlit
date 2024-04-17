# Adicionar o chatbot e o formulário para envio de mensagens no Whatsapp

import streamlit as st
from openai import OpenAI
import dotenv

load_dotenv()

# Substitua 'YourKey' pela sua chave de API real
client = OpenAI(api_key=os.environ(OPENAI_API_KEY))
GPT_MODEL = "gpt-3.5-turbo"  # Alterado para o modelo GPT-4

def enviar_mensagem(mensagem, lista_mensagens):

    messages = [
        {"role": "system", "content": 'You are a secretary from a dentist that works from 8am to 6pm and is specialized in extractions and caries.'},
        {"role": "user", "content": mensagem},
    ]

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
        temperature=0
    )

    response_message = response.choices[0].message.content

    return response_message


st.title("Chatbot iCliniCall")

lista_mensagens = st.session_state.get("lista_mensagens", [])

texto = st.text_input("Escreva aqui sua mensagem:")

if st.button("Enviar"):
    if texto:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append({"role": "user", "content": texto})
        lista_mensagens.append({"role": "assistant", "content": resposta})

st.text("Conversa:")
for mensagem in lista_mensagens:
    if mensagem["role"] == "user":
        st.text(f"Usuário: {mensagem['content']}")
    elif mensagem["role"] == "assistant":
        st.text(f"Chatbot: {mensagem['content']}")

st.session_state["lista_mensagens"] = lista_mensagens