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
def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido")
vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO = 2"
deletar(vcon, vsql)