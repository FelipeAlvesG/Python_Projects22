#Criando um Chute de numero sem nada visual

import random

class ChuteONumero:
    def __init__(self):
        self.valor_random = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentarDenovo = True
    
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValor()
        try:
            while self.tentarDenovo == True: 
                if int(self.chute) > self.valor_random:
                    print('Chute um valor mais baixo!!')
                    self.PedirValor()
                elif int(self.chute) < self.valor_random:
                    print('Chute um valor mais alto!!')
                    self.PedirValor()
                if int(self.chute) == self.valor_random:
                    self.tentarDenovo = False
                    print('VOCÊ ACERTOU O NUMERO!!')
        except:
            print('Favor digitar somente números!')
            self.Iniciar()            

    def PedirValor(self):
        self.chute = input('Chute um numero: ')
    
        
    def GerarNumeroAleatorio(self):
        self.valor_random = random.randint(self.valor_min,self.valor_max)
        
chute = ChuteONumero()
chute.Iniciar()    
    