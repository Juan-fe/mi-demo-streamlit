
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Iris app 🌺')

df = pd.read_csv('data/iris.csv')


st.sidebar.header('Filtro')

opc = df['species'].unique().tolist()
filt_speci = st.sidebar.selectbox('Especie', options=opc)

column_numerica = st.sidebar.selectbox('Columna numerica', options=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

vmin = df[column_numerica].min()
vmax = df[column_numerica].max()
rango = st.sidebar.slider(f'Rango para {column_numerica}', min_value=vmin, max_value=vmax, value=(vmin,vmax))

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

st.divider()

#Entrenar modelo

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('data/iris.csv')

X = df.drop(columns=['species'])

y = df['species'].map({
    'setosa': 0,
    'versicolor': 1,
    'virginica': 2
})



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


modelo = LinearRegression()
modelo.fit(X_train, y_train)

with st.form('prediccio'):
    sepal_length = st.slider('sepal_length')
    sepal_w = st.slider('sepal_width')
    petal_wi = st.slider('petal_width')
    petal_le = st.slider('petal_length')
    if st.form_submit_button('Predecir', type='primary'):
        prediccion = modelo.predict([[sepal_length,sepal_w,petal_le,petal_wi]])
        st.write(prediccion)
