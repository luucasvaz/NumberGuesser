import numpy as np

tentativas = range(1, 10)
numero = np.random.randint(0, 100)
chute = int(input('Chute o número que eu pensei (0 a 100). Você tem 10 tentativas.'))

for i in tentativas:
    if chute < numero:
        print('Seu chute está baixo.')
        chute = int(input('Chute um novo número mais alto:'))
    elif chute > numero:
        print('Seu chute está alto.')
        chute = int(input('Chute um novo número mais baixo:'))
    else:
        print('Correto!')
        break
