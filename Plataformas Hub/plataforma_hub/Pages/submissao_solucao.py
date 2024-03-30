import streamlit as st

def submeter_solucao(descricao, area, complexidade, outras_opcoes):
    solucao = {
        'Descrição': descricao,
        'Área': area,
        'Nível de Complexidade': complexidade,
        'Outras Opções': outras_opcoes
    }
    return solucao

st.title("Submissão de Solução")

with st.form("form_submissao_solucao"):
    descricao_solucao = st.text_area("Descreva a sua Solução:")
    area_solucao = st.selectbox("Selecione a Área da Solução:", ["Tecnologia", "Saúde", "Educação", "Negócios", "Outro"])
    nivel_complexidade_solucao = st.selectbox("Selecione o Nível de Complexidade:", ["Alto", "Médio", "Baixo"])
    outras_opcoes_solucao = st.text_input("Outras Opções (se houver):")
    submitted = st.form_submit_button("Submeter Solução")

    if submitted:
        solucao_submetida = submeter_solucao(descricao_solucao, area_solucao, nivel_complexidade_solucao, outras_opcoes_solucao)
        st.success("Solução submetida com sucesso!")
        st.write("Detalhes da Solução:")
        st.write(solucao_submetida)

