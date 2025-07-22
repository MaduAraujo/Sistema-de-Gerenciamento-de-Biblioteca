# Lista de livros (título, autor, codigo)

livros = []

# Função para registrar um novo livro no sistema

def registrar_livros(titulo, autor, codigo):
  livros.append({"Titulo": titulo, "Autor": autor, "Código": codigo})
  print(f"Livro '{titulo}' registrado com sucesso!")

# Função para emprestar um livro

def emprestar_livros(livro):

    for livro in livros:
      if livro["Titulo"] == titulo:
        print(f"Empréstimo do livro '{titulo}' realizado com sucesso!")
        return
    print("Livro não encontrado ou já emprestado.")

#Função para devolver um livro

def devolver_livros(livro):

    for livro in livros:
      if livro["Titulo"] == titulo:
        print(f"Devolução do livro '{titulo}' realizado com sucesso!")
        return
    print("Livro Recebido ou Não consta no acervo")

# Função para consultar o acervo

def consultar_acervo():
    return livros
    
# Menu Principal

while True:
    print("\nOpções:")
    print("1. Registrar Livro")
    print("2. Emprestar Livro")
    print("3. Devolver Livro")
    print("4. Consultar Acervo")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
      titulo = input("Digite o título do livro: ")
      autor = input("Digite o autor do livro: ")
      codigo = input("Digite o código do livro: ")
      registrar_livros(titulo, autor, codigo)
    elif opcao == "2":
      titulo = input("Digite o título do livro a ser emprestado: ")
      emprestar_livros(livros)
    elif opcao == "3":
      titulo = input("Digite o titulo do livro a ser devolvido:")
      devolver_livros(livros)
    elif opcao == "4":
      print("Acervo:")
      for livro in consultar_acervo():
        print(f"{livro['Titulo']}")
    elif opcao == "5":
        print("Saindo.")
        break
    else:
      print("Opção inválida.")
    
    
