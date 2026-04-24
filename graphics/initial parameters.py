#I found this in a discussion about orbit and 3D graphics, tested it in VS Code and it looked pretty good. I'm going to put together a study repository here.
#I divided the code into parts.
#pt: Achei em uma discussão sobre graficos em orbita e 3d, testei no VS Code e ficou bem legal. 
     Vou montar aqui um repositorio de estudos. 
     Dividi em partes os cod.

import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

plt.close()

G = 6.6742e-11

###Panets / pt: Planetas
###Earth / pt: Terra
name = 'Earth'
Rplanet= 6357000 #K
mplanet= 5.972e24 #Kg

###Cube satelite / pt: Satélite cúbico
mass = 1 #Kg
S = 1/100 #Trasnversal area / pt: Área transversal
CD = 2

#I'll have a R3 cartesian system. 
Therefore i'll have to set the planet in terms of xyz and Vector position, speed and force in those unit vectors. 
So i'll define all vectors as arrays.
#pt: Terei um sistema cartesiano R3. 
Portanto, terei que definir o planeta em termos de posição, velocidade e força vetorial nos eixos xyz e xyz, usando esses vetores unitários. 
Assim, definirei todos os vetores como matrizes.

x0 = 0
y0 = Rplanet + 350000
z0 = 0
r0 = Rplanet + 350000
velx0 = 0
vely0 = 0
velz0 = np.sqrt((G*mplanet)/r0)
period = 1e5

xdot = velx0
ydot = vely0
zdot = velz0

