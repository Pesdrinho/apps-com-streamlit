import streamlit as st
import requests

def send_message(numero):
    # Substitua os valores apropriados aqui
    access_token = 'EAATonZCKARZAIBO5rLVzTKo3qnD8KEN3ygEgaQj6Yb2fSutAjdki57xQsPJNKLSKRrvwZBVZAj74Voi3iNaZA5VGiWsYssWQeWecKMHt3eoK2EPQSpMse005JINJpVvEjgIUyDS0ZCCUOu51XUlGx2p66GsxfJr7iJjOlb4qwOx1tiGHZAG2tZA5Rg98MhFyV9it3fVSSRrJdDfHFUFAX8xnQ1j6sOELTXNuv1wn19SkTVAZD'
    recipient_number = numero

    # Monta a URL e os dados para a chamada cURL
    url = 'https://graph.facebook.com/v18.0/187570044430709/messages'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    payload = {
        'messaging_product': 'whatsapp',
        'to': recipient_number,
        'type': 'template',
        'template': {
            'name': 'flight_confirmation_message',
            'language': {
                'code': 'pt_BR'
            }
        }
    }

    # Faz a chamada para enviar a mensagem ao WhatsApp
    response = requests.post(url, headers=headers, json=payload)

    # Verifica a resposta da chamada
    if response.status_code == 200:
        return 'Mensagem enviada com sucesso!'
    else:
        return f'Falha ao enviar a mensagem - Status: {response.status_code}'

# Função para enviar mensagem via WhatsApp
def send_whatsapp_message():
    # Substitua 'SEU_NUMERO_DE_TELEFONE' pelo número de telefone desejado
    recipient_phone_number = '5562999971740'

    # Substitua 'SUA_MENSAGEM' pela mensagem desejada
    message = 'Olá! Gostaria de suporte'

    # Abre o link do WhatsApp com o número, o token e a mensagem
    whatsapp_link = f'https://wa.me/{recipient_phone_number}'
    return whatsapp_link

# Interface do Streamlit
st.title("Formulário de Autorização WhatsApp")

# Formulário
with st.form("authorization_form"):
    # Campo de entrada para o número de telefone
    phone_number = st.text_input("Número de Telefone", help="Digite seu número de telefone")

    # Checkbox para autorização
    authorization_checkbox = st.checkbox("Autorizar o envio de mensagens via WhatsApp")

    # Botão para enviar o formulário
    submit_button = st.form_submit_button("Enviar")

# Processamento do formulário ao clicar no botão
if submit_button:
    # Verificar se a checkbox de autorização está marcada
    if authorization_checkbox:
        # Enviar mensagem via WhatsApp
        whatsapp_link = send_whatsapp_message()
        st.success(f'Formulário enviado! Clique no link abaixo para enviar a mensagem via WhatsApp.')
        st.markdown(f"[**Iniciar Conversa no WhatsApp**]({whatsapp_link})")
        st.success(send_message(phone_number))
    else:
        st.error("Você precisa autorizar o envio de mensagens via WhatsApp marcando a checkbox.")

