import streamlit as st
import pandas as pd
from modulos import aplicar_estilo, plot_countplot, plot_histograma

aplicar_estilo()

df = pd.read_csv('dados_limpos.csv')

st.title('Quem são nossos clientes?')

st.markdown('### Faixa etária:')
st.write('Nossos clientes estão em uma faixa etária entre 43 e 61 anos, com média em torno de 51 e mediana 50.')
st.write(df['Age'].describe())
plot_histograma(df, 'Age', titulo="Distribuição de Idade", xlabel="Idade")

st.write('---------------------------------------------')

st.markdown('### Escolaridade:')
st.write('Temos predominância de clientes com nível de escolaridade de ensino superior, o que já sugere um direcionamento para nossas campanhas.')
st.write(df['education_level'].value_counts())
plot_countplot(df, 'education_level', titulo="Distribuição dos Níveis de Educação")

st.write('---------------------------------------------')

st.markdown('### Estado civil:')
st.write('Temos uma base de clientes diversificada em termos de estado civil, com maioria casada.')
st.write(df['marital_status'].value_counts())
plot_countplot(df, 'marital_status', titulo="Estado Civil", xlabel="Estado Civil")

st.write('---------------------------------------------')

st.markdown('### Quantidade de filhos:')
st.write('Grande parte dos nossos clientes tem filhos, sendo a maioria.')
st.write(df['kids'].value_counts())
plot_countplot(df, 'kids', titulo="Quantidade de Filhos", xlabel="Número de Filhos")
