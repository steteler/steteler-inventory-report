from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        9,
        "morango",
        "Emma Corporation",
        "2010-10-21",
        "2011-10-21",
        369,
        "jogue fora",
    )

    assert product.__repr__() == (
        "O produto morango fabricado "
        "em 2010-10-21 por Emma Corporation com validade "
        "até 2011-10-21 precisa ser armazenado jogue fora."
    )
