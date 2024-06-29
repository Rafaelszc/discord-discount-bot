import sqlite3
from os import path
from utils import load_json

class DataBase:
    database_rules = load_json(path.join('resources', 'rules', 'database_rules.json'))

    connection = sqlite3.connect(path.join('resources', 'databases', 'stores_database.db'))
    cursor = connection.cursor()
    connection.row_factory = sqlite3.Row

    @classmethod
    def create_database(cls):
        for mapping_json in cls.database_rules:
            name_table = mapping_json['name_table']
            columns = ", ".join([f"{column_name} {column_type}" for column_name, column_type in mapping_json["columns"].items()])

            cls.cursor.execute(f"DROP TABLE IF EXISTS {mapping_json['name_table']}")

            cls.cursor.execute(f"CREATE TABLE {name_table}({columns})")

        cls.cursor.close()
        cls.connection.close()
    
    @classmethod
    def insert_values(cls, data: tuple, table: str):
        try:
            list_columns = list(next((item["columns"].keys() for item in cls.database_rules if item["name_table"] == table), None))
            list_columns.remove('ID')

            quantity_columns = len(list_columns)

            cls.cursor.execute(f"INSERT INTO {table} ({','.join(list_columns)}) VALUES ({','.join(['?']*quantity_columns)})", data)

        except TypeError:
            print(f"{table} table don't exists.")

        except sqlite3.ProgrammingError:
            print('Unexpected amount of data, different from that supported on column')

        else:
            cls.connection.commit()

        cls.cursor.close()
        cls.connection.close()