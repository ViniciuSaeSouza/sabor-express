import os

restaurantes = ['Pizza', 'Sushi']

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
      exibir_subtitulo('Finalizando App')
      
def exibir_subtitulo(texto):
      os.system('cls')
      print(f'{texto}\n')
      
def voltar_ao_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal: ')
      main()

def opcao_invalida():
      print('Opção Inválida\n')
      voltar_ao_menu_principal()
      
            
def cadastrar_novo_restaurante():
      exibir_subtitulo('Cadastro de novos restaurantes')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      restaurantes.append(nome_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulo('Restaurantes Listados:')
      for restaurante in restaurantes:
            print(f'-{restaurante}')     
      voltar_ao_menu_principal()

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                  case 1:
                        cadastrar_novo_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        print('Ativar Restaurante')
                  case 4:
                        finalizar_app()
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()
                        
                  
def main():
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()
      

if __name__ == '__main__':
      main()