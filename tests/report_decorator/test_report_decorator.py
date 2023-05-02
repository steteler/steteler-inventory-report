from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

GREEN = "\033[32m"
BLUE = "\033[36m"
RED = "\033[31m"
CLOSE_COLOR = "\033[0m"


product_list = [
    {
        "id": 1,
        "nome_do_produto": "Sabonete líquido",
        "nome_da_empresa": "Natura",
        "data_de_fabricacao": "2022-01-10",
        "data_de_validade": "2024-01-10",
        "numero_de_serie": "0123456789",
        "instrucoes_de_armazenamento": "Armazenar em local seco e arejado",
    },
    {
        "id": 2,
        "nome_do_produto": "Arroz integral",
        "nome_da_empresa": "Tio João",
        "data_de_fabricacao": "2021-12-01",
        "data_de_validade": "2023-12-01",
        "numero_de_serie": "9876543210",
        "instrucoes_de_armazenamento": "Manter em local fresco e seco",
    },
    {
        "id": 3,
        "nome_do_produto": "Lâmpada LED",
        "nome_da_empresa": "Philips",
        "data_de_fabricacao": "2022-03-15",
        "data_de_validade": "2027-03-15",
        "numero_de_serie": "2468101214",
        "instrucoes_de_armazenamento": "Armazenar em local seco",
    },
    {
        "id": 4,
        "nome_do_produto": "Vinho tinto",
        "nome_da_empresa": "Miolo",
        "data_de_fabricacao": "2020-06-30",
        "data_de_validade": "2025-06-30",
        "numero_de_serie": "3691215182",
        "instrucoes_de_armazenamento": "Manter em local fresco",
    },
    {
        "id": 5,
        "nome_do_produto": "Creme hidratante",
        "nome_da_empresa": "Nivea",
        "data_de_fabricacao": "2022-02-05",
        "data_de_validade": "2024-02-05",
        "numero_de_serie": "5555555555",
        "instrucoes_de_armazenamento": "Armazenar em local seco e fresco",
    },
]

expect = (
    f"{GREEN}Data de fabricação mais antiga:{CLOSE_COLOR}"
    f" {BLUE}2020-06-30{CLOSE_COLOR}\n"
    f"{GREEN}Data de validade mais próxima:{CLOSE_COLOR}"
    f" {BLUE}2023-12-01{CLOSE_COLOR}\n"
    f"{GREEN}Empresa com mais produtos:{CLOSE_COLOR}"
    f" {RED}Natura{CLOSE_COLOR}"
)


def test_decorar_relatorio():
    simple_report = SimpleReport()
    colored_report = ColoredReport(simple_report)
    assert expect == colored_report.generate(product_list)
