import streamlit as st

import Pages.cadastro as cadastro
import Pages.submissao_solucao as solucoes
import Pages.submissao_problema as problemas
import Pages.contato as contato
import Pages.blog as blog

def main():
    st.title("Página Inicial")
    # st.set_page_config(page_title="Plataforma de IA")

    # usuarios = {}
    # solucoes = []
    # problemas = []

    # pages = {
    #     "Página Inicial": homepage,
    #     "Cadastro": cadastro,
    #     "Submissao Solucao": solucoes,
    #     "Submissao Problema": problemas,
    #     "Contato": contato,
    #     "Blog": blog,
    # }

    # selection = st.sidebar.radio("Navegar", list(pages.keys()))

    # # Adicionando o usuário completo como argumento nas funções correspondentes
    # if selection in ["Submissao Solucao", "Submissao Problema"]:
    #     email = st.sidebar.text_input("Digite seu email:")
    #     if email in usuarios:
    #         usuario = usuarios[email]
    #         pages[selection](usuario, solucoes if selection == "Submissao Solucao" else problemas)
    #     else:
    #         st.warning("Usuário não encontrado. Por favor, faça o cadastro.")
    # else:
    #     pages[selection]()

    # # Debug: Exibir dados armazenados
    # st.header("Dados Armazenados (Debug)")
    # st.write("Usuários:", usuarios)
    # st.write("Soluções:", solucoes)
    # st.write("Problemas:", problemas)

if __name__ == '__main__':
    main()



