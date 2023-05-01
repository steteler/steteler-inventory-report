from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]