import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def run():
    
    data = pd.read_csv('resultados_modelos.csv')
    
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
            margin-top: -50px;
            margin-bottom: 50px
        }
        </style>
        <h1 class='title'>Sobre a Construção dos Modelos</h1>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("""
    <div style="text-align: justify; text-justify: inter-word; margin-left: auto; margin-right: auto; width: 80%;">
        Os dados da plataforma de ensino foram organizados em arquivos CSV separados, que foram convertidos em um único
        DataFrame utilizando a biblioteca pandas. Para isso, foi necessário correlacionar as tabelas utilizando o nome e
        e-mail dos alunos como chaves primárias, resultando em um conjunto de dados com 161 registros e 24 atributos. Esses
        atributos foram classificados em três categorias principais: Informações Pessoais e de Identificação, Interações no AVA,
        e Atividades Avaliativas e Desempenho. O foco do projeto está nas interações dos alunos com o AVA, como participação em fóruns
        e ações em questionários, buscando entender o impacto dessas atividades no desempenho acadêmico e nas taxas de aprovação e reprovação.
        <br></br>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(
    """
    <style>
    .subtitulo {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px;
        font-size: 26px;
    }
    .texto {
        text-align: justify;
        margin: 0 auto;
        width: 80%;
    }
    </style>
    <h2 class='subtitulo'>Pré-processamento e seleção de atributos</h2>
    <div class='texto'>
        A etapa de pré-processamento dos dados é crucial para garantir que eles sejam
        adequados para análise e aprendizado de máquina. Isso incluiu a limpeza, normalização
        e codificação de variáveis categóricas, visando simplificar o conjunto de dados e remover
        atributos irrelevantes. Para preservar a privacidade dos alunos, todas as informações pessoais,
        como nome e e-mail, foram removidas, em conformidade com a Lei Geral de Proteção de Dados (LGPD).
        <br><br>
        Foi criada uma nova coluna chamada "Status", que indica se o aluno foi aprovado ou reprovado,
        com base na nota final: alunos com nota final maior ou igual a 7 foram aprovados; se fizeram prova
        de reposição e obtiveram nota final maior ou igual a 6, também foram aprovados; caso contrário, foram reprovados.
        Algumas colunas foram renomeadas e codificadas com indicadores binários para facilitar a análise posterior. E as colunas
        com características avaliativas (notas e atividades avaliativas), foram removidas do DataFrame.
        <br><br>
        Para mais, também foi feita a normalização dos dados utilizados nos na criação de modelos preditivos.
        A normalização utilizada neste projeto  foi uma variação da min-max,
        que ao invés dos valores variarem de entre -1 e 1, eles variam de 0 à 100.
        <br><br>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(
    """
    <style>
    .subtitulo {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px;
        font-size: 26px;
    }
    .texto {
        text-align: justify;
        margin: 0 auto;
        width: 80%;
    }
    </style>
    <h2 class='subtitulo'>Treinamento e Otimização dos Modelos</h2>
    <div class='texto'>
        Os atributos escolhidos para o treinamento foram: Teve_acao_Q1, Num_acoes_Q1, Teve_acao_Q2,
        Num_acoes_Q2, Avaliacao_de_Forum_1 e Avaliacao_de_Forum_2, com o atributo alvo sendo o Status,
        codificado como binário (1 para aprovado e 0 para reprovado). Um conjunto de validação de 20% dos
        dados foi criado de forma aleatória, preservando o desbalanceamento de classes.
        <br><br>
        Para equilibrar os dados de treinamento, foi utilizada a técnica SMOTE (Synthetic Minority Over-sampling Technique),
        que gera novas instâncias sintéticas da classe minoritária. Foram experimentados tamanhos de
        conjuntos de teste de 10%, 20%, 30% e 40% dos dados.
        <br><br>
        Além disso, aplicou-se validação cruzada do tipo K-fold, com 5 a 10 folds, combinados com diferentes test-sizes para
        gerar vários modelos. Para otimizar os hiperparâmetros, utilizou-se a técnica GridSearchCV, onde a métrica de avaliação
        usada foi o f1-score, selecionando a melhor combinação de parâmetros para os modelos.
        <br><br>
    </div>
    """, unsafe_allow_html=True)
    
    
    st.markdown(
    """
    <style>
    .subtitulo {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px;
        font-size: 26px;
    }
    .texto {
        text-align: justify;
        margin: 0 auto;
        width: 80%;
    }
    </style>
    <h2 class='subtitulo'>Modelos Usados e Resultados</h2>
    <div class='texto'>
        As Tabelas apresentam os resultados obtidos durante o treinamento e a validação
        dos modelos. As métricas registradas incluem a acurácia no treinamento, o número
        de folds utilizados no K-fold, o tamanho do test-size e a acurácia da validação que 
        foi a principal métrica utilizada para a seleção dos melhores modelos de cada.
        <br><br>
    </div>
    """, unsafe_allow_html=True)
    
    # Cria abas para cada modelo
    tab1, tab2, tab3, tab4 = st.tabs(["SVM", "Árvore de Decisão",
                                      "Naive Bayes", "Rede Neural"])

    with tab1:
        
        valor_especifico = 'modelos_salvos\SVM_k7_testsize20.pkl'

        # Filtra os dados para o valor específico
        dados_selecionados = data[data['model_path'] == valor_especifico]

        # Exibir os dados
        if not dados_selecionados.empty:
            # Exibir cada coluna separadamente
            st.write('Modelo:', dados_selecionados['modelo'].values[0])
            st.write('K-Fold:', dados_selecionados['kfold'].values[0])
            st.write('Test Size:', dados_selecionados['test_size'].values[0])
            st.write('Melhores Parâmetros:', dados_selecionados['best_params'].values[0])
            st.write('Acurácia do Treinamento:', dados_selecionados['accuracy'].values[0])
            st.write('Acurácia da Validação: 1.0')
            
            st.write('Relatório de Classificação Do Treinamento:')
            st.text(dados_selecionados['classification_report'].values[0])
            
            
            st.write('Matriz de Confusão:')
            
 
            confusion_matrix_str = dados_selecionados['confusion_matrix'].values[0].strip()
            
            # Verificar e corrigir a formatação
            st.write('Valor da matriz de confusão como string:', confusion_matrix_str)
            
            confusion_matrix = [[ 5, 0],[ 6, 15]]
        
            # Configurar a matriz de confusão
            plt.figure(figsize=(9, 6))
            sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues',
                        xticklabels=['Reprovado (0)', 'Aprovado (1)'],
                        yticklabels=['Reprovado (0)', 'Aprovado (1)'])
            plt.xlabel('Previsto')
            plt.ylabel('Real')
            plt.title('Matriz De Confusão')
            
            # Mostrar a figura no Streamlit
            st.pyplot(plt)
        else:
            st.write('Nenhum dado encontrado para o modelo.')
                    
    with tab2:
        
        valor_especifico = 'modelos_salvos\Arvore_Decisao_k5_testsize10.pkl'

        # Filtra os dados para o valor específico
        dados_selecionados = data[data['model_path'] == valor_especifico]

        # Exibir os dados
        if not dados_selecionados.empty:
            # Exibir cada coluna separadamente
            st.write('Modelo:', dados_selecionados['modelo'].values[0])
            st.write('K-Fold:', dados_selecionados['kfold'].values[0])
            st.write('Test Size:', dados_selecionados['test_size'].values[0])
            st.write('Melhores Parâmetros:', dados_selecionados['best_params'].values[0])
            st.write('Acurácia do Treinamento:', dados_selecionados['accuracy'].values[0])
            st.write('Acurácia da Validação: 1.0')
            
            st.write('Relatório de Classificação Do Treinamento:')
            st.text(dados_selecionados['classification_report'].values[0])
            
            
            st.write('Matriz de Confusão:')
            
 
            confusion_matrix_str = dados_selecionados['confusion_matrix'].values[0].strip()
            
            # Verificar e corrigir a formatação
            st.write('Valor da matriz de confusão como string:', confusion_matrix_str)
            
            confusion_matrix = [[2,0],[2,9]]
        
            # Configurar a matriz de confusão
            plt.figure(figsize=(9, 6))
            sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues',
                        xticklabels=['Reprovado (0)', 'Aprovado (1)'],
                        yticklabels=['Reprovado (0)', 'Aprovado (1)'])
            plt.xlabel('Previsto')
            plt.ylabel('Real')
            plt.title('Matriz De Confusão')
            
            # Mostrar a figura no Streamlit
            st.pyplot(plt)
        else:
            st.write('Nenhum dado encontrado para o modelo.')

    with tab3:
        
        valor_especifico = 'modelos_salvos\\Naive_Bayes_k5_testsize40.pkl'

        # Filtra os dados para o valor específico
        dados_selecionados = data[data['model_path'] == valor_especifico]

        # Exibir os dados
        if not dados_selecionados.empty:
            # Exibir cada coluna separadamente
            st.write('Modelo:', dados_selecionados['modelo'].values[0])
            st.write('K-Fold:', dados_selecionados['kfold'].values[0])
            st.write('Test Size:', dados_selecionados['test_size'].values[0])
            st.write('Melhores Parâmetros:', dados_selecionados['best_params'].values[0])
            st.write('Acurácia do Treinamento:', dados_selecionados['accuracy'].values[0])
            st.write('Acurácia da Validação: 1.0')
            
            st.write('Relatório de Classificação Do Treinamento:')
            st.text(dados_selecionados['classification_report'].values[0])
            
            
            st.write('Matriz de Confusão:')
            
 
            confusion_matrix_str = dados_selecionados['confusion_matrix'].values[0].strip()
            
            # Verificar e corrigir a formatação
            st.write('Valor da matriz de confusão como string:', confusion_matrix_str)
            
            confusion_matrix = [[ 9, 5], [ 2, 36]]
        
            # Configurar a matriz de confusão
            plt.figure(figsize=(9, 6))
            sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues',
                        xticklabels=['Reprovado (0)', 'Aprovado (1)'],
                        yticklabels=['Reprovado (0)', 'Aprovado (1)'])
            plt.xlabel('Previsto')
            plt.ylabel('Real')
            plt.title('Matriz De Confusão')
            
            # Mostrar a figura no Streamlit
            st.pyplot(plt)
        else:
            st.write('Nenhum dado encontrado para o modelo.')

    with tab4:
        valor_especifico = 'modelos_salvos\Rede_Neural_k10_testsize10.pkl'

        # Filtra os dados para o valor específico
        dados_selecionados = data[data['model_path'] == valor_especifico]

        # Exibir os dados
        if not dados_selecionados.empty:
            # Exibir cada coluna separadamente
            st.write('Modelo:', dados_selecionados['modelo'].values[0])
            st.write('K-Fold:', dados_selecionados['kfold'].values[0])
            st.write('Test Size:', dados_selecionados['test_size'].values[0])
            st.write('Melhores Parâmetros:', dados_selecionados['best_params'].values[0])
            st.write('Acurácia do Treinamento:', dados_selecionados['accuracy'].values[0])
            st.write('Acurácia da Validação: 0.96')
            
            st.write('Relatório de Classificação Do Treinamento:')
            st.text(dados_selecionados['classification_report'].values[0])
            
            
            st.write('Matriz de Confusão:')
            
 
            confusion_matrix_str = dados_selecionados['confusion_matrix'].values[0].strip()
            
            # Verificar e corrigir a formatação
            st.write('Valor da matriz de confusão como string:', confusion_matrix_str)
            
            confusion_matrix = [[ 1,1],[ 0,11]]
        
            # Configurar a matriz de confusão
            plt.figure(figsize=(9, 6))
            sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues',
                        xticklabels=['Reprovado (0)', 'Aprovado (1)'],
                        yticklabels=['Reprovado (0)', 'Aprovado (1)'])
            plt.xlabel('Previsto')
            plt.ylabel('Real')
            plt.title('Matriz De Confusão')
            
            # Mostrar a figura no Streamlit
            st.pyplot(plt)
        else:
            st.write('Nenhum dado encontrado para o modelo.')