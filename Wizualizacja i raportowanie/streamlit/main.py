import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris, load_wine, load_breast_cancer


# Funkcja ładowania danych w zależności od wyboru
def load_data(dataset_name):
    if dataset_name == 'iris':
        data = load_iris()
    elif dataset_name == 'wine':
        data = load_wine()
    elif dataset_name == 'breast_cancer':
        data = load_breast_cancer()

    df = pd.DataFrame(data.data, columns=data.feature_names)
    return df


# Nagłówek aplikacji
st.title("Lab Streamlit App")

# Dropdown do wyboru datasetu
dataset_name = st.selectbox(
    'Wybierz zestaw danych:',
    ['iris', 'wine', 'breast_cancer'],
    index=0  # Domyślnie wybieramy 'iris'
)

# Ładujemy odpowiednie dane
df = load_data(dataset_name)

# Wyświetlanie tabeli danych
st.subheader('Tabela danych:')
st.dataframe(df)

# Selectbox do wyboru kolumny do histogramu
column_name = st.selectbox(
    'Wybierz kolumnę do histogramu:',
    df.columns,
    index=0  # Domyślnie pierwsza kolumna
)

# Generowanie histogramu
fig = px.histogram(df, x=column_name, nbins=20, title=f'Histogram of {column_name}')
st.plotly_chart(fig)
