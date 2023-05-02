from collections.abc import Iterable
from .inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, _type):
        data = self.importer.import_data(path)
        self.data = [*self.data, *data]

    def __iter__(self):
        return InventoryIterator(self.data)
