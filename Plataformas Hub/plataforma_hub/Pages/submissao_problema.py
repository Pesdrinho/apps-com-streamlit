import streamlit as st

def submeter_problema(descricao, area, complexidade, outras_opcoes):
    problema = {
        'Descrição': descricao,
        'Área': area,
        'Nível de Complexidade': complexidade,
        'Outras Opções': outras_opcoes
    }
    return problema

st.title("Submissão de Problema")

with st.form("form_submissao_problema"):
    descricao_problema = st.text_area("Descreva o seu Problema:")
    area_problema = st.selectbox("Selecione a Área do Problema:", ["Tecnologia", "Saúde", "Educação", "Negócios", "Outro"])
    nivel_complexidade = st.selectbox("Selecione o Nível de Complexidade:", ["Alto", "Médio", "Baixo"])
    outras_opcoes = st.text_input("Outras Opções (se houver):")
    submitted = st.form_submit_button("Submeter Problema")

    if submitted:
        problema_submetido = submeter_problema(descricao_problema, area_problema, nivel_complexidade, outras_opcoes)
        st.success("Problema submetido com sucesso!")
        st.write("Detalhes do Problema:")
        st.write(problema_submetido)


