from matplotlib import pyplot as plt
import numpy as np
time = np.arange(0,500,1)
velo = np.zeros([500], dtype=float)
m=1500
b=.25
kp=300
ki=2
kd=100
vr=40 #refetence velocity
v=0
dt=1
old_e=0
E=0
for i in range(1,500):
    e=vr-v
    e_dot=e-old_e
    E=E+e
    u=kp*e+kd*e_dot+ki*E
    old_e=vr-v
    #"dv value method"
    dv=(u-(b*v))*dt/m
    v=v+dv
    velo[i]=v
shoot=max(velo)-vr
stvel=(vr-velo[10])*100/vr
print("overshoot %",shoot*100/vr)
print("velo at time 10 sec = ",100-stvel,"%of steady state velo")
title = '''cruise controller with constant velocity'''
s = '''reference
    velocity'''
plt.plot(time,velo)
plt.annotate(s,(400,vr-5))
vr_arr = np.zeros([500], dtype=float)+vr
plt.plot(time,vr_arr,'g''--',lw=2)
plt.title(title)
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.grid()
#plt.savefig('cruise_c_basic.jpeg')
plt.show()
