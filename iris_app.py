import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Iris app 🌸')

df = pd.read_csv('data/iris.csv')


st.sidebar.header('Filtro')

opc = df['species'].unique().tolist()
filt_speci = st.sidebar.selectbox('Especie', options=opc)
                                  
column_numerica = st.sidebar.selectbox('Columna numerica', options=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

minV = df[column_numerica].min()
maxV = df[column_numerica].max()

rango = st.sidebar.slider(f'Rango para {column_numerica}', min_value = minV, max_value = maxV, value = (minV, maxV))


df_sp = df[df['species']==filt_speci]
df_f = df_sp[(df_sp[column_numerica]>= rango[0]) & (df_sp[column_numerica]<=rango[1])]
st.dataframe(df_f)



st.divider()
st.subheader('Histograma')

serie = df_f[column_numerica].dropna()


if serie.empty:
    st.info("No hay datos para graficar (la columna quedó vacía o con nulos tras el filtrado).")
else:
    fig, ax = plt.subplots()
    ax.hist(serie)
    ax.set_title(f"Histograma de {column_numerica} ({filt_speci})")
    ax.set_xlabel(column_numerica)
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)

