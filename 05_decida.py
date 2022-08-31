import random
import PySimpleGUI as sg

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
        # Como vai ficar a janela ou o layout dela
        layout = [
            [sg.Text('Faça qualquer pergunta: ')],
            [sg.Input()],
            [sg.Button("Decida")],
            [sg.Output(size=(40,10))]
        ]
        # criar a janela
        self.janela = sg.Window('Decida por Mim!!',layout=layout)    
        
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.eventos == sg.WIN_CLOSED:
                break
            if self.eventos == 'Decida':
                print(random.choice(self.respostas))
              
decida = Decida()
decida.Iniciar()            