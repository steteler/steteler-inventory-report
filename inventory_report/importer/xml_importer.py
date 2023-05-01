from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
