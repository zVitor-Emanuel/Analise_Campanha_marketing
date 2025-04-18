import streamlit as st
import pandas as pd
from modulos import aplicar_estilo, plot_countplot, plot_histograma, plot_boxplot, plot_bar, plot_bar2, plot_scatter

aplicar_estilo()

df = pd.read_csv('dados_limpos.csv')

st.title('Renda e padrões de consumo pelos clientes: ')

st.write('### Temos uma distribuição de renda simétrica, sem outliers e com desvio padrão alto, pois nosso coeficiente variação é de 40%, ' \
'o que nos diz que a renda dos nossos clientes variam muito em torno da média, tendo clientes que ganham muito e clientes que ganham pouco.')
renda = df['Income'].describe()
renda
plot_histograma(df, 'Income', titulo='Distribuição Salárial',xlabel='Renda Anual', ylabel='Número de clientes')

st.write('---------------------------------------------')

st.write('## Como vimos anteriormente, grande parte dos nossos clientes tem filhos, será que esse clientes gastam mais? ')
st.write('#### Após analisar o gráfico abaixo, visualisamos que quanto menos filhos o cliente tem, mais ele gasta na plataforma.')
plot_bar(df, 'kids', 'expenses', titulo="Gasto Médio, por número de filhos",xlabel="Numero de Filhos", ylabel="Gastos")

st.write('---------------------------------------------')

st.write('## Em contrapartida, será que os cliente que mais gastam na plataforma são os que ganham mais? ')
st.write('#### Como eu tinha discretizado os salários na limpeza de dados, utilizei esse parâmetro para analisar os dados.')
st.write('#### 1 = 0-25k, 2 = 25-50k, 3 = 50-75k, 4 = 75-114k')
st.write('#### No gráfico abaixo, conseguimos observar que a média gasta por cada faixa salárial é continua, ' \
'assim, quanto maior o salário mais gasto essa pessoa tem na plataforma. ')
plot_bar(df, 'salario_por_faixa', 'expenses', titulo='Gastos Medio por Renda')
st.write('### Conseguimos observar uma possivel correlação entre salário e gastos.')
plot_scatter(df, 'Income', 'expenses', xlabel='Salário', ylabel='Gastos')


st.write('---------------------------------------------')

st.write('## Nas ultimas duas análise, observamos que quanto maior o salário mais gastos, e quanto menor o número de filhos, ' \
'maior o gasto, assim vamos correlacionar as duas variáveis para termos certeza que a média salárial de pessoas sem filhos é maior')
st.write('#### na limpeza de dados criei a coluna "tem_filho", para discretizar os valores e utilizarei ela aqui.')
plot_bar(df, 'tem_filho', 'Income', titulo='Media salárial por número de filhos', xlabel='0 = Não tem filho, 1 = Tem Filho(s)', ylabel='Media Salarial')

st.write('## Tambem verificaremos quantos clientes tem e não tem filhos. E além disso, a quantidade gasta por esses dois perfis.')
st.write('Como podemos observar nas tabelas abaixo, cerca de 3/4 dos nossos clientes tem filho, e mesmo assim, o 1/4 restante tem um gasto maior')
st.dataframe(df['tem_filho'].value_counts())

st.dataframe(df.groupby('tem_filho')['expenses'].sum())

st.write('---------------------------------------------')

st.write('## Média de Gastos baseado em estado civil: ')
st.write('#### Aqui observamos que por mais que as pessoas viúvas apresentem um maior gasto medio, em grande parte a distribuição de gastos ' \
'pelo estado civil é parecida')
gastos_estadocivil = df.groupby('marital_status')['expenses'].mean()
gastos_estadocivil
plot_bar(df, 'marital_status', 'expenses', titulo='Gastos por Estados civil')

st.write('---------------------------------------------')

st.title('Consumo dos clientes: ')
st.write('## Consumo médio por produto: ')
st.write('#### Como podemos observar abaixo, temos predominância de 2 tipos de produtos mais buscados, sendo eles: ' \
'Vinhos e Carnes. E os menos buscados: Doces e Frutas')
coluna_de_gastos = ['MntWines','MntMeatProducts','MntFruits','MntFishProducts','MntSweetProducts','MntGoldProds']
medias_gastos = df[coluna_de_gastos].mean().sort_values(ascending=False)
rename_vars = {
    'MntWines': 'Vinhos',
    'MntFruits': 'Frutas',
    'MntMeatProducts': 'Carnes',
    'MntFishProducts': 'Peixes',
    'MntSweetProducts': 'Doces',
    'MntGoldProds': 'Luxo'
}
medias_gastos.index = medias_gastos.index.to_series().replace(rename_vars)
df_medias = medias_gastos.reset_index()
df_medias.columns = ['Categoria', 'Media']
plot_bar(df_medias, 'Categoria', 'Media', ylabel='Valor $')

st.write('---------------------------------------------')

st.write('## Temos uma boa discrepância de compras de Vinhos e Carnes, nos garantindo que a maioria dos nossos clientes, ' \
'independente do estado civil, numero de filho ou educação comprariam esses produtos, mas observaremos os números pré-supostos.')
st.write('#### Media de gastos por produtos: ')
consumo_por_estadocivil = df.groupby('marital_status')[coluna_de_gastos].mean()
consumo_por_numerof = df.groupby('kids')[coluna_de_gastos].mean()
consumo_por_educao = df.groupby('education_level')[coluna_de_gastos].mean()
consumo_por_estadocivil
consumo_por_numerof
consumo_por_educao

