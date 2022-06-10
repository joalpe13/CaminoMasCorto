

class CaminoCorto():
    caminoTemporal = []
    sumaTemporal = None
    caminoCorto = []
    sumaCorta = None
    matriz = None
    coordenadasTemporales = []
    coordenadasCortas = []
    
    def __init__(self, mat):
        self.matriz = mat.copy()
        self.caminoTemporal = self.matriz[0].copy()
        self.sumaTemporal = self.suma(self.caminoTemporal)
        self.caminoCorto = self.matriz[0].copy()
        self.sumaCorta = self.suma(self.caminoCorto)
        self.coordenadasCortas = self.matriz[0].copy()
        self.coordenadasTemporales = self.matriz[0].copy()

    def buscar(self):
        
        for y in range(len(self.matriz)):
            x = 0
            self.caminoTemporal[x] = self.matriz[y][x] 
            self.coordenadasTemporales[x] = [y,x]
            self.puertas(y,x)
        
        print("Camino corto",self.caminoCorto)
        print("suma corto",self.sumaCorta)
        print("coord corto",self.coordenadasCortas)
        
        
    def suma(self, array):
        suma = 0
        for i in array:
            suma += i
        return suma
            
    def puertas(self, y, x):
        x = x+1
        y = y
        if x < len(self.matriz[0]):
            
            if y-1 >= 0 & y-1 < len(self.matriz):
                self.caminoTemporal[x] = self.matriz[y-1][x]
                self.coordenadasTemporales[x] = [y,x]
                self.puertas(y-1, x)
            
            if y >= 0 & y < len(self.matriz):
                self.caminoTemporal[x] = self.matriz[y][x]
                self.coordenadasTemporales[x] = [y,x]
                self.puertas(y, x)
                
            if y+1 >= 0 and y+1 < len(self.matriz):
                self.caminoTemporal[x] = self.matriz[y+1][x]
                self.coordenadasTemporales[x] = [y,x]
                self.puertas(y+1, x)
                
        else:
                self.suma(self.caminoTemporal)
                #print("CaTemp",self.caminoTemporal,"Sum",self.sumaTemporal)
                #print("___________")
                if self.suma(self.caminoTemporal) < self.suma(self.caminoCorto):
                    self.caminoCorto = self.caminoTemporal.copy()
                    self.coordenadasCortas = self.coordenadasTemporales        
            