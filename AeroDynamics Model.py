###AeroDynamics Model
class Aerodynamics():
    def __init__(self, name):
        self.name = name
        if name == 'Earth':
            ###Model with earth data
            self.beta = 0.1354/1000 #Desity constant
            self.rhos = 1.225 #kg/m^3
    def getDensity(self, altitude):
        if self.name == 'Earth':
            rho = self.rhos*np.exp(-altitude*self.beta)
            return rho

aeroModel = Aerodynamics(name)
