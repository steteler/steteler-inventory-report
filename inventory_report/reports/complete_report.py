from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        report = SimpleReport.generate(products)
        empresa_quantidade = {
            product["nome_da_empresa"]: 0 for product in products
        }
        for product in products:
            empresa_quantidade[product["nome_da_empresa"]] += 1

        report += "\nProdutos estocados por empresa:\n"
        for empresa, quantidade in empresa_quantidade.items():
            report += f"- {empresa}: {quantidade}\n"

        return report
