import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from modulos import plot_countplot, aplicar_estilo, plot_barhue

aplicar_estilo()

df = pd.read_csv('dados_limpos.csv')

st.title('Exploraremos qual o perfil de clientes que aceitaram campanhas, e os meios que eles utilizaram para fazer suas compras:')

cliente_propensos = df[df['Response'] == 1]

st.write("### Número de clientes que aceitaram a campanha anterior:", cliente_propensos.shape[0])
st.write('Utilizei a coluna response para filtrar os clientes que aceitaram a ultima campanha, gerando somente 311 clientes, muito menos que nossa base')
st.write(cliente_propensos)

st.write('Quantidade de clientes que tanto aceitaram, quanto negaram a última campanha: ')
st.write('0 = Não aceitou, 1 = Aceitou')

st.dataframe(df['Response'].value_counts())

st.write('---------------------------------------------------')

st.title('Irei verificar o perfil dos clientes que aceitaram as campanhas, para identificar o padrão que buscamos ' \
'para maior aceitação das próximas: ')

st.write('Como podemos ver abaixo, a distribuição de idade dos nossos clientes que aceitaram a ultima campanha, ' \
'permanece similar ao grupo completo.')
st.dataframe(cliente_propensos['Age'].describe())

st.write('### Estado civil dos cliente que aceitaram campanhas: ')
st.write('Temos um grupo maior de Solteiros e Casados')
plot_countplot(cliente_propensos, 'marital_status')

st.write('### Nivel de educação dos clientes que aceitaram a ultima campanha: ')
st.write('A maior parte dos clientes que aceitaram a campanha tem nivel de Graduação ou Doutorado')
plot_countplot(cliente_propensos, 'education_level')

st.write('### Salario dos clientes que aceitaram a campanha: ')
st.write('Nossos clientes que aceitaram as campanhas em grande parte tem renda entre: 25.000 - 114.000 ')
plot_countplot(cliente_propensos, 'salario_por_faixa')

st.write('---------------------------------------------------')

st.write('### Agora vou entender o perfil de compras desses clientes que aceitaram as campanhas e comparar as medias de gastos, com os que não aceitaram, ' \
'assim conseguiremos investir em campanhas para favorecer a compra desses produtos para ambos os públicos: ')

coluna_de_gastos = ['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']

st.write('Como se pode observar, o padrão de compras dos dois públicos são iguais, porém temos uma media de gasto maior para as pessoas ' \
'que aceitaram as campanhas, assim faz sentido investirmos em campanhas para atrair mais pessoas, que podem comprar mais.')
st.dataframe(df.groupby('Response')[coluna_de_gastos].mean().T.sort_values(by=1, ascending=False))

media_gastos = df.groupby('Response')[coluna_de_gastos].mean().T.sort_values(by=1, ascending=False)
media_long = media_gastos.reset_index().melt(id_vars='index', var_name='Response', value_name='Gasto Médio')
media_long.rename(columns={'index': 'Produto'}, inplace=True)

plt.figure(figsize=(10, 6))
ax = sns.barplot(
    data=media_long, 
    x='Gasto Médio', 
    y='Produto', 
    hue='Response', 
    palette='viridis'
)


plt.title('Gasto médio por tipo de produto (comparação entre respostas)')
plt.xlabel('Gasto médio (R$)')
plt.ylabel('Produto')

new_labels = ['Não aceitou', 'Aceitou']
handles, _ = ax.get_legend_handles_labels()
plt.legend(handles=handles, labels=new_labels, title='Resposta à campanha')

st.pyplot(plt)


st.write('---------------------------------------------------')

st.title('Verificarei os canais de compras que os clientes preferem: ')

canais = ['NumWebPurchases','NumCatalogPurchases','NumStorePurchases','NumDealsPurchases','NumWebVisitsMonth']

st.dataframe(df.groupby('Response')[canais].sum().T.sort_values(by=1, ascending=False))

soma_canais = df.groupby('Response')[canais].sum().T.sort_values(by=1, ascending=False)
soma_long = soma_canais.reset_index().melt(id_vars='index', var_name='Response', value_name='Total de Uso')
soma_long.rename(columns={'index': 'Canal'}, inplace=True)


st.write('Como é lógico pensar, temos bem mais cliente que não aceitaram as campanhas, assim o número de compras e acessos ' \
'dos clientes que não participaram da campanha é maior ')
st.write('E tambem temos preferência de compra em loja, porém com muitas visitas online, que podemos melhorar para vendermos mais online.')
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=soma_long, x='Total de Uso', y='Canal', hue='Response', palette='mako')
plt.title('Total de uso dos canais de compra por resposta à campanha')
plt.xlabel('Total de uso')
plt.ylabel('Canal')
new_labels = ['Não aceitou', 'Aceitou']
handles, _ = ax.get_legend_handles_labels()
plt.legend(handles=handles, labels=new_labels, title='Resposta à campanha')
st.pyplot(plt)

st.write('---------------------------------------------------')

st.title('Quem gastou mais, os que não aceitaram ou os que aceitaram as campanhas? ')
st.write('Como também podia ser presumivel, os clientes que não aceitaram as campanhas estavam em maior número, assim' \
' gastaram um total maior que os clientes que aceitaram ultima campanha, porém estamos falando de uma comparação entre 1700 e 300 clientes. ')
st.dataframe(df.groupby('Response')['expenses'].sum())

st.write('### Se formos pensar no gasto individual médio: ')
st.write('##### O gasto individual médio de cada cliente que não aceitou é aproximadamente: $500')
st.write('##### Ja o gasto individual medio de cada cliente que aceitou a campanha é aproximadamente: $917')
st.write('Isso nos ajuda a dizer que investir em campanhas para atrair mais clientes pode ser ainda mais vantajoso, ' \
'tendo em vista que os clientes que aceitam campanhas tem um gasto individual maior.')