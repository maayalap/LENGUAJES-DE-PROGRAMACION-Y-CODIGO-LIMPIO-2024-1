# database_manager.py

import psycopg2
from configparser import ConfigParser

class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        # Lee los datos de conexión desde el archivo secret.config
        config = ConfigParser()
        config.read('secret.cfg')

        self.host = config.get('database', 'PGHOST')
        self.database = config.get('database', 'PGDATABASE')
        self.user = config.get('database', 'PGUSER')
        self.password = config.get('database', 'PGPASSWORD')

        # Establece la conexión a la base de datos
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def execute_query(self, query):
        # Ejecuta una consulta en la base de datos
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def insert_data(self, table, data):
        # Inserta datos en una tabla específica
        with self.connection.cursor() as cursor:
            columns = ', '.join(data.keys())
            values = ', '.join(f"'{value}'" for value in data.values())
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            cursor.execute(query)
        self.connection.commit()


    def close_connection(self):
        self.connection.close()


