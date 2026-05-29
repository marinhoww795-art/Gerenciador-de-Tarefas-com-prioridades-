import os

tarefas_pendentes = []
usuarios = []
senhas = []

def limpar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def line():
    print("=============================================")


print("\033[31m")



while True:
    print(r"""
████████╗ █████╗ ███████╗██╗  ██╗ ███████╗██╗      ██████╗ ██╗    ██╗
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝ ██╔════╝██║     ██╔═══██╗██║    ██║
   ██║   ███████║███████╗█████╔╝  █████╗  ██║     ██║   ██║██║ █╗ ██║
   ██║   ██╔══██║╚════██║██╔═██╗  ██╔══╝  ██║     ██║   ██║██║███╗██║
   ██║   ██║  ██║███████║██║  ██╗ ██║     ███████╗╚██████╔╝╚███╔███╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝
          
""")                                     

    print("--- Gerenciador de Tarefas ---")
    print("""(1) Usuarios\n(2) Listar tarefas\n(3) Adicionar Tarefas\n(0) Concluir Tarefas\n\n""")
    escolha = input("\nDigite a opção: ")

    if escolha == "1":
        limpar()
        line()
        print("(1) Novo usuario\n(2) Ver usuarios")
        line()
        pu = input("\n\nescolha: ")

        if pu == "1":
            l_usuario = input("Digite o seu nome de usuario: ")
            l_senha = input("Digite sua senha: ")

            usuarios.append(l_usuario)
            senhas.append(l_senha)

            print("\nUsuario adicionado com sucesso!")
            input("\n\nPressione enter para continuar . . .")
            limpar()

        if pu == "2":
            line()
            if len(usuarios) > 0:
                for c in range(0,len(usuarios)):
                    print(f"({c+1}){usuarios[c]}")
                    line()
                input("\n\nPressione enter para continuar . . .")
                limpar()

            else:
                print("Nenhum usuario encontrado!\n\nPressione enter para continuar . . .")
                input()
       
    if escolha == "2":
        limpar()
        print("\n")
        for c in range(0,len(tarefas_pendentes)):
            print(f"({c+1}) {tarefas_pendentes[c]}")
        input("\n\nPressione enter para continuar . . .")
        limpar()

    
    elif escolha == "3":
        adicionar = input("Digite o nome da tarefa que deseja adicionar: ")
        tarefas_pendentes.append(adicionar)
        print("tarefas adicionadas com sucesso!")
        input("Pressione enter para continuar . . .")
        limpar()

    elif escolha == "0":
        sair = input("Deseja realmente sair?\n(S|N): ")
        if sair.lower() == "s":
            limpar()
            break
    else:
        input("Comando não encontrado!\n\nPressione enter para continuar . . .")
        limpar()

print("Programa finalizado!\n\n")