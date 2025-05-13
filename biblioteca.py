class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.dormindo =  False
        self.falando = False
        self.comendo = False
    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} ja esta dormindo")
        elif self.falando == True:
            print(f"{self.nome} nao pode dormir pq ta falando")
        elif self.comendo ==  True:
            print(f"{self.nome} nao pode dormir pq ta comendo")
        else:
            print(f"o aluno foi dormir")
            self.dormindo = True
    def acordar(self):
        if self.dormindo == True:
            self.dormindo = False
            print("o tabacudo acordou")
        else:
            print("ele ja esta acordado")
class ContaBancaria:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.saldo = 0.0
        self.ativa = False
class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer (self):
        print(f"O {self.nome} foi comer...")
class Gato(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def miar(self):
        print(f"O gato {self.nome} foi miando e a cor dele é {self.cor} um gato muito bonito...")
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def latir(self):
        print(f"O cachorro {self.nome} com a cor {self.cor} comecou a latir bastante por causa do gato")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def muge(self):
        print(f"A vaca {self.nome} ficou mugindo, a cor dela é {self.cor} é muito bonita ")
class Coelho(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def guinchar(self):
        print(f"O Coelho astuto {self.nome} correu bastante do cachorro e depois ficou guinchando a cor dele é {self.cor}")
class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprime_valor(self):
        print(f"o valor do ingresso é {self.valor:.2f}")
class Vip(Ingresso):
    def __init__(self, valor):
        super(). __init__(valor)
        self.adicional = self.valor * 0.5
    def ValorTotal(self):
        return self.valor + self.adicional
class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0
class Retangulo(Forma):
    def __init__(self):
        super(). __init__()

    def calculeArea(self, base, altura):
        self.area = base*altura
        print(f"a Area do retangulo é {self.area}")
    def calculaPerimetro(self, base, altura):
        self.perimetro = 2*(base+altura)
        print(f"o Perimetro do triangulo é {self.perimetro}")
class Triangulo(Forma):
    def __init__(self):
        super(). __init__()
    def calculeArea(self, base, altura):
        self.area = (base*altura) / 2
        print(self.area)
    def calculePerimetro(self, base, altura):
        self.perimetro = (base+altura)
        print(self.perimetro)

