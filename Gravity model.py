###Gravity model

def gravity(x, y, z):
    global Rplanet, mplanet, G

    r = np.sqrt(x**2 + y**2 + z**2)

    if r < Rplanet:
        accelx = 0
        accely = 0
        accelz = 0
    else:
        accelx = (G*mplanet)*x/(r**3)
        accely = (G*mplanet)*y/(r**3)
        accelz = (G*mplanet)*z/(r**3)
    return np.asarray([accelx, accely, accelz]), r
    
