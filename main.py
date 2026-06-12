import os

tarefas_pendentes = []
usuarios = ["Bruno", "Biel", "Biguelo", "Cezar", "Gustavo", "Luan"]
senhas = []
esc = ""

def limpar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def title():
    print(r"""
████████╗ █████╗ ███████╗██╗  ██╗ ███████╗██╗      ██████╗ ██╗    ██╗
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝ ██╔════╝██║     ██╔═══██╗██║    ██║
   ██║   ███████║███████╗█████╔╝  █████╗  ██║     ██║   ██║██║ █╗ ██║
   ██║   ██╔══██║╚════██║██╔═██╗  ██╔══╝  ██║     ██║   ██║██║███╗██║
   ██║   ██║  ██║███████║██║  ██╗ ██║     ███████╗╚██████╔╝╚███╔███╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝
""")  

def line():
    print("===============================================")


print("\033[31m")

def escolha():
    while True:
        print("--- Gerenciador de Tarefas ---")
        print("""
(1) Usuarios
(2) Listar tarefas
(3) Adicionar Tarefas
(0) Concluir Tarefas
            

            """)
        escolha = input("digite a opção: ")

        
        global esc
        esc = escolha
        break



while True:
    print("loop")
    escolha()     
    if esc == "1":
        limpar()
        line()
        print("(1) Novo usuario\n(2) Ver usuarios")
        line()
        pergunta_usuario = input("\n\nescolha: ")

        if pergunta_usuario == "1":
            l_usuario = input("Digite o seu nome de usuario: ")
            l_senha = input("Digite sua senha: ")

            usuarios.append(l_usuario)
            senhas.append(l_senha)

            print("\nUsuario adicionado com sucesso!")
            input("\n\nPressione enter para continuar . . .")
            limpar()

        if pergunta_usuario == "2":
            limpar()
            print("\n--- Lista de Usuarios ---\n")
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
       
    elif esc == "2":
        limpar()

        print("(1) Novo usuario\n(2) Ver usuarios\n")

        escolha_tarefas = input("digite a escolha: ")
        print("\n")
        for c in range(0,len(tarefas_pendentes)):
            print(f"({c+1}) {tarefas_pendentes[c]}")
        input("\n\nPressione enter para continuar . . .")

        limpar()

    
        adicionar = input("Digite o nome da tarefa que deseja adicionar: ")
        tarefas_pendentes.append(adicionar)
        print("tarefas adicionadas com sucesso!")
        input("Pressione enter para continuar . . .")
        limpar()


    elif esc == "0":
        sair = input("Deseja realmente sair?\n(S|N): ")
        if sair.lower() == "s":
            limpar()
            break
    if(esc not in ["0", "1", "2", "3"]):

        input("Comando não encontrado!\n\nPressione enter para continuar . . .")
        limpar()


print("Programa finalizado!\n\n")