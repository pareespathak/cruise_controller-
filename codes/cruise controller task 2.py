from matplotlib import pyplot as plt
import numpy as np
import math as sl
time = np.arange(0,500,1)
velo = np.zeros([500], dtype=float)
m=1500
b=.25
kp=500
ki=8.5
kd=10
# enter initial refrence velo value in vr
vr=20
v=0
dt=1
old_e=0
E=0
g=9.8
vrmax=vr
us=0.01 #friction coefficient
#slopes
#slope=sl.pi/8  #slope enter values between [-pi/2 ,pi/2]
slope=0
# designing pid controller
for i in range(1,500):
    #enter time in i and velocity desired at that point as vr
    if i>50:
        vr=40
    '''if i>15 and i<25:
        vr=60'''
    if i>300:
        vr=70
    #for more intervals copy paste the above condition and enter desired value
    e=vr-v                  #proportional error
    e_dot=e-old_e
    E=(E+e)*dt              #integral error
    u=kp*e+kd*e_dot+ki*E
    old_e=vr-v
    F=m*g*(sl.sin(slope)+us*sl.cos(slope))
    v=((u-F)*dt+m*v)/(m+b*v)
    velo[i]=v
                       #details of slope on graph
s = '''without slope
    of road'''
plt.annotate(s,(400,vr-10))
                        # reference velocity lines
vr_arr = np.zeros([500], dtype=float)+20
plt.plot(time,vr_arr,'g''--',lw=2)
vr_arr = np.zeros([500], dtype=float)+40
plt.plot(time,vr_arr,'g''--',lw=2)
vr_arr = np.zeros([500], dtype=float)+70
plt.plot(time,vr_arr,'g''--',lw=2)
                        # parameters of overshoot 
shoot=max(velo)-vr
stvel=(vr-velo[10])*100/vr
print("velo at 0 sec",velo[0])
print("overshoot %",shoot*100/vr)
print("velo at time 10 sec = ",100-stvel,"%of steady state velo")
                        # Graph labelings  
title='''Variable input velocities
         and constant slope '''
plt.title(title)
plt.xlabel("time")
plt.ylabel("velocity")
plt.grid()
plt.plot(time,velo)
plt.savefig('task2_without_slope.jpeg') #saving graph
plt.show()