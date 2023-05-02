
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import sys

reports = {"simples": SimpleReport, "completo": CompleteReport}


def main():
    try:
        _, path, type = sys.argv

        if path.endswith(".csv"):
            data = InventoryRefactor(CsvImporter)
        elif path.endswith(".json"):
            data = InventoryRefactor(JsonImporter)
        elif path.endswith(".xml"):
            data = InventoryRefactor(XmlImporter)

        data.import_data(path, type)

        sys.stdout.write(reports[type].generate(data.data))

    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")