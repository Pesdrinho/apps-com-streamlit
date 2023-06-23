import streamlit as st
import pandas as pd
import joblib
import pickle

# Carregar o modelo de Machine Learning
analise_credito = joblib.load(r"C:\Users\Pepson\Desktop\analise_credito.pkl")

# Configurar a identidade visual
primary_color = '#6E0C6D'
background_color = '#000000'
text_color = '#FFFFFF'

# Definir as configurações da página
st.set_page_config(
    page_title='Análise de Crédito',
    page_icon=':money_with_wings:',
    layout='centered',
    initial_sidebar_state='auto',
)

# Definir o estilo CSS customizado
custom_css = f"""
<style>
body {{
    color: {text_color};
    background-color: {background_color};
}}
.stButton button,
.stTextInput input,
.stSelectbox select,
.stTextArea textarea {{
    color: {text_color} !important;
    background-color: {primary_color} !important;
    border-color: {primary_color} !important;
}}
.stButton button:hover,
.stTextInput input:hover,
.stSelectbox select:hover,
.stTextArea textarea:hover {{
    background-color: {primary_color} !important;
    filter: brightness(1.2) !important;
}}
.stButton button:active,
.stTextInput input:active,
.stSelectbox select:active,
.stTextArea textarea:active {{
    background-color: {primary_color} !important;
    filter: brightness(0.8) !important;
}}
.stTextInput input:focus,
.stSelectbox select:focus,
.stTextArea textarea:focus {{
    background-color: {primary_color} !important;
    box-shadow: none !important;
}}
.stButton button:focus {{
    background-color: {primary_color} !important;
    box-shadow: 0 0 0 0.2rem rgba(110, 12, 109, 0.25) !important;
    outline: none !important;
}}
.stProgress > div > div > div > div {{
    background-color: {primary_color} !important;
}}
</style>
"""

# Aplicar o estilo customizado
st.markdown(custom_css, unsafe_allow_html=True)

# Título da aplicação
st.title('Análise de Crédito')

# Criar o formulário
idade = st.number_input('Idade', min_value=18, max_value=100, value=30)
renda = st.number_input('Renda Anual', min_value=0, value=50000)
tipo_residencia = st.selectbox('Tipo de Residência', ['Aluguel', 'Própria', 'Outra'])
tempo_emprego = st.number_input('Tempo no Emprego (em anos)', min_value=0, value=2)
motivacao_emprestimo = st.selectbox('Motivação do Empréstimo', ['Pessoal', 'Educação', 'Saúde', 'Outra'])
valor_emprestimo = st.number_input('Valor do Empréstimo', min_value=0, value=10000)
taxa_juros = st.number_input('Taxa de Juros', min_value=0.0, value=0.05)
status_emprestimo = st.selectbox('Status do Empréstimo', ['Aprovado', 'Negado'])
historico_nao_pagamento = st.selectbox('Histórico de Não Pagamentos', ['S', 'N'])
tempo_historico_credito = st.number_input('Tempo de Histórico de Crédito (em anos)', min_value=0, value=5)

# Botão para fazer a previsão
if st.button('Verificar Crédito'):
    # Criar um DataFrame com os dados inseridos pelo usuário
    dados = pd.DataFrame({
        'Idade': [idade],
        'Renda Anual': [renda],
        'Tipo de Residência': [tipo_residencia],
        'Tempo no Emprego': [tempo_emprego],
        'Motivação do Empréstimo': [motivacao_emprestimo],
        'Valor do Empréstimo': [valor_emprestimo],
        'Taxa de Juros': [taxa_juros],
        'Status do Empréstimo': [status_emprestimo],
        'Histórico de Não Pagamentos': [historico_nao_pagamento],
        'Tempo de Histórico de Crédito': [tempo_historico_credito]
    })

    # Fazer a previsão usando o modelo de Machine Learning
    resultado = analise_credito.predict(dados)

    # Exibir o resultado
    if resultado[0] == 1:
        st.success('Crédito Liberado!')
    else:
        st.error('Crédito Negado!')

if __name__ == '__main__':
    # Obtém a porta configurada para o servidor Streamlit
    porta = st.server.port

    # Escreve o link local na interface do Streamlit
    st.write(f"Acesse o aplicativo em: http://localhost:{porta}")