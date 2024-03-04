import os

def exibir_nome_do_programa():
      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """) #aspas triplas geram uma nova linha, assim como "\n"

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Ativar Restaurante')
      print('4. Sair\n')

def finalizar_app():
      os.system('cls')
      print('Finalizando App\n')

def escolher_opcao():
      opcao_escolhida = int(input('Escolha uma opção: '))
      match opcao_escolhida:
            case 1:
                  print('Cadastrar Restaurante: ')
            case 2:
                  print('Listar Restaurantes')
            case 3:
                  print('Ativar Restaurante')
            case 4:
                  finalizar_app()
            case _:
                  finalizar_app()
                  print('Opção Inválida!')
                  
            
      

def main():
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()
      

if __name__ == '__main__':
      main()