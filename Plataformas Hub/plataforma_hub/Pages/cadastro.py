import streamlit as st
import cliente as cliente
import Controllers.ClienteController as ClienteController

st.title("Cadastro de Usuário")

with st.form("form_cadastro"):
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    senha = st.text_input("Senha:", type="password")
    tipo = st.selectbox("Tipo de Usuário:", ['Dono de Problema', 'Dono de Solução', 'Profissional independente', 'Investidor'])

    submitted = st.form_submit_button("Cadastrar")

    if submitted:
        cliente.nome = nome
        cliente.email = email
        cliente.senha = senha
        cliente.tipo = tipo
        st.success(f"Cadastro realizado com sucesso! Obrigado pelo seu cadasto {cliente.nome}")

        ClienteController.IncluirCliente(cliente)



