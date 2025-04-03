# https://dontpad.com/apptickers
import requests
import json
import sqlite3
import streamlit as st
import pandas as pd

arquivo_banco = 'banco.db'

# Função para obter a lista de preços
# ------------------------------------------------------------------------------
def obter_precos(cod_ativo):
    url = "https://statusinvest.com.br/acao/tickerprice"

    params = {
        "ticker" : cod_ativo,
        "type": 3
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    http_req = requests.get(url, params=params, headers=headers)
    
    dados = http_req.json()
    return dados[0]["prices"]

# ------------------------------------------------------------------------------

def ler_precos(id_ativo):
    return

def adicionar_ativo(nome, ticker):
    # id_ativo = 0
    with sqlite3.connect(arquivo_banco) as arq:
        banco = arq.cursor()
        banco.execute("INSERT INTO Ativos (nome, ticker) VALUES (?, ?)", (nome, ticker))
        id_ativo = banco.lastrowid

        arq.commit()

    return id_ativo

def inserir_precos(id_ativo, precos):
    with sqlite3.connect(arquivo_banco) as arq:
        banco = arq.cursor()

        for preco in precos:
            banco.execute("INSERT INTO Precos (id_ativo, preco, data) VALUES (?, ?, ?)", 
                          (id_ativo, preco["price"], preco["date"]))

        arq.commit()

def ler_precos(id_ativo):
    with sqlite3.connect(arquivo_banco) as arq:
        banco = arq.cursor()
        banco.execute('SELECT preco, data FROM Precos WHERE id_ativo=?', (id_ativo,))

        precos = banco.fetchall()
    
    return precos

def ler_ativos():
    with sqlite3.connect(arquivo_banco) as arq:
        banco = arq.cursor()
        banco.execute('SELECT * FROM Ativos')

        ativos = banco.fetchall()
    
    return ativos

def capturar_dados(nome, ticker):
    try:
        precos = obter_precos(ticker)

        if len(precos) == 0:
            st.error(f"Erro ao capturar preços do ativo: {ticker}")
            return 
        
        id_ativo = adicionar_ativo(nome, ticker)
        inserir_precos(id_ativo, precos)
        st.success(f"Ativo adicionado: {ticker} - {nome}")
    except:
        st.error(f"Erro ao capturar preços do ativo: {ticker}")



# ------------------------------------------------------------------------------

def formatar_selectbox(ativo):
    return f'{ativo[1]} - {ativo[2]}'

@st.dialog("Adicionar ativo")
def janela_add_ativo():
    nome = st.text_input("Nome do ativo: ")
    ticker = st.text_input("Código de negociação: ")
    
    if st.button("Adicionar"):
        capturar_dados(nome, ticker)

st.title('Consulta de preços')

col1, col2 = st.columns([9, 1])

ativos = ler_ativos()
ativo_sel = col1.selectbox("Ativo", options=ativos, format_func=formatar_selectbox)

col2.text("")
col2.text("")
if col2.button("➕"):
    janela_add_ativo()


precos = ler_precos(ativo_sel[0])
# st.table(precos)
df_precos = pd.DataFrame(precos, columns=("preço", "data"))
st.line_chart(df_precos, y="preço", x="data")
