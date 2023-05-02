from .importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".json"):
            with open(path) as file:
                reader = json.load(file)
                return list(reader)

        raise ValueError("Arquivo inválido")
