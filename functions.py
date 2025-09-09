auto_id = 100

def cadastro_usuario(login): # Fuçao para cadastro do usuario
    email = input("Digite o Email: ").lower() 
    senha = input("Digite a senha: ") 
    for user in login: #Percorre o dicionario para ver se ja esta cadastrado
        if email == user["email"]:
            print("Usuário já cadastrado! Tente outro nome.")
        else: # Caso o usuario nao esteja cadastrado, faz o cadastro
            login.append({"email":email, "senha":senha}) #Cadastro do usuario
            print("\nUsuário cadastrado com sucesso!")
            break 
def sair():
    print("Encerrando...")
    exit()
        
def menu():
    print("""
    =============================
           MENU PRINCIPAL
    =============================
    [1] Login
    [2] Cadastrar-se
    [3] Sair
    =============================
    """)
    
def menu_admin():
    print("""
    =============================
           MENU DE OPÇÕES
    =============================
    [1] Adicionar aluno
    [2] Remover aluno
    [3] Mostrar média
    [4] Listar alunos
    [5] Atualizar aluno
    [0] Sair
    =============================  
    """)

def add_aluno(alunos, login):
    print("\nCadastro de Login")
    cadastro_usuario(login)
    print("\nCadastro de dados do aluno")
    nome = input("Digite o nome: ").lower()
    cpf = input("Digite o CPF: ")
    matricula = gerar_matricula()
    turma = input("Digite a turma: ").lower()
    curso = input("Digite o curso: ").lower()
    turno = input("Digite o turno: ").lower()
    alunos.append({"nome":nome,"cpf":cpf,"matricula":matricula,"turma":turma,"curso":curso,"turno":turno})
    print("Aluno adicionado com sucesso!")
    
    
def gerar_matricula():
    global auto_id
    auto_id +=1
    return auto_id

def retornar_menu():
    opcaomenu = input("Deseja retornar para o Menu? (S/N) ").lower
    
    

