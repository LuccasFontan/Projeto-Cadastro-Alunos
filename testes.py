while True:
        turno = input("Digite um turno: ").lower()
        if turno == "matutino" or turno == "vespertino" or turno == "noturno":
            break
        else:
            print("Digite um turno valido! (Matutino, Vespertino, Noturno)")