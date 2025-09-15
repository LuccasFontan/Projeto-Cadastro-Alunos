from functions import cadastro_usuario
import functions

login = [
    {"email":"lucasfontan@gmail.com","senha":"123"},
    ]
turmas = [
    {'turma':"a"},
    ]
alunos = [
    {"nome":"lucas","cpf":"00000000000","matricula":"1","turma":"a","turno":"noturno","email":"lucas@gmail.com","senha":"123"},
    ]   

while True:
    functions.menu()
    option = input("Digite a opção desejada: ") 
    match option: 
        case "1":
            count = 0 
            while count < 3:
                count +=1 
                email = input("Digite o Email: ") 
                senha = input("Digite a Senha: ") 
                validado = False    
                for user in login: 
                    if email == user["email"] and senha == user["senha"]: 
                        validado = True
                        break
                if validado: 
                    print("\nLogado com sucesso!")
                    while True:
                            functions.menu_admin()
                            option = input("Digite a opção desejada: ")
                            match option:
                                case "1":
                                    functions.add_aluno(alunos, turmas)
                                case "2":
                                    functions.cadastrar_turma(turmas)
                                case "3":
                                    functions.listar_alunos(alunos)
                                case "4": 
                                    functions.buscar_aluno(alunos)
                                case "5":
                                    break
                                case "0":
                                    functions.sair()
                                case _:
                                    print("Opção inválida, tente novamente.")
                                    continue
                    break
                else:
                    print("Email ou senha Incorreto!") 
                tentativas_restantes = 3 - count
                if tentativas_restantes > 0:
                    print(f"Você ainda tem {tentativas_restantes} tentativa(s).")
                else:
                    print("Você excedeu o limite de tentativas.")
            if validado: 
                continue 
        case "2":
            email = input("Digite o Email: ").lower() 
            senha = input("Digite a senha: ") 
            cadastro_usuario(login, email, senha)
            continue
        case "3":
            functions.sair()
        case _: 
            print("Opção inválida, tente novamente.")
            continue
        
        
                
            
        
        
    