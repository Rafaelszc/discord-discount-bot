import sqlite3
from os import path
from utils import load_json

class DataBase:
    def __init__(self) -> None:
        self.database_rules = load_json(path.join('resources', 'rules', 'database_rules.json'))

        self.connection = sqlite3.connect(path.join('resources', 'databases', 'stores_database.db'))
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row

    def create_database(self):
        for mapping_json in self.database_rules:
            name_table = mapping_json['name_table']
            columns = ", ".join([f"{column_name} {column_type}" for column_name, column_type in mapping_json["columns"].items()])

            self.cursor.execute(f"DROP TABLE IF EXISTS {mapping_json['name_table']}")

            self.cursor.execute(f"CREATE TABLE {name_table}({columns})")

        self.cursor.close()
        self.connection.close()
    
    def insert_values(self, data: tuple, table: str):
        try:
            list_columns = list(next((item["columns"].keys() for item in self.database_rules if item["name_table"] == table), None))
            list_columns.remove('ID')

            quantity_columns = len(list_columns)

            self.cursor.execute(f"INSERT INTO {table} ({','.join(list_columns)}) VALUES ({','.join(['?']*quantity_columns)})", data)

        except TypeError:
            print(f"{table} table don't exists.")

        except sqlite3.ProgrammingError:
            print('Unexpected amount of data, different from that supported on column')

        else:
            self.connection.commit()

        self.cursor.close()
        self.connection.close()

    def get_id(self, item: str, table: str) -> int:
        column = table

        try:
            query_search = self.cursor.execute(f"SELECT ID FROM {table} WHERE {column} = ?", (item,))

            required_id = [id for id in query_search][0]

        except IndexError:
            print(f"{table} hasn't {item} item")

        else:
            self.cursor.close()
            self.connection.close()

            return required_id[0]
    
    def get_values(self, table: str, head: int = None) -> list:
        if head is not None and head > 0:
            query_search = self.cursor.execute(f'SELECT * FROM {table} WHERE (ID > 0 AND ID <= {head})')

            values = [value for value in query_search]

            return values
        else:
            query_search = self.cursor.execute(f'SELECT * FROM {table}')

            values = [value for value in query_search]

            return values