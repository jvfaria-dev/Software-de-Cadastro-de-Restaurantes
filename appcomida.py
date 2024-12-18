import os

restaurantes = [{'nome':'Larusso', 'categoria':'Italiana', 'ativo':False},
                {'nome':'CocoBambu', 'categoria':'Francesa', 'ativo':True},
                {'nome':'Outback', 'categoria':'Rodizio', 'ativo':False}]

def exibir_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ██████╗░███████╗  ░█████╗░░█████╗░░██████╗░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  ██║░░██║█████╗░░  ██║░░╚═╝███████║╚█████╗░███████║
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██║░░██║██╔══╝░░  ██║░░██╗██╔══██║░╚═══██╗██╔══██║
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ██████╔╝███████╗  ╚█████╔╝██║░░██║██████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝  ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝ 
""") #Exibição do nome do aplicativo

def perguntas_iniciais():
    print("(1) Cadastrar Restaurante: ")  #Opção de cadastrar restaurante
    print("(2) Lista Restaurante: ")    #Opção de listar os restaurantes já cadastrados
    print("(3) Alternar estado do Restaurante: ")   #Opção de ativar algum restaurante
    print("(4) Sair: \n")     #Sair do aplicativo

def voltar_menu():
    input("Digite uma tecla para voltar ao menu principal. \n")
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def cadastrar():
    exibir_subtitulo("Cadastro de novos restaurantes: ")
    nome_restaurante = input("Digite o nome do restaurante: ")  #Inserir o nome do restaurante
    categoria_restaurante = input(f"Digite a categoria do restaurante: ")    #Inserir a categotia do restaurante
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False} #Controlar os dados dos restaurantes
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado! ")
    voltar_menu()

def listar():
    exibir_subtitulo("Listando os restaurantes: \n")
    for restaurante in restaurantes:
        nome = restaurante['nome']
        print(f"Nome: {nome}")
        categoria = restaurante['categoria']
        print(f"Categoria: {categoria}")
        ativo = restaurante['ativo']
        if ativo is True:
            print("Ativo: O restaurante está ativo!\n")
        else:
            print("O restaurante não está ativo!\n")
    voltar_menu()

def finalizar_app(): 
    exibir_subtitulo("Finalizando app...")

def opção_invalida():
    print("Opção Invalida!")
    voltar_menu()

def alternar_estado():
    exibir_subtitulo("Alternando estado do restaurante:")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo']:
                print(f"O Restaurante {nome_restaurante} foi ativado com sucesso!")
            else:
                print(f"O restaurante {nome_restaurante} foi desativado com sucesso!")
    if not restaurante_encontrado:
        print("Restaurante não encontrado.")
    voltar_menu()

def escolher_opção():    #Escolher as opções
    try:
        opçao_escolhida = int(input("Digite a opção escolhida: "))
        print(f"Você escolheu a opção {opçao_escolhida}\n")
        if opçao_escolhida == 1: 
            cadastrar()
        elif opçao_escolhida == 2:
            listar()
        elif opçao_escolhida == 3:
            alternar_estado()
        elif opçao_escolhida == 4:
            finalizar_app()        
        else:
            opção_invalida()
    except:
        opção_invalida()

def main():
    os.system('cls')
    exibir_programa()
    perguntas_iniciais()
    escolher_opção()

if __name__ == "__main__":
    main()