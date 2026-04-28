###Differential equation of the system
def Derivatives(state, t):
    global mass

    x = state[0]
    y = state[1]
    z = state[2]
    velx = state[3]
    vely = state[4]
    velz = state[5]

    xdot = velx
    ydot = vely
    zdot = velz

    ###Forces
    ###Gravity
    accel, r = gravity(x, y, z)
    GravityF = -accel*mass

    ###Aerodynamics
    altitude = r - Rplanet
    rho = aeroModel.getDensity(altitude)
    V = np.sqrt(velx**2 + vely**2 + velz**2)
    qinf = -1/2*rho*abs(V)*S
    aeroF = qinf*CD*np.asarray([velx, vely, velz])
    
    Forces = GravityF + aeroF

    ddot = Forces/mass

    statedot = np.asarray([xdot, ydot, zdot, ddot[0], ddot[1], ddot[2]])
    return statedot
