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
def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado")
vsql = "UPDATE tb_contatos SET T_NOMECONTATO='Joaozindamassa', T_TELEFONECONTATO='(31)984848484', T_EMAILCONTATO='joaozin@edu.etefmc.com.br'WHERE N_IDCONTATO = 6"
atualizar(vcon, vsql)