import streamlit as st
import pandas as pd
import sqlite3

st.title('Gerenciador de banco de dados')

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

def lista_de_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    return alunos

def adicionar_aluno(nome, email):
    cursor.execute("INSERT INTO Alunos (nome, email) VALUES (?, ?)", (nome, email))
    cursor.commit()

@st.dialog("Adicionar Aluno")
def janela_adicionar_aluno():
    nome = st.text_input("Nome")
    email = st.text_input("Email")

    if st.button("Adicionar"):
        adicionar_aluno(nome, email)
        st.success("Aluno adicionado com sucesso!")
    

conn.close()