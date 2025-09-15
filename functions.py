auto_id = 1

def cadastro_usuario(login, email, senha): 
    while True:
        if not validar_email(email):
            print("\nE-mail inválido! Digite novamente.\n")
            email = input("Digite o Email: ").lower()
            senha = input("Digite a senha: ")
            continue
        existe = False
        for user in login: 
            if email == user["email"]:
                print("\nE-mail já cadastrado! Tente outro e-mail.\n")
                email = input("Digite o Email: ").lower() 
                senha = input("Digite a senha: ")
                existe = True
                break  
        if not existe:    
            login.append({"email":email, "senha":senha}) 
            print("\nUsuário cadastrado com sucesso!")
            break
        
def cadastro_alunos(alunos, email, senha): 
    while True:
        if not validar_email(email):
            print("\nE-mail inválido! Digite novamente.\n")
            email = input("Digite o Email: ").lower()
            senha = input("Digite a senha: ")
            continue
        existe = False
        for user in alunos: 
            if email == user["email"]:
                print("\nE-mail já cadastrado! Tente outro e-mail.\n")
                email = input("Digite o Email: ").lower() 
                senha = input("Digite a senha: ")
                existe = True
                break  
        if not existe:    
            return email and senha
            
def listar_alunos(alunos):
    print(f"Lista de alunos cadastrados:\n")
    for i in alunos:
        print(f"Nome: {i["nome"]} - Matricula: {i["matricula"]}")
    
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
    [3] Listar alunos
    [4] Buscar aluno
    [5] Retornar ao Menu Principal
    [0] Sair
    =============================  
    """)

def add_aluno(alunos,turmas):
    print("\nCadastro de Login\n")
    email = input("Digite o Email: ").lower() 
    senha = input("Digite a senha: ") 
    cadastro_alunos(alunos,email, senha)
    print("\nCadastro de dados do aluno\n")
    nome = f_nome()
    cpf = f_cpf(alunos)
    matricula = gerar_matricula()
    turma = f_turma(turmas)
    turno = f_turno()
    alunos.append({"nome":nome,"cpf":cpf,"matricula":matricula,"turma":turma,"turno":turno,"email":email,"senha":senha})
    print("\nAluno adicionado com sucesso!\n")
    print(alunos)
    
def cadastrar_turma(turmas):
    while True:
        turma = input("Digite a turma: ").lower()
        for i in turmas:
            if i["turma"] == turma:
                print("\nTurma ja cadastrada!\n")
            else:
                turmas.append({"turma":turma})
                print("\nTurma cadastrada.\n")    
                return False

def buscar_aluno(alunos):
    aluno = input("Digite o aluno que deseja buscar: ").lower()
    for i in alunos:
        if i["nome"] == aluno: 
            print(f"\n|Dados do aluno|\nNome: {i["nome"]}\nCPF: {i["cpf"]}\nMatricula: {i["matricula"]}\nTurma: {i["turma"]}\nTurno: {i["turno"]}\nEmail: {i["email"]}")
        else:
            print("\nAluno não encontrado!\n")
    
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

def f_cpf(alunos):
    while True:
        cpf_input = input("Digite o CPF (somente números): ")
        if not validar_cpf(cpf_input):
            print("\nCPF inválido!\n")
            continue
        cpf_existente = False
        for aluno in alunos:
            if aluno["cpf"] == cpf_input:
                print("Este CPF já está cadastrado!")
                cpf_existente = True
                break
        if cpf_existente:
            continue
        return cpf_input
            
def f_nome():
    while True:
        nome = input("Digite o nome: ").lower()
        if nome.isalpha():
            break
        else:
            print("\nNome pode conter apenas letras!\n")
    return nome
    
def f_turno():
    while True:
        turno = input("Digite um turno: ").lower()
        if turno == "matutino" or turno == "vespertino" or turno == "noturno":
            break
        else:
            print("\nDigite um turno valido! (Matutino, Vespertino, Noturno)\n")
    return turno

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
            print("\nTurma inválida! Turmas disponíveis:")
            print(", ".join(t["turma"] for t in turmas))
            
def validar_email(email: str) -> bool:
    if "@" not in email or "." not in email:
        return False
    if email.startswith("@") or email.endswith("@"):
        return False
    if " " in email or not email.strip():
        return False
    return True
