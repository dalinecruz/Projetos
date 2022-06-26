class ControleRemoto():
    numero_canal = None
    volume = None
    
    def __init__(self, numero_canal, volume):
        self.numero_canal = numero_canal
        self.volume = volume
        
    def aumentar_volume(self):
        self.volume += 1
        
    def diminuir_volume(self):
        self.volume -= 1
        
    def trocar_canal(self, numero_canal):
        self.numero_canal = numero_canal
        
    def aumentar_canal(self):
        self.numero_canal += 1
    
    def diminuir_canal(self):
        self.numero_canal -= 1     