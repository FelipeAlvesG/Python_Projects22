# Criando um Chute de numero com tela usando biblioteca PySimpleGUI
# Gerar um valor aleatório e não vísivel e eu 
#  tenho que ficar tentando o número até eu acertar
import random
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valor_random = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentarDenovo = True
    
    def Iniciar(self):
        # Como vai ficar a janela ou o layout dela
        layout = [
            [sg.Text('Chute um Numero', size=(20,0))],
            [sg.Input(size=(18,0),key='chute')],
            [sg.Button("CHUTAR!")],
            [sg.Output(size=(39,10))]
        ]
        # criar a janela
        self.janela = sg.Window('Chute o numero!!',layout=layout)
        self.GerarNumeroAleatorio()
        #self.PedirValor()
        try:
            while True:
                # receber e ler os valores digitados
                self.evento, self.valores = self.janela.Read()
                if self.evento==sg.WIN_CLOSED:
                    break
                if self.evento =='CHUTAR!':
                    self.chute = self.valores['chute']
                # Logica
                    while self.tentarDenovo == True: 
                        if int(self.chute) > self.valor_random:
                            print('Chute um valor mais baixo!!')
                            break
                        elif int(self.chute) < self.valor_random:
                            print('Chute um valor mais alto!!')
                            break
                        elif int(self.chute) == self.valor_random:
                            self.tentarDenovo = False
                            print('VOCÊ ACERTOU O NUMERO!!')
                            break
        except:
            print('Favor digitar somente números!')
            self.Iniciar()            
        
    def GerarNumeroAleatorio(self):
        self.valor_random = random.randint(self.valor_min,self.valor_max)
        
chute = ChuteONumero()
chute.Iniciar()    