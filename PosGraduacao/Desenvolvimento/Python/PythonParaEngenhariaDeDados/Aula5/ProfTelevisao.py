class Televisao():
    
    ligado = None
    potencia = None
    canal_atual = None
    volume_atual = None
    controle = None
    
    def __init__(self):
        self.ligado = False
        self.marca = ""
        self.potencia = ""
        self.canal_atual = 0
        self.volume_atual = 0
    
    def ligar(self, ligado, controle):
        self.ligado = ligado
        self.controle = controle
        self.canal_atual = self.controle.numero_canal
        self.volume_atual = self.controle.volume
        print("Ligado " + str(self.ligado) + " Canal Atual = " + str(self.canal_atual) + " Volume Atual = " + str(self.volume_atual))

    def desligar(self, desligado):
        self.ligado = desligado
        print("Desligado")