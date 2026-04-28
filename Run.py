###Run

stateInitial = np.asarray([x0, y0, z0, velx0, vely0, velz0])

###Time window

tout = np.linspace(0, period, 1000)

stateout = sci.odeint(Derivatives,stateInitial,tout)

xout = stateout[:,0]
yout = stateout[:,1]
zout = stateout[:,2]
velxout = stateout[:,3]
velyout = stateout[:,4]
velzout = stateout[:,5]
altitude = np.sqrt(xout**2 + yout**2 + zout**2) -Rplanet
velout = np.sqrt(velxout**2 + velyout**2 + velzout**2)
