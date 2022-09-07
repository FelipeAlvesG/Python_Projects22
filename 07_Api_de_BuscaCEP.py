#Api para consultar qualquer CEP via API "Via CEP"

from tokenize import String
import requests


cep = input('Digite seu CEP: ')

cep = cep.replace("-", "").replace(".", "").replace(" ", "")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    print(requisicao)

    dic_requisicao = requisicao.json()

    cp = dic_requisicao['cep']
    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    complemento = dic_requisicao['complemento']
    rua = dic_requisicao['logradouro']
    bairro = dic_requisicao['bairro']
    
    print("CEP:",cp,
          "-Rua:",rua,
          "-Bairro:",bairro,
          "-Estado:",uf)
else:
    print("CEP Inválido")