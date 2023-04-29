from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        fabricacao_mais_antiga = min(
            product["data_de_fabricacao"] for product in products
        )
        validade_mais_proxima = min(
            product["data_de_validade"]
            for product in products
            if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        )
        empresas = list(product["nome_da_empresa"] for product in products)
        empresa_mais_produtos = max(empresas, key=lambda x: empresas.count(x))

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}"
        )
