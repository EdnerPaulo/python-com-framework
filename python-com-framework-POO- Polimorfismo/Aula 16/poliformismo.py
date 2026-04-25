import streamlit as st
import pandas as pd

# herança e poliformismo ...

class Linguagem:
    def executar(self):
        return "Executando codigo ... "
    
class Python(Linguagem):
    def executar(self):
        return 'Executar Linguagem back e front'
    
class Go(Linguagem):
    def executar(self):
        return 'Executar Linguagem de servidor e segurança'
    
class JavaScript(Linguagem):
    def executar(self):
        return 'Executar Linguagem para Web'
    
st.title('POO - Polimorfismo')
st.write('Escolha um ...')
opcao = st.selectbox(
    'Escolha a Linguagem ',
    ['','Python','Go', 'JavaScript']
)
if opcao == '':
    linguagem = Linguagem()
if opcao == 'Python':
    linguagem = Python()
elif opcao == 'Go':
    linguagem = Go()
elif opcao == 'JavaScript':
    linguagem = JavaScript()

st.subheader('RESULTADO')
st.success(linguagem.executar())
st.balloons()

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)