# 📚 Sistema de Gerenciamento de Livros

Um sistema simples e intuitivo para gerenciar o acervo de livros, permitindo registrar novos livros, controlar empréstimos e devoluções, e consultar o status de cada item. 
Este projeto oferece duas interfaces: uma **versão interativa baseada em console** e uma **interface gráfica intuitiva desenvolvida com Streamlit**.

## 🚀 Funcionalidades

  * **Registro de Livros:** Adicione novos livros ao acervo com informações como título, autor e código.
  * **Empréstimo de Livros:** Marque livros como emprestados (na versão Streamlit, o status é atualizado; na versão console, é uma mensagem de confirmação).
  * **Devolução de Livros:** Registre a devolução de livros (na versão Streamlit, o status é atualizado; na versão console, é uma mensagem de confirmação).
  * **Consulta de Acervo:** Visualize todos os livros registrados, seus autores, códigos e o status atual (disponível ou emprestado na versão Streamlit).

## 🛠️ Tecnologias Utilizadas

### Para a Versão com Interface Gráfica (Streamlit)

  * **Python:** Linguagem de programação principal.
  * **Streamlit:** Framework para criação de interfaces web interativas.
  * **Pandas:** Biblioteca para manipulação e análise de dados, utilizada para exibir o acervo em formato de tabela.

### Para a Versão de Console

  * **Python:** Linguagem de programação principal.

## ⚙️ Como Executar o Projeto

Você pode executar o projeto em duas versões: **interface gráfica (Streamlit)** ou **apenas no console**.

### Pré-requisitos

Certifique-se de ter o **Python** (versão 3.7 ou superior) instalado em seu sistema.

### 1\. Clonar o Repositório (ou baixar os arquivos)

Se o código estiver em um repositório Git, clone-o:

```bash
git clone https://github.com/MaduAraujo/Sistema-de-Gerenciamento-de-Biblioteca
cd Sistema-de-Gerenciamento-de-Biblioteca
```

### Executando a Versão com Interface Gráfica (Streamlit)

Esta versão oferece uma interface web interativa.

#### 2.1. Instalar Dependências

Navegue até o diretório do projeto e instale as bibliotecas necessárias usando `pip`:

```bash
pip install streamlit pandas
```

#### 2.2. Executar o Aplicativo Streamlit

Após a instalação das dependências, execute o aplicativo Streamlit a partir do terminal:

```bash
streamlit run App.py
```

Isso abrirá automaticamente o aplicativo em seu navegador padrão. Se não abrir, copie e cole o URL fornecido no terminal em seu navegador.

### Executando a Versão de Console

Esta versão é executada diretamente no terminal.

#### 2.1. Executar o Aplicativo de Console

Navegue até o diretório do projeto e execute o arquivo Python diretamente:

```bash
python Projeto Colaborativo.py
```

O programa será iniciado no seu terminal, apresentando um menu de opções.

## 📖 Como Usar

### Usando a Versão com Interface Gráfica (Streamlit)

A interface do usuário é dividida em seções acessíveis através da **barra lateral** à esquerda:

1.  **Registrar Livro:** Preencha os campos **"Título do Livro"**, **"Autor do Livro"** e **"Código do Livro"** e clique em **"Registrar"**. O sistema verificará duplicatas.
2.  **Emprestar Livro:** Digite o **"Título do Livro a ser emprestado"** e clique em **"Emprestar"**. O status do livro será atualizado.
3.  **Devolver Livro:** Digite o **"Título do Livro a ser devolvido"** e clique em **"Devolver"**. O status do livro será atualizado.
4.  **Consultar Acervo:** Visualize uma tabela com todos os livros registrados, incluindo Título, Autor, Código e **Status** (Disponível ou Emprestado).

### Usando a Versão de Console

Ao executar o `Projeto Colaborativo.py`, você verá um menu de opções no terminal:

```
Opções:
1. Registrar Livro
2. Emprestar Livro
3. Devolver Livro
4. Consultar Acervo
5. Sair
```

1.  **Registrar Livro:** Digite `1`, e em seguida, insira o título, autor e código quando solicitado.
2.  **Emprestar Livro:** Digite `2`, e em seguida, insira o título do livro a ser emprestado.
3.  **Devolver Livro:** Digite `3`, e em seguida, insira o título do livro a ser devolvido.
4.  **Consultar Acervo:** Digite `4` para ver a lista de livros registrados.
5.  **Sair:** Digite `5` para encerrar o programa.

-----

## ⚠️ Observações Importantes

  * **Persistência de Dados:** Para ambas as versões, os dados dos livros são armazenados apenas na memória da aplicação e serão **perdidos toda vez que o aplicativo for reiniciado**. Para um sistema de produção, seria necessário integrar um banco de dados persistente (SQLite, PostgreSQL, etc.).
  * **Validações (Versão Console):** A versão de console possui validações mais básicas para empréstimo e devolução, não controlando o status de "emprestado" como a versão Streamlit.
  * **Sensibilidade a Maiúsculas/Minúsculas:** O campo "Código" (na versão Streamlit) e o "Título" (para todas as operações na versão Streamlit) são tratados como case-insensitive para verificação e busca. Na versão de console, as buscas por título são case-sensitive.
