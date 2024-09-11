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
            margin-bottom: 5px;
        }
        .curso{
            font-size: 25px;
            font-weight: bold;
        }
        </style>
        <div class="title-page">
            <div class="university">Universidade Federal do Maranhão</div>
            <div class="curso">Curso de Ciência e Tecnologia</div>
            <div class="subtitle">Trabalho de Conclusão de Curso</div>
            <div class="authors">Orientadora: Profa. Dra. Alana de A. Oliveira M. Teixeira</div>
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
        Este estudo investiga o impacto do acesso a recursos e atividades em Ambientes
        Virtuais de Aprendizagem (AVA) no sucesso acadêmico em Educação a Distância
        (EaD), um modelo que, embora flexível, enfrenta desafios relacionados ao
        engajamento e à eficácia do ensino. Com o objetivo de melhorar a qualidade da EaD, a
        pesquisa utilizou técnicas de Mineração de Dados Educacionais (MDE) para analisar
        padrões de acesso, participação em atividades e interações dos alunos, buscando
        prever o desempenho acadêmico.<br><br>
        Através dessa análise, foi desenvolvido um modelo preditivo que auxilia educadores
        e gestores na implementação de intervenções pedagógicas mais eficazes. Além de
        fornecer uma ferramenta prática, o estudo visa facilitar o uso de recursos preditivos
        intuitivos, acessíveis mesmo a educadores com pouca familiaridade técnica.<br><br>
        Os resultados mostram uma forte correlação entre o nível de interação dos alunos e
        seu sucesso acadêmico, culminando na criação de uma aplicação web que monitora o
        engajamento e prevê o desempenho. A pesquisa, assim, oferece soluções baseadas
        em dados para promover uma gestão pedagógica mais eficiente e elevar a qualidade
        da EaD.<br><br>
    </div>
    """, unsafe_allow_html=True)