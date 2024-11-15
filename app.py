import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = '../datasets/BeansDataSet.csv'
data = pd.read_csv(filename)

st.set_page_config(page_title="Analyse des Ventes : Beans and Pods", layout="wide")

st.title("Analyse des Ventes : Beans and Pods")
st.write("Explorez les données du dataset **Beans and Pods** à l'aide de visualisations interactives.")

st.sidebar.header("Options d'Analyse")
selected_columns = st.sidebar.multiselect(
    "Choisissez les colonnes à inclure dans l'analyse",
    data.columns.tolist(),
    default=data.columns.tolist()
)

st.subheader("Aperçu des Données")
st.write(data[selected_columns].head())

if st.sidebar.checkbox("Afficher la Matrice de Corrélation"):
    st.subheader("Matrice de Corrélation")
    num_data = data.select_dtypes(include=['int64', 'float64'])
    corr_matrix = num_data.corr().round(2)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax, center=0)
    st.pyplot(fig)

if st.sidebar.checkbox("Analyse des Ventes par Canal"):
    st.subheader("Comparaison des Ventes par Channel")
    ventes_par_canal = data.groupby('Channel').sum()
    fig, ax = plt.subplots()
    ventes_par_canal[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].plot(kind='box', ax=ax)
    ax.set_title("Comparaison des Ventes par Channel")
    ax.set_xlabel("Channel")
    ax.set_ylabel("Ventes")
    st.pyplot(fig)

if st.sidebar.checkbox("Analyse des Ventes par Région"):
    st.subheader("Comparaison des Ventes par Région")
    ventes_par_region = data.groupby('Region').sum()
    fig, ax = plt.subplots()
    ventes_par_region[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].plot(kind='bar', stacked=True, ax=ax)
    ax.set_title("Comparaison des Ventes par Région")
    ax.set_xlabel("Région")
    ax.set_ylabel("Ventes")
    ax.legend(title="Produits")
    st.pyplot(fig)

if st.sidebar.checkbox("Résumé des Ventes"):
    VenteTotal_C = data.groupby('Channel')[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].sum()
    VenteTotal_R = data.groupby('Region')[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].sum()
    
    st.subheader("Ventes Totales par Channel")
    st.write(VenteTotal_C)

    st.subheader("Ventes Totales par Région")
    st.write(VenteTotal_R)

if st.sidebar.checkbox("Nombre de Ventes par Région et Canal"):
    st.subheader("Nombre de Ventes par Région et par Canal")
    ventes_par_region_par_channel = data.groupby(['Region', 'Channel']).size().unstack()
    st.write(ventes_par_region_par_channel)

st.sidebar.subheader("Histogramme")
selected_hist_column = st.sidebar.selectbox("Choisissez une colonne pour l'histogramme", data.select_dtypes(include=['int64', 'float64']).columns)
if st.sidebar.checkbox("Afficher l'Histogramme"):
    st.subheader(f"Histogramme : {selected_hist_column}")
    fig, ax = plt.subplots()
    data[selected_hist_column].hist(bins=20, ax=ax, color='skyblue')
    ax.set_title(f"Histogramme de {selected_hist_column}")
    st.pyplot(fig)
