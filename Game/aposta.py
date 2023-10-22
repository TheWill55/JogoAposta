from random import randint
from colorama import Fore, Back, Style, init


init(autoreset=True)

saldo = float(input('Digite o seu saldo inicial: R$'))

while saldo > 0:
    print(f'Seu saldo atual é: R${saldo:.2f}')

    ge = float(input('Digite o valor da sua aposta: R$'))
    
    if ge > saldo:
        print('Você não tem saldo suficiente para essa aposta.')
        continue

    print('='*50)

    def mostrar_numeros_disponiveis(numero_escolhido):
        print("Números disponíveis:")
        for i in range(1, 26):
            if i in numero_escolhido:
                print(Fore.BLACK + Back.GREEN + f"{i:2d}", end=" ")
            else:
                print(Fore.WHITE + Back.BLACK + f"{i:2d}", end=" ")
            if i % 5 == 0:
                print()

    print('        Aposta        ')
    print('='*50)
    print("""
    Acertos
        6 acertos multiplica 2x
        7 acertos multiplica 5x
        8 acertos multiplica 10x
        9 acertos multiplica 30x
        10 acertos multiplica 60x
        
        BOA SORTE!!!
    """)

    numero_escolhido = []

    while len(numero_escolhido) < 10:
        mostrar_numeros_disponiveis(numero_escolhido)
        numero = int(input(' Escolha um numero: '))
        if 1 <= numero <= 25 and numero not in numero_escolhido:
            numero_escolhido.append(numero)
        else:
            print('Escolha inválida. Por favor, escolha um número entre 1 e 25 que ainda não foi escolhido.')

    numero_escolhido2 = sorted(numero_escolhido)
    print('-' * 50)
    print(f'Números escolhidos {numero_escolhido2}')

    comput = set()
    while len(comput) < 10:
        numero = randint(1, 25)
        comput.add(numero)
    comput2 = sorted(comput)
    print('-' * 50)
    print(f'Números escolhidos pelo computador: {comput2}')

    coincidencias = set(numero_escolhido).intersection(comput)
    num_coincidencias = len(coincidencias)
    ganho = 0
    print('-' * 50)
    if  num_coincidencias == 6:
        ganho = ge * 2
        print(f'Você acertou {num_coincidencias}. ')
        print(f'Ganho de 2x: R${ganho:.2f}')
    elif num_coincidencias == 7:
        ganho = ge * 5
        print(f'Você acertou {num_coincidencias}.')
        print(f'Ganho de 5x: R${ganho:.2f}')
    elif num_coincidencias == 8:
        ganho = ge * 10
        print(f'Você acertou {num_coincidencias}.')
        print(f'Ganho de 10x: R${ganho:.2f}')
    elif num_coincidencias == 9:
        ganho = ge * 30
        print(f'Você acertou {num_coincidencias}.')
        print(f'Ganho de 30x: R${ganho:.2f}')
    elif num_coincidencias == 10:
        ganho = ge * 60
        print(f'Você acertou {num_coincidencias}.')
        print(f'Ganho de 60x: R${ganho:.2f}')
    else:
        print(f'Você acertou {num_coincidencias}.')
        print('Sinto muito, você perdeu a aposta')
    
    # Adiciona o ganho ao saldo
    saldo += ganho
    
    # Desconta o valor da aposta do saldo
    saldo -= ge

    # Verifica se o saldo ficou negativo após a aposta
    if saldo < 0:
        print(f'Seu saldo atual é: R$0.00')
        print('Você não tem mais saldo para apostar. Fim do jogo.')
        break

    continuar = input('Deseja continuar jogando? (s/n): ')
    if continuar.lower() != 's':
        print(f'Seu saldo final é: R${saldo:.2f}')
        print('Obrigado por jogar! Até a próxima.')
        break
