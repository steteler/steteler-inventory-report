from .importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".csv"):
            with open(path) as file:
                reader = csv.DictReader(file)
                return list(reader)

        raise ValueError("Arquivo inválido")
