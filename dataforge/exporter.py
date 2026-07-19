from .exporters.csv_export import CSVExporter
from .exporters.json_export import JSONExporter
from .exporters.excel_export import ExcelExporter
from .exporters.sqlite_export import SQLiteExporter
from .exporters.txt_export import TXTExporter
from .exporters.sql_export import SQLExporter


class Exporter:

    def __init__(self):
        self.csv = CSVExporter()
        self.json = JSONExporter()
        self.excel = ExcelExporter()
        self.sqlite = SQLiteExporter()
        self.txt = TXTExporter()
        self.sql = SQLExporter()

    def to_csv(self, dataframe, filename):
        return self.csv.export(dataframe, filename)

    def to_json(self, dataframe, filename):
        return self.json.export(dataframe, filename)

    def to_excel(self, dataframe, filename):
        return self.excel.export(dataframe, filename)

    def to_sqlite(self, dataframe, filename, table="data"):
        return self.sqlite.export(dataframe, filename, table)

    def to_txt(self, dataframe, filename):
        return self.txt.export(dataframe, filename)

    def to_sql(self, dataframe, filename, table="data"):
        return self.sql.export(dataframe, filename, table)

    def export_all(self, dataframe, name, table="data"):

        self.to_csv(dataframe, f"{name}.csv")
        self.to_json(dataframe, f"{name}.json")
        self.to_excel(dataframe, f"{name}.xlsx")
        self.to_sqlite(dataframe, f"{name}.db", table)
        self.to_txt(dataframe, f"{name}.txt")
        self.to_sql(dataframe, f"{name}.sql", table)

        print("Export completed successfully!")