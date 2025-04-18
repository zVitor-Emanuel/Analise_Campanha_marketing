import streamlit as st
import pandas as pd

df2 = pd.read_csv('mkt_data.csv', index_col=0)
df2.index.name = 'Index'

st.title('Informações iniciais sobre a base de dados: ')

st.markdown("""
# Conteúdo do Dataset:
### 1. Inicialmente o dataset apresentava 2205 Linhas e 43 Colunas
### 2. Contém informações demográficas, financeiras e de consumo de cada cliente
### 3. Sem valores ausentes, porém com 184 duplicatas.
""")

st.write('---------------------------------------------------')

st.markdown("""
# Dicionário dos dados
            
### 🧍 Perfil Demográfico

| Coluna           | Descrição                                                      |
| ---------------- | -------------------------------------------------------------- |
| Age            | Idade do cliente.                                              |
| Education      | Nível de educação (ex: "Graduation", "PhD", "Basic", etc.).    |
| Marital_Status | Estado civil (ex: "Single", "Married", "Divorced", etc.).      |
| Income         | Renda anual do cliente.                                        |
| Kidhome        | Número de crianças na residência.                              |
| Teenhome       | Número de adolescentes na residência.                          |
| Customer_Days  | Dias do cliente na plataforma.                                 |
| Recency        | Dias desde a última compra.                                    |
| Complain       | Cliente já realizou alguma reclamação? (1 = Sim, 0 = Não). |

---

### 🛍️ Comportamento de Compra

| Coluna             | Descrição                              |
| ------------------ | -------------------------------------- |
| MntWines         | Gasto total com vinhos.                |
| MntFruits        | Gasto total com frutas.                |
| MntMeatProducts  | Gasto total com carnes.                |
| MntFishProducts  | Gasto total com peixes.                |
| MntSweetProducts | Gasto total com doces.                 |
| MntGoldProds     | Gasto total com produtos de ouro/luxo. |

---

### 🛒 Canais de Compra

| Coluna                | Descrição                                                        |
|-----------------------|------------------------------------------------------------------|
| NumDealsPurchases   | Nº de compras realizadas com desconto.                          |
| NumWebPurchases     | Nº de compras feitas pela internet.                             |
| NumCatalogPurchases | Nº de compras feitas por catálogo.                              |
| NumStorePurchases   | Nº de compras feitas em loja física.                            |
| NumWebVisitsMonth   | Nº de visitas ao site no último mês.                            |

---

### 📣 Campanhas de Marketing

| Coluna         | Descrição                                               |
| -------------- | ------------------------------------------------------- |
| AcceptedCmp1 | Aceitou a campanha 1? (1 = Sim, 0 = Não)            |
| AcceptedCmp2 | Aceitou a campanha 2?                                   |
| AcceptedCmp3 | Aceitou a campanha 3?                                   |
| AcceptedCmp4| Aceitou a campanha 4?                                   |
| AcceptedCmp5 | Aceitou a campanha 5?                                   |
| Response     | Aceitou a campanha mais recente? (1 = Sim, 0 = Não) |

---
""")

st.markdown("# Dataframe Inicial")

df2