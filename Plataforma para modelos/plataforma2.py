import streamlit as st
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("https://drive.google.com/uc?id=1bTQLgA-6_iw9llnEo59WNe_fm7uq83Bu")

features = df.drop('Y', axis=1)
target = df['Y']

# # Alterando o label para -1 e 1
# df['Y'] = df['Y'].apply(lambda x: 1 if x == 'Up' else -1 if x == 'Down' else x )

# # normalizando o ano
# scaler = MinMaxScaler(feature_range=(-2, 2))
# df['Ano'] = scaler.fit_transform(df[['Ano']].values)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

features = df[['Ano', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']]
target = df['Y']

# melhores parâmetros para cada modelo
lda_best_params = {'param0': 0.5512338032847833, 'param1': 0.6652880993776471, 'param2': 0.1599488915094367, 'param3': 0.7661040636049521}
qda_best_params = {'param0': 0.5675430372376934, 'param1': 0.4280759340305544, 'param2': 0.46712758465432114, 'param3': 0.971130269611102}

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
modelo_lda = LinearDiscriminantAnalysis().fit(X_train, y_train)
modelo_qda = QuadraticDiscriminantAnalysis().fit(X_train, y_train)
modelo_nb = GaussianNB().fit(X_train, y_train)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Função para realizar a predição e calcular métricas
def prever_e_calcular_metricas(modelo, entrada_usuario):
    previsao = modelo.predict(entrada_usuario)
    probabilidade_acerto = None
    
    # Verifica se o modelo tem a função predict_proba (apenas para alguns modelos)
    if hasattr(modelo, 'predict_proba'):
        probabilidade_acerto = modelo.predict_proba(entrada_usuario)
    
    return previsao, probabilidade_acerto

# Interface gráfica usando Streamlit
st.title('Predição e Avaliação de Modelos')

# Seção para entrada de dados
st.sidebar.header('Entrada de Dados')
# Adapte isso para as features do seu conjunto de dados
ano = st.sidebar.number_input('Ano', min_value=2001.0, max_value=2005.0, step=1.0, value=2003.0)
x1 = st.sidebar.number_input('X1', min_value=-4.0, max_value=4.0, step=0.1, value=0.0)
x2 = st.sidebar.number_input('X2', min_value=-4.0, max_value=4.0, step=0.1, value=0.0)
x3 = st.sidebar.number_input('X3', min_value=-4.0, max_value=4.0, step=0.1, value=0.0)
x4 = st.sidebar.number_input('X4', min_value=-4.0, max_value=4.0, step=0.1, value=0.0)
x5 = st.sidebar.number_input('X5', min_value=-4.0, max_value=4.0, step=0.1, value=0.0)
x6 = st.sidebar.number_input('X6', min_value=-4.0, max_value=4.0, step=0.1, value=0.0)
x7 = st.sidebar.number_input('X7', min_value=-4.0, max_value=4.0, step=0.1, value=0.0)

# Adapte isso para o seu conjunto de dados
entrada_usuario = pd.DataFrame({'Ano': [ano], 'X1': [x1], 'X2': [x2], 'X3': [x3], 'X4': [x4], 'X5': [x5], 'X6': [x6], 'X7': [x7]})

# Seção para exibir os dados de entrada do usuário
st.sidebar.header('Dados de Entrada do Usuário')
st.sidebar.write(entrada_usuario)

# Botão para realizar predições e exibir métricas
if st.sidebar.button('Realizar Predições e Avaliar Modelos'):
    # Realiza as predições com cada modelo
    previsao_lda, probabilidade_lda = prever_e_calcular_metricas(modelo_lda, entrada_usuario)
    previsao_qda, probabilidade_qda = prever_e_calcular_metricas(modelo_qda, entrada_usuario)
    previsao_nb, probabilidade_nb = prever_e_calcular_metricas(modelo_nb, entrada_usuario)

    # Exibe resultados
    st.subheader('Resultados da Predição e Avaliação dos Modelos')
    
    st.write('### LDA')
    st.write(f'Predição: {previsao_lda[0]}')
    if probabilidade_lda is not None:
        st.write(f'Probabilidade de Acréscimo: {probabilidade_lda[0][1]:.4f}')
        st.write(f'Melhores parâmetros: {lda_best_params}')

    st.write('### QDA')
    st.write(f'Predição: {previsao_qda[0]}')
    if probabilidade_qda is not None:
        st.write(f'Probabilidade de Acréscimo: {probabilidade_qda[0][1]:.4f}')
        st.write(f'Melhores parâmetros: {qda_best_params}')

    st.write('### Naive Bayes')
    st.write(f'Predição: {previsao_nb[0]}')
    if probabilidade_nb is not None:
        st.write(f'Probabilidade de Acréscimo: {probabilidade_nb[0][1]:.4f}')
