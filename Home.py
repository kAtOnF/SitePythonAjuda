import streamlit as st
from PIL import Image

# variáveis
imagem_eu = Image.open("eulindo.jpg")

# textos iniciais
st.write("# Dashboard Python Ikaros")
st.write("Aqui haverá diversas dicas para ajudar você em sua jornada no aprendizado da linguagem de programação Python.")
st.write("O propósito para eu ter feito este site, é para ajudar tanto a mim quanto á você que está lendo isso.")
st.write("### Quem sou eu?")
col1, col2, col3 = st.columns([1, 2, 3]) # definição de colunas
with col2:
     st.image("eulindo.jpg", caption="Eu mesmo, o mais gostioso do Brasil! 😎", width=300)
st.write("Meu nome é André Ícaro, atualmente tenho 14 anos e estou cursando o 1°ano do ensino médio integrado a um curso técnico de informática, no IFPB Campus Campina Grande.")
st.write("Meu maior objetivo na área é me formar, desenvolver diversos projetos e conseguir trabalhar para um empresa bem renomada."
" Um objetivo secundário, que eu também tenho, é criar um jogo que alcance um sucesso considerável.")
st.write("Na barra lateral ao lado, existem diversas sessões onde explico (ou tento) detalhadamente diversas funções e sistemas do Python. Fique á vontade em explorar para tirar suas dúvidas ou até mesmo aprender coisas novas!")