import sqlite3, os
db = sqlite3.connect(os.path.expandvars('%APPDATA%\\Controle Estoque Mandioca\\controle_estoque_v1.db'))
db.execute("DELETE FROM equipment WHERE name LIKE '%esteira 1%'")
db.commit()
