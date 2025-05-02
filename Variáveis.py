import streamlit as st
from PIL import Image

# variáveis
exemplosvariaveis = '''
idade (variável) = 14 (valor)    #variável do tipo int
altura = 1.72    #variável do tipo float
nome = "André Ícaro"    #variável do tipo string
namorando = false     #variável do tipo bool
'''
exemplosvariaveis2 = '''
preco = 50
desconto = 10
preco_final = preco - desconto
print("O preço final é:", preco_final)

Saída:
O preço final é: 40
'''
exemplooperacoes = '''
cedulas = 10
moedas = 5
print(cedulas+moedas)

Saída:
15'''

imagemvar = Image.open("variaveis.png")

col1, col2, col3 = st.columns([1, 2, 3])
with col2:
    st.image("variaveis.png", caption="-", width=400)

st.write("# O que são as variáveis?")
st.write("Uma variável em Python é algo que pode guardar um valor/informação, geralmente em números inteiros (int), números decimais (float), caracteres (string) e 'false' ou 'true' (bool).")
st.write("Podemos levar como exemplo as caracteristicas de uma pessoa.")
st.write("Primeiramente, para criar uma variável, precisamos simplesmente escolher o nome da variável e o valor dela.")
st.write("### Exemplos:")
st.code(exemplosvariaveis, language = 'python')
st.write("# Porque é importante e como podemos utilizar uma variável?")
st.write("As variáveis são fundamentais porque elas permitem que o programa guarde informações temporariamente na memória para usar depois."
" Sem variáveis, seria como tentar fazer uma conta matemática sem anotar os números em lugar nenhum!")
st.write("✅ Com variáveis, podemos:"
"\nArmazenar dados do usuário (ex: nome, idade, resposta);"
"\nFazer cálculos com números guardados;"
"\nControlar o que o programa vai mostrar ou fazer (ex: verificar se uma média é maior que 7);"
"\nReutilizar e modificar valores sem precisar repetir tudo.")
st.write("### Exemplos:")
st.code(exemplosvariaveis2, language = 'python')

st.write("# Operações Aritméticas")
st.write("Em Python, podemos: adicionar, subtrair, multiplicar e dividir livremente os valores de uma variável.")
st.write("Para adição: +")
st.write("Para subtração: -")
st.write("Para multiplicação: *")
st.write("Para divisão: /")
st.write("### Exemplos:")
st.code(exemplooperacoes, language = 'python')

st.write("# Cuidado com a formatação!")