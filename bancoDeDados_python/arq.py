# https://dontpad.com/streamlit3103
import streamlit as st
import sqlite3

st.title("Gerenciador de notas")

# def abrir_banco():
#     arquivo_bd = sqlite3.connect("banco.db")
#     banco = arquivo_bd.cursor()
#     return arquivo_bd, banco

def lista_de_alunos():
    with sqlite3.connect("banco.db") as arq:
        banco = arq.cursor()
        banco.execute("""
            SELECT 
            Alunos.id, nome, email, 
            MAX(CASE WHEN Notas.bimestre = 1 THEN nota ELSE NULL END) AS nota_1,
            MAX(CASE WHEN Notas.bimestre = 2 THEN nota ELSE NULL END) AS nota_2,
            MAX(CASE WHEN Notas.bimestre = 3 THEN nota ELSE NULL END) AS nota_3,
            MAX(CASE WHEN Notas.bimestre = 4 THEN nota ELSE NULL END) AS nota_4
            FROM Alunos JOIN Notas ON Alunos.id = Notas.id_aluno
            GROUP BY Alunos.id;
        """)
        
        alunos = banco.fetchall()

    return alunos

def adicionar_aluno(nome, email, notas):

    try:
        with sqlite3.connect("banco.db") as arq:
            banco = arq.cursor()
            banco.execute("INSERT INTO Alunos (nome, email) VALUES (?, ?)", (nome, email))

            id_aluno = banco.lastrowid

            banco.execute("""
                INSERT INTO Notas (id_aluno, bimestre, nota)
                VALUES 
                (?, 1, ?),
                (?, 2, ?),
                (?, 3, ?),
                (?, 4, ?)
                """, 
                (id_aluno, notas[0],
                 id_aluno, notas[1],
                 id_aluno, notas[2],
                 id_aluno, notas[3])
            )
            
        st.success(f"Aluno adicionado: {nome} - {email}")
    except Exception as error:
        st.error(f"Falha ao adicionar aluno: {error}")

def remover_aluno(id):
    try:
        with sqlite3.connect("banco.db") as arq:
            banco = arq.cursor()
            banco.execute("SELECT nome FROM Alunos WHERE id = ?", (id,))
            aluno = banco.fetchone()

            if aluno is not None:
                banco.execute("DELETE FROM Alunos WHERE id = ?", (id,))
                st.success(f"Aluno removido: {aluno[0]}")
            else:
                st.warning(f"Aluno com ID {id} não existe")

    except Exception as error:
        st.error(f"Falha ao remover aluno: {error}")

# ---------------------------------------------------------
# STREAMLIT -
# ---------------------------------------------------------

@st.dialog("Adicionar aluno")
def janela_add_aluno():
    nome = st.text_input("Nome: ")
    email = st.text_input("Email: ")

    col1, col2, col3, col4 = st.columns(4)
    nota_1 = col1.number_input("Nota 1", min_value=0, max_value=10)
    nota_2 = col2.number_input("Nota 2", min_value=0, max_value=10)
    nota_3 = col3.number_input("Nota 3", min_value=0, max_value=10)
    nota_4 = col4.number_input("Nota 4", min_value=0, max_value=10)

    if st.button("Adicionar"):
        # adicionar aluno
        notas = [nota_1, nota_2, nota_3, nota_4]
        adicionar_aluno(nome, email, notas)

@st.dialog("Remover aluno")
def janela_rm_aluno():
    id = st.number_input("ID: ", step=1)
    if st.button("Remover"):
        # Remover aluno
        remover_aluno(id)

col1, col2 = st.columns(2)
# Coluna da esquerda
with col1:
    if st.button("Adicionar aluno", use_container_width=True):
        janela_add_aluno()
# Coluna da direita
with col2:
    if st.button("Remover aluno", use_container_width=True):
        janela_rm_aluno()

alunos = lista_de_alunos()
st.table(alunos)

# arquivo_bd.close()