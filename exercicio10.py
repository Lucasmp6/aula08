from biblioteca import Ingresso, Vip

ingresso_comum = Ingresso(100.0)
ingresso_comum.imprime_valor()

ingresso_vip = Vip(100.0)
print(f"O valor do ingresso vip é R$ {ingresso_vip.ValorTotal():.2f}")