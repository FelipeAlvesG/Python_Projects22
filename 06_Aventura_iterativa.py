#A intenção é um jogo com varios finais diferentes,
# tudo leva como base a resposta do jogador.
#Baseado no projeto do Jhonatan

import PySimpleGUI as sg
class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte eu ou sul? (n/s)' # norte = LadoA, sul = LadoB
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' # espada = Lado1, escudo = Lado2
        self.pergunta3 = 'Qual é a sua especialidade?(linha de frente/tatico)' # linha de frente = Lado1, tático = Lado2
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'

        
    def Iniciar(self):
        # Layout
        layout = [
            #[sg.Output(size=(20,5))],
            [sg.Text(self.pergunta1),sg.Output(size=(20,5))],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        # criar a janela
        self.janela = sg.Window('Jogo de Aventura!',layout=layout)
        while True:
            # ler os dados
            self.LerValores()
            if self.evento == sg.WIN_CLOSED:
                break
            # fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria4)
        
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()


jogo = JogoDeAventura()
jogo.Iniciar()