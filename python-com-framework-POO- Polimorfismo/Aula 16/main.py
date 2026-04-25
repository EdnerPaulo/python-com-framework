import streamlit as st
import pandas as pd
import numpy as np



st.title('ISSO É UM TESTE')

# dados = {

#     'dia': [1,2,3,4,5],
#     'Vendas': [500,450,200,150,1000] 
# }

# df = pd.DataFrame



#-----------------------------------------------------------------------

st.title('Ler o CSV')


arquivo = st.file_uploader('Enviar CSV',type=['csv'])

if arquivo:
    df = pd.read_csv('dados.csv')
    st.write('dados')
    st.dataframe(df)
    if st.button('Gerar Grafico'):
        st.bar_chart(df)


#--------------------------------------------------------------------------

st.title('Imagem')

st.image('mordor.jpg'
         )

