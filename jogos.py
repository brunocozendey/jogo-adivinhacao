import forca
import adivinhacao

def escolhe_jogo():
    print('********************************')
    print('******** MENU DE JOGOS *********')
    print('********************************')

    print('Escolha o jogo desejado:')
    jogo = int(input('(1) Forca / (2) Adivinhação\n'))

    if (jogo == 1 ):
        print('Jogando forca')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando adivinhação')
        adivinhacao.jogar()

if (__name__ == "__main__"): #Quando executado pela linha de comando o python associa a classe name o __main__
    escolhe_jogo()


