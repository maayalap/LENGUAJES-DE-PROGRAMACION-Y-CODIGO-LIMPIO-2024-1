from model.database_manager import DatabaseManager

db = DatabaseManager()

class Usuario:
    @classmethod
    def create(cls, table, data):
        try:
            db.insert_data(table, data)
            print("Usuario creado correctamente.")
            return True
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
            return False



    @classmethod
    def find_by_credentials(cls, id_usuario, contrasena):
        query = f"SELECT * FROM usuario WHERE ID_usuario = '{id_usuario}' AND contrasena = '{contrasena}'"
        result = db.execute_query(query)
        return result