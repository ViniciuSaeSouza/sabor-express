import os

restaurantes = [{'nome':'Praça Sushi', 'categoria':'Japonesa', 'ativo':False} , 
                {'nome':'Pizza Express', 'categoria':'Pizzaria', 'ativo':True} , 
                {'nome':'BurgerMax', 'categoria':'Lanches', 'ativo':False},
                {'nome':'Cantina Pepe', 'categoria':'Italiano', 'ativo':True}]

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
      print('3. Ativar ou desativar restaurante')
      print('4. Sair\n')
      
def exibir_subtitulo(texto):
      os.system('cls')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(f'{linha}\n')

            
def voltar_ao_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal: ')
      main()

def cadastrar_novo_restaurante():
      exibir_subtitulo('Cadastro de novos restaurantes')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulo('Restaurantes Listados:')
      print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status do restaurante")
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativo' if restaurante['ativo'] else 'desativado'
           
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')     
      voltar_ao_menu_principal()
      
def ativar_desativar_restaurante():
      exibir_subtitulo('Alterando Status do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
      restaurante_encontrado = False
      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)
      if not restaurante_encontrado:
            print('O restaurante não foi encontrado')
      voltar_ao_menu_principal()

def opcao_invalida():
      print('Opção Inválida\n')
      voltar_ao_menu_principal()
      
def finalizar_app():
      exibir_subtitulo('Finalizando App')

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                  case 1:
                        cadastrar_novo_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        ativar_desativar_restaurante()
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