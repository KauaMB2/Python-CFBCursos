import sqlite3
from sqlite3 import Error
def ConexaoBanco():
    caminho = "C:\\Users\\Rafael\\Desktop\\ETE Escola Kauã\\Python - CFB Cursos\\banco\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = ConexaoBanco()
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado
vsql = "SELECT * FROM tb_contatos"
res = consultar(vcon, vsql)
for i in res:
    print(i)