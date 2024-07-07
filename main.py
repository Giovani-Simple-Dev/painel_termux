import requests

# Substitua pelo endereço IP da sua TV Roku
ROKU_TV_IP = '192.168.15.4'  # Substitua pelo IP da sua TV Roku
BASE_URL = f"http://{ROKU_TV_IP}:8060/keypress/"

# Função para enviar comandos para a TV Roku
def send_command(command):
    try:
        url = BASE_URL + command
        response = requests.post(url)
        if response.status_code == 200:
            print(f"Comando '{command}' enviado com sucesso.")
        else:
            print(f"Falha ao enviar o comando '{command}'. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar o comando '{command}': {e}")

# Menu de comandos
def menu():
    print("Escolha um comando para enviar à TV Roku:")
    print("1. Desligar a TV")
    print("2. Ligar a TV")
    print("3. Aumentar o Volume")
    print("4. Diminuir o Volume")
    print("5. Mudar de Canal (subir)")
    print("6. Mudar de Canal (descer)")
    print("7. Direcional Cima")
    print("8. Direcional Baixo")
    print("9. Direcional Esquerda")
    print("10. Direcional Direita")
    print("11. Botão OK")
    print("12. Botão '*' (Desinstalar app)")
    print("13. Botão Mute")
    print("14. Botão de Retornar")
    print("15. Botão de Avançar")
    print("16. Botão de Play/Pause")
    print("17. Botão Home")
    print("18. Sair")

while True:
    menu()
    choice = input("Digite o número do comando: ")

    if choice == '1':
        send_command('PowerOff')
    elif choice == '2':
        send_command('PowerOn')
    elif choice == '3':
        send_command('VolumeUp')
    elif choice == '4':
        send_command('VolumeDown')
    elif choice == '5':
        send_command('ChannelUp')
    elif choice == '6':
        send_command('ChannelDown')
    elif choice == '7':
        send_command('Up')
    elif choice == '8':
        send_command('Down')
    elif choice == '9':
        send_command('Left')
    elif choice == '10':
        send_command('Right')
    elif choice == '11':
        send_command('Select')
    elif choice == '12':
        send_command('Backspace')
    elif choice == '13':
        send_command('VolumeMute')
    elif choice == '14':
        send_command('Back')
    elif choice == '15':
        send_command('Forward')
    elif choice == '16':
        send_command('Play')
    elif choice == '17':
        send_command('Home')  # Envia o comando para voltar para a tela inicial (Home)
    elif choice == '18':
        print("Saindo...")
        break
    else:
        print("Escolha inválida. Tente novamente.")
