import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


# Estilo grafico
def aplicar_estilo():
    sns.set_style("whitegrid")  
    sns.set_palette(["#8ecae6", "#219ebc", "#ffb703", "#fb8500", "#ff006e"])
    plt.rcParams.update({
        'axes.facecolor': '#1e1e1e',         # fundo do gráfico
        'figure.facecolor': '#1e1e1e',       # fundo da figura
        'axes.edgecolor': '#aaaaaa',         # bordas
        'axes.labelcolor': '#dddddd',        # rótulos dos eixos
        'xtick.color': '#ADD8E6',            # cor dos ticks x
        'ytick.color': '#ADD8E6',            # cor dos ticks y
        'text.color': '#ADD8E6',             # cor geral dos textos
        'font.size': 12,
        'axes.titlesize': 14,
        'axes.titleweight': 'bold',
        'grid.color': '#ADD8E6',             # cor da grid discreta
        'grid.linestyle': ':',               # estilo pontilhado
        'legend.facecolor': '#2b2b2b',
        'legend.edgecolor': '#444444',
    })

# Barras
def plot_countplot(df, coluna, titulo="", xlabel="", ylabel=""):
    fig, ax = plt.subplots()
    sns.countplot(x=coluna, data=df, ax=ax)
    ax.set_title(titulo, fontsize=16)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# Histograma
def plot_histograma(df, coluna, bins=20, titulo="", xlabel="", ylabel=""):
    fig, ax = plt.subplots()
    sns.histplot(df[coluna], kde=True, color='skyblue', bins=bins, ax=ax)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# Boxplot
def plot_boxplot(df, coluna, titulo="", xlabel="", ylabel=""):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x=coluna)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

def plot_bar(df, colx, coly, titulo="", xlabel="", ylabel=""):
    fig, ax = plt.subplots()
    sns.barplot(df, x=colx, y=coly)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

def plot_bar2(df, colx, coly, titulo="", xlabel="", ylabel=""):
    fig, ax = plt.subplots()
    plt.figure(figsize=(10, 6))
    sns.barplot(df, x=colx, y=coly)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

def plot_barhue(df, colx, coly, huec, titulo="", xlabel="", ylabel=""):
    fig, ax = plt.subplots()
    sns.barplot(df, x=colx, y=coly, hue=huec)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

def plot_scatter(df, colx, coly, titulo="", xlabel="", ylabel=""):
    fig, ax = plt.subplots()
    sns.scatterplot(df, x=colx, y=coly)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)
