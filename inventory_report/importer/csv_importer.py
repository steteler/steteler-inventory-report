from .importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        with open(path, encoding="utf8") as file:
            reader = csv.DictReader(file)
            return list(reader)