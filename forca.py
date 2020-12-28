from random import randrange 

def jogar():
    
    letras_erradas = []
    acertou = False
    enforcou = False
    tentativa = 0
    
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    print(palavra_secreta)
    palavra_descoberta = gera_palavra_descoberta(palavra_secreta)
    
    while (not acertou and not enforcou):
        imprime_forca(tentativa)
        chute = captura_chute()
        if (chute in palavra_secreta):
            palavra_descoberta = avaliar_chute(chute, palavra_secreta, palavra_descoberta)
            acertou = palavra_secreta == "".join(palavra_descoberta)
        else:
            letras_erradas.append(chute)
            tentativa+=1
            enforcou = tentativa == 6

        imprime_palavra_descoberta(palavra_descoberta)
        imprime_letras_erradas(letras_erradas)
    
    if (enforcou):
        imprime_forca(tentativa)
        imprime_mensagem_perdedor(palavra_secreta)
        
    else:
        imprime_mensagem_vencedor()
    print("Fim do Jogo!")


def mensagem_abertura():
    print('********************************')
    print('***Bem vindo ao jogo de Forca***')
    print('********************************')

def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt","r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    return palavras[randrange(0,len(palavras))].upper()    

def imprime_forca(erros):
    desenho_forca = (
        ['________ ','|        ','|        ','|         '],
        ['________ ','|      O ','|        ','|         '],
        ['________ ','|      O ','|     \  ','|         '],
        ['________ ','|      O ','|     \| ','|         '],
        ['________ ','|      O ','|     \|/','|         '],
        ['________ ','|      O ','|     \|/','|     /   '],
        ['________ ','|      O ','|     \|/','|     / \\']
    )
    desenho_forca_atual = desenho_forca[erros]
    for i in desenho_forca_atual:
        print (i)


def captura_chute():
    chute = ""
    while (len(chute)!=1):
        chute = input('Digite uma letra\n').strip().upper()
    return chute

def avaliar_chute(chute,palavra_secreta, palavra_descoberta):
    for pos in range(0,len(palavra_secreta)):            
        if (palavra_secreta[pos] == chute):
            palavra_descoberta[pos] = chute
    return palavra_descoberta                

def gera_palavra_descoberta(palavra_secreta):
    return list("-"*len(palavra_secreta)) 

def imprime_palavra_descoberta(palavra_descoberta):
    print("".join(palavra_descoberta))

def imprime_letras_erradas(letras_erradas):
    print("Letras erradas:","-".join(letras_erradas))

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if (__name__ == "__main__"): #Quando executado pela linha de comando o python associa a classe name o __main__
    jogar()
