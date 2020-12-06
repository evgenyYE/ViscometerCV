import sqlite3
import os
from scripts.path import the_local_path


class _SQLiteBasic:
    """A context manager Class for sqlite3 database. Allows to use 'with' construction."""

    def __init__(self, database: str):
        self.connection = sqlite3.connect(database)

    def __enter__(self):
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        if exc_type == sqlite3.OperationalError:
            return True


class SQLiteAgent:
    """ Class for writing and reading the application data from sqlite3 database"""
    DATA_LEN = 6
    __instance = None

    def __init__(self):

        if not SQLiteAgent.__instance:
            print("SQLiteAgent __init__ method called..")
            self.my_database = 'setup_data.db'
            self.setup_key = ('setup',)
            self.setup_table = 'setup'
            self.setup_data = None

            if not os.path.isfile('database//' + self.my_database):
                self.__create_db()
            else:
                self.read_from_db()
        else:
            print("SQLiteAgent instance already created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SQLiteAgent()
        return cls.__instance

    def __create_db(self):
        with _SQLiteBasic('database//' + self.my_database) as database:
            local_path = the_local_path()

            database.execute('''CREATE TABLE setup
                    (key test, source text, results text, namespace text, is_top real, is_sound real)''')

            data = [local_path + '\\defaultSource', local_path + '\\defaultResult',
                    local_path + '\\namespaces\\default_namespace.txt', 1, 1]
            self.write_to_db(data)
            database.execute('SELECT * FROM setup WHERE key=?', self.setup_key)
            self.setup_data = database.fetchone()

    def write_to_db(self, data: list, mode='setup') -> bool:
        if mode == 'setup':
            if isinstance(data, list) and len(data) == self.DATA_LEN - 1:
                data.insert(0, self.setup_key[0])

                data = self.__data_validation(data)

                with _SQLiteBasic('database//' + self.my_database) as database:
                    database.execute('DELETE FROM setup WHERE key=?', self.setup_key)
                    database.executemany('INSERT INTO setup VALUES (?,?,?,?,?,?)', [data])
            else:
                return False

    def read_from_db(self, mode='setup'):
        if mode == 'setup':
            with _SQLiteBasic('database//' + self.my_database) as database:
                database.execute('SELECT * FROM setup WHERE key=?', self.setup_key)
                self.setup_data = database.fetchone()

            self.setup_data = self.__data_validation(self.setup_data)
            return self.setup_data

    def __data_validation(self, data) -> list:

        data = list(data)
        default = [self.setup_key, the_local_path() + '\\defaultSource', the_local_path() + '\\defaultResult',
                   the_local_path() + '\\namespaces\\default_namespace.txt', 1, 1]

        if not os.path.isfile(default[3]):
            with open(default[3], "w") as f:
                f.write('Result.xlsx')

        for i in range(1, self.DATA_LEN):
            if i < 3 and (not os.path.isdir(data[i])):
                data[i] = default[i]
            elif i == 3 and (not os.path.isfile(data[i])):
                data[i] = default[i]
            elif i > 3 and (not (data[i] == 1 or data[i] == 0)):
                data[i] = default[i]

        return data
