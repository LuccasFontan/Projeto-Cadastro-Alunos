turmas = [
    {'turma':"a"}
]

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
cadastrar_turma(turmas)

def f_turma(turmas):
    for i in turmas:
        print(i["turma"])
        
f_turma(turmas)
print(turmas)