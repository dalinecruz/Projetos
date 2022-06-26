class Automovel:
    ano_fabricacao = None
    modelo = None
    marca = None
    potencia = None
    numero_portas = None
    placa = None
    cor = None
    chassi = None
    tipo = None
    
    
    def imprimir(self, a):
        print("Marca: " + a.marca)
        print("Modelo: " + a.modelo)
        print("Cor: " + a.cor)
        print("Ano Fabricacao: " + str(a.ano_fabricacao))
        print("Chassi : " + a.chassi)
        print("Placa: " + a.placa)
        
    def ligar(self):
        print("Carro ligado!")
        
    def desligar(self):
        print("Carro desligando...")
    
    def frear(self):
        print("Carro freando...")
        
    def travarPortas(self):
        print("Portas travadas!")
        
    def acelerar(self):
        print("Carro acelerando...")
