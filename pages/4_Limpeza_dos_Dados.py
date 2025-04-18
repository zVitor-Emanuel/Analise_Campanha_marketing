import streamlit as st
import pandas as pd

df = pd.read_csv('mkt_data.csv')
numeric_vars = df.select_dtypes(include='number')
str_var = df.select_dtypes(include='object')


st.markdown("""
## Entendendo os dados da nossa base:
""")
st.write("<h2 style='font-size: 24px;'>Para começar a análise separei nossas variáveis entre categóricas" \
" e numéricas para entender como os dados estavam distribuidos, após isso consegui identificar 10 colunas" \
" que não seriam úteis para nossa análise pois eram colunas booleanas que representavam variações das nossas colunas categóricas.</h2>", unsafe_allow_html=True)

st.markdown("## Váriaveis Numéricas:")
numeric_vars.columns

st.markdown("## Váriaveis Categóricas:")
str_var.columns

st.markdown('## Variaveis booleanas que serão apagadas pois temos duas variaveis categóricas que respresentam melhor os valores: ')
df[['marital_status','education_level','education_2n Cycle', 'education_Basic', 'education_Graduation', 'education_Master', 
    'education_PhD', 'marital_Divorced', 'marital_Married', 'marital_Single', 'marital_Together', 'marital_Widow']]

st.write('---------------------------------------------------')

df1 = df.drop(columns=['education_2n Cycle', 'education_Basic', 'education_Graduation', 'education_Master', 'education_PhD', 
                       'marital_Divorced', 'marital_Married', 'marital_Single', 'marital_Together', 'marital_Widow'])

st.markdown('## Não existem valores nulos em nossa base, em contrapartida temos 184 duplicatas que foram excluidas da nossa base: ')
st.markdown('### Resultando no dataset final com 2021 linhas e 33 colunas.')

st.write('---------------------------------------------------')

st.markdown('# Para facilitar análises futuras irei criar 2 colunas: ')
st.markdown("""
### Coluna: ['tem_filho'] = Temos clientes que tem mais de 1 filho, assim irei criar uma coluna booleana para verificar se o cliente tem filho ou não.
### Coluna: ['salario_por_faixa'] = Irei discretizar a renda dos cliente em 4 valores, 0-25k = 1, 25-50k = 2, 50-75k = 3, 75-114k = 4""")

dataset = pd.read_csv('dados_limpos.csv')
st.markdown("## DataSet Limpo e pronto para ser analisado, com 2021 Linhas e 35 Colunas")
dataset