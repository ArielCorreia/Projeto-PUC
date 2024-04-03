
from urllib.parse import quote

from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

import cx_Oracle


lib_dir = "D:\Programa de desenvolvimneto gti\ORACLE\instantclient-basic-windows.x64-21.13.0.0.0dbru\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

USER = 'CTL_ESTOQUE'
PASSWD = quote('admin') # quote é utilizado para ajustar a URL que possui caracteres especiais
HOST = 'localhost'
PORT = 1521
SID = "xe"


sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"
engine = create_engine(url=instance, echo=True, max_identifier_length=30)
session = scoped_session(sessionmaker(bind=engine, autoflush=True,autocommit=False))
# response = session.execute(text('SELECT * FROM PESSOA'))
'''for o in response:
    print(o)'''
print("Conectado no banco de dados.")

