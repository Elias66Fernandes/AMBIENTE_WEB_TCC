import streamlit as st
import joblib
import numpy as np


def run():
    # Função para fazer previsões
    def fazer_previsao(model):
        pred = model.predict(input_data)
        return pred[0]

    # Carregar os modelos salvos
    svm_model = joblib.load(open('models/SVM_k7_testsize20.pkl', 'rb'))
    decision_tree_model = joblib.load(open('models/Arvore_Decisao_k5_testsize10.pkl', 'rb'))
    naive_bayes_model = joblib.load(open('models/Naive_Bayes_k5_testsize40.pkl', 'rb'))
    neural_network_model = joblib.load(open('models/Rede_Neural_k10_testsize10.pkl', 'rb'))

    # Título da página
    #st.title('Previsão de Desempenho do Aluno')
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

        teve_acao_q1 = st.selectbox('Teve Ação no Questionário 1?', ['Sim', 'Não'])
        num_acoes_q1 = st.slider('Número de Ações no Questionário 1', 0, 100, 0)
        teve_acao_q2 = st.selectbox('Teve Ação no Questionário 2?', ['Sim', 'Não'])
        num_acoes_q2 = st.slider('Número de Ações no Questionário 2', 0, 100, 0)
        avaliacao_forum_1 = st.slider('Participação no Fórum 1', 0, 100, 0)
        avaliacao_forum_2 = st.slider('Participação no Fórum 2', 0, 100, 0)

        if teve_acao_q1 == 'Sim':
            teve_acao_q1 = 1
        else:
            teve_acao_q1 = 0

        if teve_acao_q2 == 'Sim':
            teve_acao_q2 = 1
        else:
            teve_acao_q2 = 0

        # Entradas do user
        input_data = np.array([[teve_acao_q1, num_acoes_q1, teve_acao_q2,
                                num_acoes_q2, avaliacao_forum_1, avaliacao_forum_2]])

    # Coluna para previsão e resultados
    with col2:
        st.header('Previsão')

        # Cria abas para cada modelo
        tab1, tab2, tab3, tab4 = st.tabs(["SVM", "Árvore de Decisão",
                                        "Naive Bayes", "Rede Neural"])

        with tab1:
            if st.button('Prever com SVM'):
                resultado = fazer_previsao(svm_model)
                if resultado == 1:
                    st.image('src/Resultado_Aprovado.png')
                else:
                    st.image('src/Resultado_Reprovado.png')
        with tab2:
            if st.button('Prever com Árvore de Decisão'):
                resultado = fazer_previsao(decision_tree_model)
                if resultado == 1:
                    st.image('src/Resultado_Aprovado.png')
                else:
                    st.image('src/Resultado_Reprovado.png')

        with tab3:
            if st.button('Prever com Naive Bayes'):
                resultado = fazer_previsao(naive_bayes_model)
                if resultado == 1:
                    st.image('src/Resultado_Aprovado.png')
                else:
                    st.image('src/Resultado_Reprovado.png')

        with tab4:
            if st.button('Prever com Rede Neural'):
                resultado = fazer_previsao(neural_network_model)
                if resultado == 1:
                    st.image('src/Resultado_Aprovado.png')
                else:
                    st.image('src/Resultado_Reprovado.png')
