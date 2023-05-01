from .importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            reader = json.load(file)
            return list(reader)
