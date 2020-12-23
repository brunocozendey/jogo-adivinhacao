from random import randrange 

print('********************************')
print('Bem vindo ao jogo de adivinhação')
print('********************************')

numero_secreto = randrange(1,101)
n_tentativas = 6
pontos = 1000

print('Qual o nível de dificuldade?')
print('1 - Fácil')
print('2 - Médio')
print('3 - Difícil')
nivel = int(input('Defina o nível: '))

if ( nivel == 1 ):
    n_tentativas = 20
elif ( nivel == 2):
    n_tentativas = 10
else:
    n_tentativas = 5

for i in range(1,n_tentativas+1):
    
    chute = int(input('Advinhe o número de 1 a 100: '))
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    n_tentativas_restantes = n_tentativas-i

    print('Você digitou ',chute)
    if (acertou):
        print('Você acertou o número é {}!'.format(numero_secreto))
        break
    else:
        if (maior):
            print('Você errou! Seu chute foi maior que o número secreto! :(')
        else:
            print('Você errou! Seu chute foi menor que o número secreto! :(')
        print('Você ainda tem {} tentativas'.format(n_tentativas_restantes))
        if (n_tentativas_restantes == 0):
            print('Você perdeu :( e o numero secreto era {}'.format(numero_secreto))

print("Fim do Jogo!")