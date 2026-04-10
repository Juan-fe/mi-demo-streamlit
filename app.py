import streamlit as st
import pandas as pd


#Texto
st.title('Hello streamlit!')
st.caption('Vamos a ver algunos componentes.')
st.subheader('Esto es un subtitulo en streamlit')
st.text('Esto es un texto en streamlit')
st.markdown('_Markdown_')

st.divider()

#Input Widget
text_input = st.text_input('Nombre')
text_area = st.text_area('Text Area',max_chars=100, placeholder='Esto es un placeHolder')
select_bx = st.selectbox('Pick one', options=['Julian', 'Pedro', 'Maria'])
radio = st.radio('Radio', options=['Julian', 'Pedro', 'Maria'], horizontal=True)

st.divider()

#Numeric
number = st.number_input('Pick a number', min_value=-100, max_value=100, step=1)
slider = st.slider('Age')

#Date and time
date = st.date_input('Your birthday')
time = st.time_input('Meeting time')



#Boolean
check_box = st.checkbox('Check')
activated = st.toggle('Activate')

st.divider()

feedback = st.feedback('thumbs')


st.divider()

col1, col2, col3 = st.columns(3)


with col1:
    st.write('Julian')
with col2:
    st.slider('Edad')
with col3:
    st.date_input('Cumpleaño')

st.sidebar.header('Este es el sidebar')
st.sidebar.toggle('Activate')

tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])


with tab2:
    st.subheader('Estoy en Tab2')
