from ..importer.csv_importer import CsvImporter
from ..importer.json_importer import JsonImporter
from ..importer.xml_importer import XmlImporter
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def check_type(path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)
        else:
            raise ValueError("Valor do path não reconhecido")

    @staticmethod
    def import_data(path, type):
        data = Inventory.check_type(path)

        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
        else:
            raise ValueError("Deve ser simples ou completo")
