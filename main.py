import os

#        for c in range(0, len(tarefas_pendentes)):
#            print(f"({c+1}) {tarefas_pendentes[c]}")
#        concluir = input("Digite o numero da tarefa pra conclui-la: ")
#        tarefas_pendentes.remove(tarefas_pendentes[concluir-1])
#        input("Tarefa concluida com sucesso!\n\nPressione enter pra continuar . . .")
#        os.system('cls')




print("\033[31m")
tarefas_pendentes = ["Matematica", "Geografia","Portugues"]

usuarios = []
senhas = []


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
    print("""(1) Usuarios\n(2) Listar tarefas\n(3) Adicionar Tarefas\n(4) Concluir Tarefas\n\n""")
    escolha = str(input("\nDigite a opção: "))

    if escolha == "1":
        pu = input("(1) Novo usuario\n(2) Ver usuarios\n\nescolha: ")

        if pu == "1":
            l_usuario = input("Digite o seu nome de usuario: ")
            l_senha = input("Digite sua senha: ")

            usuarios.append(l_usuario)
            senhas.append(l_senha)

            print("\nUsuario adicionado com sucesso!")
            input("\n\nPressione enter para continuar . . .")
            os.system('cls')

        if pu == "2":
            if len(usuarios) > 0:
                for c in range(0,len(usuarios)):
                    print(f"({c+1}){usuarios[c]}")
                input("\n\nPressione enter para continuar . . .")
                os.system('cls')

            else:
                print("Nenhum usuario encontrado!\n\nPressione enter para continuar . . .")
                input()
       

    if escolha == "2":
        print("\n")
        for c in range(0,len(tarefas_pendentes)):
            print(f"({c+1}) {tarefas_pendentes[c]}")
        input("\n\nPressione enter para continuar . . .")
        os.system('cls')

    
    elif escolha == "3":
        adicionar = input("Digite o nome da tarefa que deseja adicionar: ")
        tarefas_pendentes.append(adicionar)
        print("tarefas adicionadas com sucesso!")
        input("Pressione enter para continuar . . .")
        os.system('cls')

    elif escolha == "4":
        sair = input("Deseja realmente sair?\n(S|N): ")
        if sair.lower() == "s":
            break
    else:
        input("Comando não encontrado!\n\nPressione enter para continuar . . .")
        os.system("cls")

print("Programa finalizado!\n\n")