from ArvoreAVL import ArvoreAVL
from No import No

def exibir_menu():
    print("\n===== Árvore AVL Interativa =====")
    print("1. Inserir nó")
    print("2. Remover nó")
    print("3. Buscar valor")
    print("4. Mostrar árvore (Pré-ordem)")
    print("5. Mostrar árvore (In-ordem)")
    print("6. Mostrar árvore (Pós-ordem)")
    print("7. Mostrar árvore graficamente")
    print("8. Sair")
    return input("Escolha uma opção: ")

def main():
    arvore = ArvoreAVL()
    raiz = None

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            try:
                valor = int(input("Digite o valor a ser inserido: "))
                raiz = arvore.inserir(raiz, valor)
                print(f"Valor {valor} inserido com sucesso.")
            except ValueError:
                print("Por favor, insira um número inteiro.")

        elif opcao == "2":
            try:
                valor = int(input("Digite o valor a ser removido: "))
                raiz = arvore.remover(raiz, valor)
                print(f"Valor {valor} removido (se existente).")
            except ValueError:
                print("Por favor, insira um número inteiro.")

        elif opcao == "3":
            try:
                valor = int(input("Digite o valor a ser buscado: "))
                no_encontrado = arvore.buscar(raiz, valor)
                if no_encontrado:
                    print(f"Valor {valor} encontrado na árvore.")
                else:
                    print(f"Valor {valor} NÃO encontrado na árvore.")
            except ValueError:
                print("Por favor, insira um número inteiro.")

        elif opcao == "4":
            print("Pré-ordem (VLR):", arvore.pre_ordem_vlr(raiz))

        elif opcao == "5":
            print("In-ordem (LVR):", arvore.in_ordem_lvr(raiz))

        elif opcao == "6":
            print("Pós-ordem (LRV):", arvore.pos_ordem_lrv(raiz))

        elif opcao == "7":
            print("\nÁrvore Graficamente:")
            arvore.imprimir_arvore(raiz)

        elif opcao == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()