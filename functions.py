auto_id = 0

def cadastro_usuario(login, email, senha): 
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
    [2] Abrir nova turma
    [3] Remover aluno
    [4] Mostrar média
    [5] Listar alunos
    [6] Atualizar aluno
    [0] Sair
    =============================  
    """)

def add_aluno(alunos,turmas, login):
    print("\nCadastro de Login")
    email = input("Digite o Email: ").lower() 
    senha = input("Digite a senha: ") 
    cadastro_usuario(login, email, senha)
    print("\nCadastro de dados do aluno")
    nome = f_nome()
    cpf = f_cpf()
    matricula = gerar_matricula()
    turma = f_turma(turmas)
    turno = f_turno()
    alunos.append({"nome":nome,"cpf":cpf,"matricula":matricula,"turma":turma,"curso":curso,"turno":turno})
    print("Aluno adicionado com sucesso!")
    print(alunos)
    
def cadastrar_turma(turmas):
    while True:
        turma = input("Digite a turma: ").lower()
        for i in turmas:
            if i["turma"] == turma:
                print("Turma ja cadastrada!")
            else:
                turmas.append({"turma":turma})
                print("Turma cadastrada.")    
                return False
    
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

def f_turma(turmas):
    while True:
        turma = input("Digite a turma: ").lower()
        if turma["turma"] in turmas:
            break
        else:
            print("Turma não encontrada.")
    return turma

def f_turma(turmas):
    while True:
        turma_digitada = input("Digite a turma: ").lower()
        turma_valida = False
        for t in turmas:
            if t["turma"] == turma_digitada:
                turma_valida = True
                break  
        if turma_valida:
            return turma_digitada
        else:
            print("Turma inválida! Turmas disponíveis:")
            print(", ".join(t["turma"] for t in turmas))
