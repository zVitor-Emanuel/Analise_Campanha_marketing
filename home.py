import streamlit as st

st.title("Análise Exploratória de Dados - Campanha de Marketing")

st.write("""<h2 style='font-size: 24px;'>Neste projeto busquei fazer uma análise exploratória dos dados,
         utilizando unicamente estatística descritiva para entender o perfil dos clientes e seus comportamentos em 
         relação as campanhas de marketing promovidas. Também tentei identificar oportunidades para melhorar as campanhas,
         dado que a grande maioria dos nossos clientes não participam delas. Assim, fiz a limpeza e preparação dos dados.
          Após isso, explorei todas as variáveis para entender o padrão de compra dos usuários e fazer recomendações baseadas nos insights
         que obtive ao explorar o dataset.</h2>""", unsafe_allow_html=True)

st.write("""<h2 style='font-size: 24px;'>Todo o projeto foi feito utilizando python e suas bibliotecas, principalmente Pandas, Seaborn e matplotlib.
          Após pensar em como apresentar os dados, resolvi utilizar a biblioteca streamlit para fazer essa página contendo todos os insights,
         de forma rápida e visual sem precisar ficar olhando o código no notebook, porém ele está disponível abaixo para possíveis dúvidas
         ou curiosidades sobre a análise.</h2>""", unsafe_allow_html=True)


url = "https://github.com/zVitor-Emanuel/Analise_Campanha_marketing/blob/main/eda_notebook.ipynb"

if st.button('Ver código Jupyter Notebook'):
    st.markdown(f'<a href="{url}" target="_blank">Clique aqui para acessar o notebook no GitHub</a>', unsafe_allow_html=True)
