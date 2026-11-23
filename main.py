
from src.analisador import AnalisadorDados


# Criando o objeto da classe
analisador = AnalisadorDados("data/Sample - Superstore.csv")


# Menu principal
while True:

    print("\n================================")
    print("     SISTEMA DE ANALISE DE VENDAS")
    print("================================")
    print("1 - Mostrar estatisticas gerais")
    print("2 - Mostrar vendas por categoria")
    print("3 - Grafico de linha")
    print("4 - Grafico de barras")
    print("5 - Histograma")
    print("6 - Produtos mais vendidos")
    print("7 - Produtos mais lucrativos")
    print("0 - Sair")
    print("================================")

    try:

        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:
            analisador.mostrar_estatisticas()

        elif opcao == 2:
            analisador.vendas_por_categoria()

        elif opcao == 3:
            analisador.grafico_linha()

        elif opcao == 4:
            analisador.grafico_barras()

        elif opcao == 5:
            analisador.grafico_histograma()

        elif opcao == 6:
            analisador.produtos_mais_vendidos()

        elif opcao == 7:
            analisador.produtos_mais_lucrativos()

        elif opcao == 0:
            print("Encerrando o sistema...")
            break

        else:
            print("Opcao invalida! Escolha de 0 a 5.")

    except ValueError:
        print("Erro: digite apenas numeros!")

    except Exception as erro:
        print("Ocorreu um erro:", erro)
