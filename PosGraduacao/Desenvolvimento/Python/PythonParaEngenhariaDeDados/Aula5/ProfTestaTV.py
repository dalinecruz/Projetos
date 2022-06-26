from ListaExercicios2 import ProfTelevisao
from ListaExercicios2 import ProfControleRemoto

t = ProfTelevisao.Televisao()
c = ProfControleRemoto.ControleRemoto(17, 30)
t.ligar(True, c)

c.aumentar_canal()
c.aumentar_canal()
c.diminuir_volume()
c.diminuir_volume()
t.canal_atual = c.numero_canal
t.volume_atual = c.volume
c.trocar_canal(9)
t.canal_atual = c.numero_canal
print("Canal Atual = " + str(t.canal_atual))
print("Volume Atual = " + str(t.volume_atual))