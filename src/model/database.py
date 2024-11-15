import sqlite3
from os import path
from utils import load_json

class DataBase:
    def __init__(self) -> None:
        self.database_rules = load_json(path.join('resources', 'rules', 'database_rules.json'))
        self.default_values = load_json(path.join('resources', 'rules', 'default_values.json'))

        self.connection = sqlite3.connect(path.join('resources', 'databases', 'stores_database.db'))
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row

    def create_database(self) -> None:
        for mapping_json in self.database_rules:
            table_name = mapping_json['table_name']
            columns = ", ".join([f"{column_name} {column_type}" for column_name, column_type in mapping_json["columns"].items()])

            self.cursor.execute(f"DROP TABLE IF EXISTS {mapping_json['table_name']}")

            self.cursor.execute(f"CREATE TABLE {table_name}({columns})")

        for mapping_json in self.default_values:
            table_name = mapping_json['table_name']
            values = mapping_json['values']

            for value in values:
                DataBase().insert_values((value,), table_name)

        self.cursor.close()
        self.connection.close()
    
    def insert_values(self, data: tuple, table: str) -> None:
        try:
            list_columns = list(next((item["columns"].keys() for item in self.database_rules if item["table_name"] == table), None))
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

    def get_id(self, item: str, table_name: str) -> int:
        column_name = table_name

        try:
            query_search = self.cursor.execute(f"SELECT ID FROM {table_name} WHERE {column_name} = ?", (item,))

            required_id = [id for id in query_search][0]

        except IndexError:
            print(f"{table_name} hasn't {item} item")

        else:
            self.cursor.close()
            self.connection.close()

            return required_id[0]
        
        self.cursor.close()
        self.connection.close()
    
    def get_values(self, table: str, head: int = None) -> list:
        if head is not None and head > 0:
            try:
                query_search = self.cursor.execute(f'SELECT * FROM {table} WHERE (ID > 0 AND ID <= {head})')

            except sqlite3.OperationalError:
                print(f"{table} table don't exists")

            else:
                values = [value for value in query_search]

                return values
        else:
            if type(head) == int and head <= 0:
                raise ValueError (f"head can be only None or a integer > 0.\nCan you say {head*-1 if head < 0 else 1}?")
            
            try:
                query_search = self.cursor.execute(f'SELECT * FROM {table}')
            
            except sqlite3.OperationalError:
                print(f"{table} table don't exists")
            else:
                values = [value for value in query_search]

                return values
            
        self.cursor.close()
        self.connection.close()
    
    def remove_value(self, table: str, column: str, item):
        if item == 'all':
            self.cursor.execute(f'DELETE FROM {table}')
        else:
            self.cursor.execute(f'DELETE FROM {table} WHERE {column} = ?', (item,))

        self.connection.commit()
        self.cursor.close()
        self.connection.close()