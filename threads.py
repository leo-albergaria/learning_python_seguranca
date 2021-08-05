import time
from threading import Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.2)
        print('Piloto: {} Km {} '.format(piloto, trajeto))

t_carro_a = Thread(target=carro, args=[2, 'Bruno'])
t_carro_b = Thread(target=carro, args=[2, 'Zezinho'])

t_carro_a.start()
t_carro_b.start()


