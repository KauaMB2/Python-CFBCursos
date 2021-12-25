import canal as cn #ao invés de se referir à biblioteca como "canal", será usado o "cn"
from jogador import jogador as jg
print(jg["nome"])
cn.canal_nome()
print(cn.jogador["nome"])
res = dir(cn)
print(res)