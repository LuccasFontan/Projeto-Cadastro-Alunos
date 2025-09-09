auto_id = 0

def cadastro_usuario(login): 
    email = input("Digite o Email: ").lower() 
    senha = input("Digite a senha: ") 
    for user in login: 
        if email == user["email"]:
            print("Usuário já cadastrado! Tente outro nome.")
        else: 
            login.append({"email":email, "senha":senha}) 
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
    nome = f_nome()
    cpf = f_cpf()
    matricula = gerar_matricula()
    turma = f_turma()
    curso = input("Digite o curso: ").lower()
    turno = f_turno()
    alunos.append({"nome":nome,"cpf":cpf,"matricula":matricula,"turma":turma,"curso":curso,"turno":turno})
    print("Aluno adicionado com sucesso!")
    print(alunos)
    
    
def gerar_matricula():
    global auto_id
    auto_id +=1
    return auto_id

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10
    return cpf[-2:] == f"{dig1}{dig2}"

def f_cpf():
    while True:
        cpf_input = input("Digite o CPF (somente números): ")
        if validar_cpf(cpf_input):
            break
        else:
            print("CPF inválido!")
    return cpf_input
            
def f_nome():
    while True:
        nome = input("Digite o nome: ").lower()
        if nome.isalpha():
            break
        else:
            print("Nome pode conter apenas letras!")
    return nome
    
def f_turno():
    while True:
        turno = input("Digite um turno: ").lower()
        if turno == "matutino" or turno == "vespertino" or turno == "noturno":
            break
        else:
            print("Digite um turno valido! (Matutino, Vespertino, Noturno)")
    return turno
def f_turma():
    while True:
        turma = input("Digite a turma: ").lower()
        if turma == "A":
            break
        else:
            print("Digite uma turma valida!")
            print("Turmas dispovineis: ""A"" ")
    return turma
