from functions import cadastro_usuario
import functions

login = [
    {"email":"admin","senha":"admin"},
]
turmas = [
    {'turma':"a",}
]
alunos = []



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
                    if email == "admin":
                        print("\nAdministrador Logado com sucesso!")
                        while True:
                            functions.menu_admin()
                            option = input("Digite a opção desejada: ")
                            match option:
                                case "1":
                                    functions.add_aluno(alunos, turmas, login,)
                                case "2":
                                    functions.cadastrar_turma(turmas)
                                case "3":
                                    pass
                                case "4": 
                                    pass
                                case "5":
                                    pass
                                case "6":
                                    pass
                                case "0":
                                    functions.sair()
                                case _:
                                    print("Opção inválida, tente novamente.")
                                    continue
                    else:
                        print("Logado com sucesso!")
                    break
                else:
                    print("Email ou senha Incorreto!") 
                tentativas_restantes = 3 - count
                if tentativas_restantes > 0:
                    print(f"Você ainda tem {tentativas_restantes} tentativa(s).")
                else:
                    print("Você excedeu o limite de tentativas.")
            if validado: 
                break
            continue 
        case "2":
            cadastro_usuario(login, email, senha)
            continue
        case "3":
            functions.sair()
        case _: 
            print("Opção inválida, tente novamente.")
            continue
        
        
                
            
        
        
    