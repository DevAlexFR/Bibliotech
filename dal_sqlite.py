import sys
import os
import sqlite3

from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.absolute().parent.absolute()))



class SqliteDal:
    def __init__(
        self,
        db_name: str = 'database/bibliotech.db',
        db_folder: str = '',
    ):
        self.db_path = str(Path(db_folder) / db_name)
        os.makedirs(db_folder, exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.close_conn()

    def open_conn(self):
        """Abre a conexão com o banco."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute('PRAGMA synchronous = off')

    def close_conn(self):
        """Fecha a conexão da instância"""
        self.conn.close()

    def table_exists(self, tb_name):
        """Verifica se uma determinada tabela existe em um banco."""
        self.open_conn()
        cursor = self.conn.cursor()
        table = cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' "
            + f"AND name='{tb_name}'; "
        ).fetchall()

        if not table:
            table_exists = False
        else:
            table_exists = True

        self.close_conn()
        return table_exists

    def run_query(self, query:str, parameters=(), insert:bool=False):
        """
            Executa um comando SQL no banco
            param: query (string) -> comando sql que será executado, colocar parametros com "?"
            param: parameters (tupla de strings) -> parametros que ocuparam os caracteres "?" dentro da query
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if insert:
                result = cursor.executemany(query, parameters).fetchall()
            else:
                result = cursor.execute(query, parameters).fetchall()
            conn.commit()
        return result

