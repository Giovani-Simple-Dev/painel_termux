import requests
from colorama import init, Fore
from time import sleep
import os


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

def exibir_banner():
    banner = """
██████╗  █████╗ ██╗███╗   ██╗███████╗██╗         ██████╗ ███████╗     ██████╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗  ████████╗ █████╗ ███████╗
██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║         ██╔══██╗██╔════╝    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗██╔════╝
██████╔╝███████║██║██╔██╗ ██║█████╗  ██║         ██║  ██║█████╗      ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     ██║   ███████║███████╗
██╔═══╝ ██╔══██║██║██║╚██╗██║██╔══╝  ██║         ██║  ██║██╔══╝      ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██║   ██╔══██║╚════██║
██║     ██║  ██║██║██║ ╚████║███████╗███████╗    ██████╔╝███████╗    ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██║   ██║  ██║███████║
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚══════╝
    """
    print(banner)

# Chamar a função para exibir o banner
exibir_banner()



def menu():
  while True:
    cls()
    print(Fore.GREEN + "1. Consultar IP [+_+]")
    print(Fore.GREEN + "2. Consultar CEP [+_+]")
    print(Fore.GREEN + "3. Consultar CNPJ [+_+]")
    print(Fore.GREEN + "4. Consultar Bancos [+_+]")
    print(Fore.GREEN + "5. Consultar BIN [+_+]")
    print(Fore.CYAN + "0. Sair [=(]")
    choice = input("Digite a opção: ")

    if choice == "1":
      consultar_ip()
    elif choice == "2":
      consultar_cep()
    elif choice == "3":
      consultar_cnpj()
    elif choice == "4":
      consultar_banco()
    elif choice == "5":
      consultar_bin()
    elif choice == "0":
      print("Saindo...")
      break
    else: 
      print("Opção inválida")
      sleep(2)

def consultar_ip():
  ip = input("Digite o IP: ")
  response = requests.get(f"http://ip-api.com/json/{ip}")
  data = response.json()
  if response.status_code == 200:
    print(f"STATUS: {data['status']}")
    print(f"CODIGO DO PAIS: {data['countryCode']}")
    print(f"TIMEZONE: {data['timezone']}")
    print(f"ZIP: {data['zip']}")
    print(f"ISP: {data['isp']}")
    print(f"IP: {data['query']}")
    print(f"País: {data['country']}")
    print(f"Região: {data['region']}")
    print(f"Cidade: {data['city']}")
    print(f"AS: {data['as']}")
    print(f"ORG: {data['org']}")
    print(f"LATITUDE: {data['lat']}")
    print(f"LONGITUDE: {data['lon']}")
    
  else:
    print("Erro na consulta do IP.")
  input("Pressione Enter para continuar... ")


def consultar_cep():
  cep = input("Digite o CEP: ")
  response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
  data = response.json()
  if 'erro' not in data:
    print(f"CEP: {data['cep']}")
    print(f"Logradouro: {data['logradouro']}")
    print(f"Bairro: {data['bairro']}")
    print(f"Cidade: {data['localidade']}")
    print(f"Complemento: {data['complemento']}")
    print(f"Estado: {data['uf']}")
    print(f"IBGE: {data['ibge']}")
    print(f"GIA: {data['gia']}")
    print(f"DDD: {data['ddd']}")
    print(f"SIAFI: {data['siafi']}")
  else:
    print("CEP inválido.")
  input("Pressione Enter para continuar...")


    

def consultar_feriados():
  ano = input("Digite o Ano: ")
  response = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{ano}")
  feriados = response.json()
  if response.status_code == 200:
    for feriado in feriados:

      print(f"Data: {feriado['date']}")
    print(f"Nome: {feriado['name']}")
    print("-" * 20)
  else:
    print("Erro ao consultar feriados")
  input("Pressione Enter para continuar...")

def consultar_cnpj():
  cnpj = input("Digite o CNPJ: ")
  response = requests.get(f"https://receitaws.com.br/v1/cnpj/{cnpj}")
  data = response.json()
  if response.status_code == 200:
    
      print(f"STATUS: {data['status']}")
      print(f"CNPJ: {data['cnpj']}")
      print(f"Logradouro: {data['logradouro']}")
      print(f"Tipo: {data['tipo']}")
      print(f"Porte: {data['porte']}")
      print(f"Nome: {data['nome']}")
      print(f"Nome Social: {data['fantasia']}")
      print(f"Abertura: {data['abertura']}")
      print(f"Numero: {data['numero']}")
      print(f"Completemento: {data['complemento']}")
      print(f"CEP: {data['cep']}")
      print(f"Bairro: {data['bairro']}")
      print(f"Municipio: {data['municipio']}")
      print(f"Estado: {data['uf']}")
      print(f"EMAIL: {data['email']}")
      print(f"Telefone: {data['telefone']}")
      print(f"Situação: {data['situacao']}")
      print(f"Data de Situação: {data['data_situacao']}") 
      print(f"Capital Social: {data['capital_social']}")
      print(f"QSA: {data.get('nome')}")
      print(f"Natureza Juridica: {data['natureza_juridica']}")
  else:
    print("Erro ao consultar o CNPJ.")
  input("Pressione Enter para continuar...")



def consultar_ddd():
  ddd = input("Digite o DDD: ")
  response = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}")
  data = response.json()
  if response.status_code == 200:
    print(f"Estado: {data['state']}")
    print(f"Cidades com o mesmo DDD: {data['cities']}")
  else:
    print("Erro ao consultar o DDD")
  input("Pressione Enter para continuar...")






def consultar_banco():
  code = input("Digite o código do banco(Exemplo: Código 1, Código 2): ")
  response = requests.get(f"https://brasilapi.com.br/api/banks/v1/{code}")
  data = response.json()
  if response.status_code == 200:
    print(f"ISPB: {data['ispb']}")
    print(f"NOME: {data['name']}")
    print(f"CODIGO: {data['code']}")
    print(f"NOME COMPLETO: {data['fullName']}")
  else:
    print("Erro ao consultar o banco")
  input("Pressione Enter para continuar...")

def consultar_bin():
  bin = input("Digite o código bin (45717360): ")
  response = requests.get(f"https://lookup.binlist.net/{bin}")
  data = response.json()
  if response.status_code == 200:
    print(f"Numero: {data.get('number', {}).get('length')}")
    print(f"Cartao Valido: {data.get('numeber', {}).get('luhn')}")
    print(f"Marca: {data.get('brand')}")
    print(f"Esquema: {data.get('scheme')}")
    print(f"Tipo: {data.get('type')}")
    print(f"País: {data.get('country', {}).get('name')}")
    print(f"Banco: {data.get('bank', {}).get('name')}")
    print(f"URL do Banco: {data.get('bank', {}).get('url')}")
    print(f"Telefone do Banco: {data.get('bank', {}).get('phone')}")
    print(f"Cidade do Banco: {data.get('bank', {}).get('city')}")
  input("Pressione Enter para continuar...")

if __name__ == "__main__":
  menu()