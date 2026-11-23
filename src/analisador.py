
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorDados:

    def __init__(self, caminho_arquivo):

        self.dados = pd.read_csv(
            caminho_arquivo,
            encoding="latin1"
        )

        print("Arquivo carregado com sucesso!")

        # Limpeza dos dados
        self.dados.dropna(
            subset=["Order Date", "Category", "Sales", "Profit"],
            inplace=True
        )

        print("Limpeza dos dados concluída!")

        # Converter data
        self.dados["Order Date"] = pd.to_datetime(
            self.dados["Order Date"]
        )

        # Mostrar colunas
        print("\nColunas da base:")
        print(self.dados.columns.tolist())

    # 1. Estatísticas gerais
    
    # 1. Estatísticas gerais
    def mostrar_estatisticas(self):

        print("\n===== ESTATISTICAS GERAIS =====")

        print("Quantidade de vendas:", len(self.dados))

        print(f"Faturamento total: R$ {self.dados['Sales'].sum():,.2f}")

        print(f"Lucro total: R$ {self.dados['Profit'].sum():,.2f}")

        print(f"Media das vendas: R$ {self.dados['Sales'].mean():,.2f}")

        print(f"Maior venda: R$ {self.dados['Sales'].max():,.2f}")

        print(f"Menor venda: R$ {self.dados['Sales'].min():,.2f}")

    # 2. Vendas por categoria
    def vendas_por_categoria(self):

        resultado = self.dados.groupby(
            "Category"
        )["Sales"].sum()

        print("\n===== VENDAS POR CATEGORIA =====")
        print(resultado)

        return resultado


    # 3. Produtos com maior faturamento
    def produtos_mais_vendidos(self):

        resultado = self.dados.groupby(
            "Product Name"
        )["Sales"].sum()

        resultado = resultado.sort_values(
            ascending=False
        ).head(10)

        print("\n===== 10 PRODUTOS COM MAIOR FATURAMENTO =====")

        for produto, valor in resultado.items():
            print(f"{produto}: R$ {valor:,.2f}")

        return resultado



    # 4. Produtos que geraram mais lucro
    def produtos_mais_lucrativos(self):

        resultado = self.dados.groupby(
            "Product Name"
        )["Profit"].sum()

        resultado = resultado.sort_values(
            ascending=False
        ).head(10)

        print("\n===== 10 PRODUTOS MAIS LUCRATIVOS =====")

        for produto, lucro in resultado.items():
            print(f"{produto}: R$ {lucro:,.2f}")

        return resultado


    # 5. Gráfico de linha
    def grafico_linha(self):

        vendas = self.dados.groupby(
            "Order Date"
        )["Sales"].sum()

        vendas = vendas.sort_index()

        plt.figure(figsize=(10, 5))

        plt.plot(vendas.index, vendas.values)

        plt.title("Vendas ao Longo do Tempo")
        plt.xlabel("Data")
        plt.ylabel("Faturamento")

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 6. Gráfico de barras
    def grafico_barras(self):

        vendas = self.vendas_por_categoria()

        plt.figure(figsize=(10, 5))

        vendas.plot(kind="bar")

        plt.title("Faturamento por Categoria")
        plt.xlabel("Categoria")
        plt.ylabel("Faturamento")

        plt.tight_layout()
        plt.show()

    # 7. Histograma
    def grafico_histograma(self):

        plt.figure(figsize=(10, 5))

        sns.histplot(
            data=self.dados,
            x="Sales",
            bins=20,
            kde=True
        )

        plt.title("Distribuicao das Vendas")
        plt.xlabel("Valor das Vendas")
        plt.ylabel("Quantidade")

        plt.tight_layout()
        plt.show()
