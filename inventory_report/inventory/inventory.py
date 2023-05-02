from ..importer.csv_importer import CsvImporter
from ..importer.json_importer import JsonImporter
from ..importer.xml_importer import XmlImporter
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport

reports = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @staticmethod
    def check_type(path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)

    @staticmethod
    def import_data(path, type):
        data = Inventory.check_type(path)

        return reports[type].generate(data)
