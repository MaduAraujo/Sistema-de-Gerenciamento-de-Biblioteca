import streamlit as st
import pandas as pd

# Lista de livros (título, autor, codigo, e um novo campo para status de empréstimo)
if 'livros' not in st.session_state:
    st.session_state.livros = []

# Função para registrar um novo livro no sistema
def registrar_livros(titulo, autor, codigo):
    # Verifica se o livro já existe pelo título ou código
    for livro in st.session_state.livros:
        if livro["Titulo"].lower() == titulo.lower() or livro["Código"].lower() == codigo.lower():
            st.warning(f"O livro '{titulo}' com o código '{codigo}' já existe no acervo.")
            return False
    st.session_state.livros.append({"Titulo": titulo, "Autor": autor, "Código": codigo, "Emprestado": False})
    st.success(f"Livro '{titulo}' registrado com sucesso!")
    return True

# Função para emprestar um livro
def emprestar_livros(titulo):
    found = False
    for livro in st.session_state.livros:
        if livro["Titulo"].lower() == titulo.lower():
            if not livro["Emprestado"]:
                livro["Emprestado"] = True
                st.success(f"Empréstimo do livro '{titulo}' realizado com sucesso!")
            else:
                st.warning(f"O livro '{titulo}' já está emprestado.")
            found = True
            break
    if not found:
        st.error("Livro não encontrado no acervo.")

# Função para devolver um livro
def devolver_livros(titulo):
    found = False
    for livro in st.session_state.livros:
        if livro["Titulo"].lower() == titulo.lower():
            if livro["Emprestado"]:
                livro["Emprestado"] = False
                st.success(f"Devolução do livro '{titulo}' realizada com sucesso!")
            else:
                st.warning(f"O livro '{titulo}' não estava emprestado.")
            found = True
            break
    if not found:
        st.error("Livro não encontrado no acervo.")

# Função para consultar o acervo
def consultar_acervo():
    return st.session_state.livros

## Interface Streamlit

st.set_page_config(page_title="Sistema de Gerenciamento de Livros", layout="wide")

st.title("📚 Sistema de Gerenciamento de Livros")

# Barra lateral para navegação
st.sidebar.header("Navegação")
opcao = st.sidebar.radio("Escolha uma opção:", ["Registrar Livro", "Emprestar Livro", "Devolver Livro", "Consultar Acervo"])

if opcao == "Registrar Livro":
    st.header("📖 Registrar Novo Livro")
    with st.form("registro_livro"):
        titulo = st.text_input("Título do Livro").strip()
        autor = st.text_input("Autor do Livro").strip()
        codigo = st.text_input("Código do Livro").strip()
        submitted = st.form_submit_button("Registrar")
        if submitted:
            if titulo and autor and codigo:
                registrar_livros(titulo, autor, codigo)
            else:
                st.error("Preencha todos os campos para registrar o livro.")

elif opcao == "Emprestar Livro":
    st.header("📤 Emprestar Livro")
    with st.form("emprestimo_livro"):
        titulo_emprestar = st.text_input("Título do Livro a ser emprestado").strip()
        submitted = st.form_submit_button("Emprestar")
        if submitted:
            if titulo_emprestar:
                emprestar_livros(titulo_emprestar)
            else:
                st.error("Digite o título do livro para emprestar.")

elif opcao == "Devolver Livro":
    st.header("📥 Devolver Livro")
    with st.form("devolucao_livro"):
        titulo_devolver = st.text_input("Título do Livro a ser devolvido").strip()
        submitted = st.form_submit_button("Devolver")
        if submitted:
            if titulo_devolver:
                devolver_livros(titulo_devolver)
            else:
                st.error("Digite o título do livro para devolver.")

elif opcao == "Consultar Acervo":
    st.header("📚 Acervo de Livros")
    livros_disponiveis = consultar_acervo()
    if livros_disponiveis:
        df = pd.DataFrame(livros_disponiveis)
        df['Status'] = df['Emprestado'].apply(lambda x: "Emprestado" if x else "Disponível")
        df_display = df[['Titulo', 'Autor', 'Código', 'Status']]
        st.dataframe(df_display, use_container_width=True)
    else:
        st.info("Nenhum livro registrado no acervo ainda.")