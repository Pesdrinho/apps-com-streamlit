import streamlit as st
from openai import OpenAI

client = OpenAI(api_key='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')
GPT_MODEL = "gpt-3.5-turbo"

def generate_insights(mensagem):

    messages = [
        {"role": "system", "content": 'You are a marketing specialist and need to provide useful informations to your customers about how to increase their influence on social media'},
        {"role": "user", "content": f"Me ofereça insights (em formato de tópicos) em relação a seguinte às seguintes necessidades: {mensagem}"},
    ]

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
        temperature=0
    )

    response_message = response.choices[0].message.content

    return response_message

# Interface do Streamlit
st.title("Página de Marketing")

# Formulário para selecionar redes sociais e automações
st.header("Formulário para Selecionar Redes Sociais e Automações")
selected_social_media = st.multiselect("Selecione as redes sociais", ["WhatsApp", "Instagram", "Twitter", "Facebook"])
selected_automations = st.checkbox("Responder Comentários")
selected_automations += st.checkbox("Enviar Promoções")
selected_automations += st.checkbox("Enviar Directs")

# Formulário para enviar possibilidades de automações
st.header("Formulário para Envio de Possibilidades de Automações")
possibilities_form = st.form(key="possibilities_form")
possibility = possibilities_form.text_area("Digite suas possibilidades de automações")
possibilities_submit_button = possibilities_form.form_submit_button("Enviar Possibilidades")

# Processamento do formulário de possibilidades ao clicar no botão
if possibilities_submit_button:
    st.success(f"Possibilidades enviadas: {possibility}")

# Formulário para gerar insights usando o ChatGPT
st.header("Gerar Insights de Automações")
# insights_form = st.form(key="insights_form")
# insights_prompt = insights_form.text_area("Digite um prompt para gerar insights")
# insights_submit_button = insights_form.form_submit_button("Gerar Insights")
insights_submit_button = st.button("Gerar Insights")

# Processamento do formulário de insights ao clicar no botão
if insights_submit_button:
    generated_insights = generate_insights('Gere possibilidades de processos dentro de redes sociais que podem ser alvo de automações de marketing digital, usando ferramentas de IA ou automação de processos. Ofereça opções de ferramentas para cada uma das possibilidades apresentadas. Faça isso da maneira mais sucinta possível.')
    st.success(f"Insights Gerados:\n{generated_insights}")

# Formulário para automações adicionais
st.header("Formulário para Automações Adicionais")
additional_automations_form = st.form(key="additional_automations_form")
additional_automations = additional_automations_form.text_area("Digite automações adicionais")
additional_automations_submit_button = additional_automations_form.form_submit_button("Adicionar Automações")

# Processamento do formulário de automações adicionais ao clicar no botão
if additional_automations_submit_button:
    st.success(f"Automações Adicionais:\n{additional_automations}")
