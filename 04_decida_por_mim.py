import random

class Decida:
    def __init__(self):
        self.respostas= [
            'Claro que sim',
            'Não faz isso',
            'Beleza, cara!',
            'Opa, Tranquilo',
            'Chupeu e Irineu, vc não sabe imagina eu!'
        ]
        
    def Iniciar(self):
        input('Faça qualquer pergunta: ')
        print(random.choice(self.respostas))
        
decida = Decida()
decida.Iniciar()            