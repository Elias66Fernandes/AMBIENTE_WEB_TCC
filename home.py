import streamlit as st

def run():
    
    col1, col2, col3  = st.columns([1, 4, 1])

    # Exibir a imagem na coluna central e ajustar o tamanho
    with col2:
        st.markdown(
        """
        <style>
        .title-page {
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 18px;
            margin-bottom: 50px
        }
        .subtitle {
            font-size: 16px;
            font-weight: bold;
        }
        .authors {
            font-size: 16px;
            font-weight: bold;
        }
        .text {
            font-size: 16px;
            margin-top: 20px;
        }
        .university {
            font-size: 35px;
            font-weight: bold;
        }
        </style>
        <div class="title-page">
            <div class="university">Universidade Federal do Maranhão</div>
            <div class="subtitle">Trabalho de Conclusão de Curso</div>
            <div class="authors">Francisco Elias da Silva Fernandes</div>
            <div class="authors">Rosivânia da Silva Viana</div>  
        </div>
        """,
        unsafe_allow_html=True
    )
        
    
    st.markdown(
    """
    <style>
    .title {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px
    }
    </style>
    <h1 class='title'>Impacto dos Acessos a Recursos Educacionais
    na Aprovação em EaD: Uma Abordagem Estatística e Preditiva</h1>
    """, unsafe_allow_html=True)
    
    # Texto justificado e centralizado
    st.markdown("""
    <div style="text-align: justify; text-justify: inter-word; margin-left: auto; margin-right: auto; width: 80%;">
        O estudo busca investigar o impacto do acesso a recursos e atividades em Ambientes
        Virtuais de Aprendizagem (AVA) no sucesso acadêmico em Educação a Distância
        (EaD). Apesar da flexibilidade oferecida pela EaD, ela enfrenta desafios significativos
        relacionados ao engajamento e à eficácia do ensino. Para enfrentar esses desafios, a
        pesquisa analisou dados de um AVA, incluindo acessos, participação em atividades e
        interações dos alunos, utilizando técnicas de Mineração de Dados Educacionais (MDE)
        para identificar padrões e prever o desempenho acadêmico.<br><br>
        A pesquisa visa desenvolver um modelo preditivo que possa auxiliar educadores
        e gestores na implementação de intervenções pedagógicas mais eficazes,
        potencialmente melhorando os resultados acadêmicos. Além de oferecer uma
        solução prática, o estudo busca contribuir para a melhoria da qualidade do ensino em
        EaD, ao criar ferramentas preditivas intuitivas que possam ser utilizadas facilmente
        por educadores, mesmo aqueles com pouca familiaridade técnica.<br><br>
        Os resultados da pesquisa revelam uma forte correlação entre o nível de interação
        dos alunos e seu sucesso acadêmico. O estudo culmina na criação de um modelo
        preditivo integrado a uma aplicação web, que funciona como uma ferramenta prática
        para monitorar o engajamento dos alunos e prever seu desempenho. Dessa forma,
        a pesquisa oferece soluções baseadas em dados que promovem uma gestão
        pedagógica mais eficiente e a melhoria da qualidade educacional em EaD.
    </div>
    """, unsafe_allow_html=True)