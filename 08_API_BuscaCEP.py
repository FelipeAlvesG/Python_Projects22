#Consumindo uma Api para consultar qualquer CEP pelo "Via CEP"

import requests
import PySimpleGUI as sg
sg.theme('SandyBeach') #Alterando o Tema da tela


class API_CEP:  
    
    def Iniciar(self):
        # Como vai ficar a janela ou o layout dela
        layout = [
            [sg.Text('Digite seu CEP: ')],
            [sg.Input(size=(15,0),key='cep',)],
            [sg.Button("Buscar")],
            [sg.Output(size=(40,10))]
        ]
        # criar a janela
        self.janela = sg.Window('BUSCAR CEP',layout=layout)
        try: 
            while True:
                # Ler os valores
                self.eventos, self.valores = self.janela.Read()
                self.cep = self.valores['cep']
                       
                # Fazer algo com os valores
                if self.eventos == sg.WIN_CLOSED:
                    break
                if self.eventos == 'Buscar':
                    #self.cep = self.valores['cep']
                    self.BuscarCep()
        except:
            print("CEP Inválido")
    
    def BuscarCep(self):
            
        #self.cep = self.cep.replace("-", "").replace(".", "").replace(" ", "")    
        
        if len(self.cep) == 8:
            #puxando dados da API
            link = f'https://viacep.com.br/ws/{self.cep}/json/'
            #Armazenando dados recebidos em uma variavel    
            requisicao = requests.get(link)
            #print(requisicao) #Para tratar erro ao receber a variavel!
            #Salvando em uma variavel para tratar o dicionario recebido
            dic_requisicao = requisicao.json()
            #Extraindo as informações que preciso do CEP
            cp = dic_requisicao['cep']
            uf = dic_requisicao['uf']
            cidade = dic_requisicao['localidade']
            complemento = dic_requisicao['complemento']
            rua = dic_requisicao['logradouro']
            bairro = dic_requisicao['bairro']
            
            #print(dic_requisicao) #Imprimindo o dicionario inteiro
            #imprimindo somente as informações que vamos precisar mostrar!
            print("CEP:",cp,
                "-Rua:",rua,
                "-Bairro:",bairro,
                "-Cidade:",cidade,
                "-Estado:",uf)
        else:
            print("CEP com tamanho inválido")                          
                        
                
decida = API_CEP()
decida.Iniciar()            