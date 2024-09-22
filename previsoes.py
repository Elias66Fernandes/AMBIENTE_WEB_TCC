import streamlit as st
import joblib
import numpy as np
import pandas as pd

def run():
    
    # Valores máximos originais para normalização
    max_values = {
        'Num_acoes_Q1': 101,
        'Num_acoes_Q2': 51,
        'Avaliacao_de_Forum_1': 3,
        'Avaliacao_de_Forum_2': 3
    }
    
    # Função de normalização
    def normalizar(valor, coluna):
        if valor > max_values[coluna]:
            valor = max_values[coluna]  # Limita o valor ao máximo permitido
        return (valor / max_values[coluna]) * 100
    
    # Função para fazer previsões
    def fazer_previsao(model):
        
        input_df = pd.DataFrame(input_data, columns=['Teve_acao_Q1', 'Num_acoes_Q1', 'Teve_acao_Q2', 
                                                     'Num_acoes_Q2', 'Avaliacao_de_Forum_1', 'Avaliacao_de_Forum_2'])
        pred = model.predict(input_df)
        return pred[0]

    # Carregar os modelos salvos
    svm_model = joblib.load(open('models/SVM_k7_testsize20.pkl', 'rb'))
    decision_tree_model = joblib.load(open('models/Arvore_Decisao_k5_testsize10.pkl', 'rb'))
    naive_bayes_model = joblib.load(open('models/Naive_Bayes_k5_testsize40.pkl', 'rb'))
    neural_network_model = joblib.load(open('models/Rede_Neural_k10_testsize10.pkl', 'rb'))

    # Título da página
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
            margin-top: -50px;
            margin-bottom: 50px
        }
        </style>
        <h1 class='title'>Previsão de Desempenho do Aluno</h1>
        """, 
        unsafe_allow_html=True
    )

    # Divide a página em colunas
    col1, col2 = st.columns([2, 3])

    # Coluna para seleção de atributos
    with col1:
        st.header('Atributos do Aluno')
        
        num_acoes_q1 = st.slider('Número de Ações no Questionário 1', 0, 110, 0)
        teve_acao_q1 = 1 if num_acoes_q1 != 0 else 0
        num_acoes_q2 = st.slider('Número de Ações no Questionário 2', 0, 110, 0)
        teve_acao_q2 = 1 if num_acoes_q2 != 0 else 0
        avaliacao_forum_1 = st.slider('Participação no Fórum 1', 0, 110, 0)
        avaliacao_forum_2 = st.slider('Participação no Fórum 2', 0, 110, 0)

        # Entradas do usuário
        input_data = np.array([[teve_acao_q1, 
                                normalizar(num_acoes_q1, 'Num_acoes_Q1'), 
                                teve_acao_q2, 
                                normalizar(num_acoes_q2, 'Num_acoes_Q2'), 
                                normalizar(avaliacao_forum_1, 'Avaliacao_de_Forum_1'), 
                                normalizar(avaliacao_forum_2, 'Avaliacao_de_Forum_2')]])

    # Coluna para previsão e resultados
    with col2:
        st.header('Previsão')

        # Cria abas para cada modelo
        tab1, tab2, tab3, tab4 = st.tabs(["SVM", "Árvore de Decisão",
                                          "Naive Bayes", "Rede Neural"])

        with tab1:
            if st.button('Prever com SVM'):
                resultado = fazer_previsao(svm_model)
                st.image('src/Resultado_Aprovado.png' if resultado == 1 else 'src/Resultado_Reprovado.png')

        with tab2:
            if st.button('Prever com Árvore de Decisão'):
                resultado = fazer_previsao(decision_tree_model)
                st.image('src/Resultado_Aprovado.png' if resultado == 1 else 'src/Resultado_Reprovado.png')

        with tab3:
            if st.button('Prever com Naive Bayes'):
                resultado = fazer_previsao(naive_bayes_model)
                st.image('src/Resultado_Aprovado.png' if resultado == 1 else 'src/Resultado_Reprovado.png')

        with tab4:
            if st.button('Prever com Rede Neural'):
                resultado = fazer_previsao(neural_network_model)
                st.image('src/Resultado_Aprovado.png' if resultado == 1 else 'src/Resultado_Reprovado.png')

