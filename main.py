import os

mensagens = []

nome = input("Nome: ")

while True:

    #limpando terminal 
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("______________________")

    # obter texto
    texto = input("Mensagem: ")
    if texto == "fim":
                break

    #adicionar menssagem a lista
    mensagens.append({
    "nome": nome,
    "texto": texto
    })
            