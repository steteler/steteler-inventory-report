from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product1 = Product(
        1,
        "Emma Cabelos",
        "Emma Corporation",
        "1978",
        "1979",
        1514,
        "no congelador",
    )
    expect = (
        "O produto Emma Cabelos fabricado"
        " em 1978 por Emma Corporation com validade até 1979"
        " precisa ser armazenado no congelador."
    )

    assert expect == product1.__repr__()
