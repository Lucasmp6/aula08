from biblioteca import Pessoa

aluno01 = Pessoa("Lucas", 19,66 )
aluno02 = Pessoa("Victor", 20,76)
aluno01.nome = "Guilherme o Grande"
print(f"{aluno01.nome} tem {aluno01.idade} anos e pesa {aluno01.peso} kg")
aluno02.nome = "Lucas o Brincalhão"
print(f"{aluno02.nome} tem {aluno02.idade} anos e pesa {aluno02.peso} kg")
aluno01.falar()
aluno01.comer("Pipoca")
aluno01.dormir()
