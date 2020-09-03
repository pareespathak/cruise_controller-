# **CRUISE_CONTROLLER**

## AIM:

Implementing the concept of PID controller by designing cruise controller to reach desired velocity.  
1.With constant input velocity .  
2.With variable input velocity and constant slope.

## Motion Model:  
The model of the cruise control system is relatively simple. If the inertia of the wheels is neglected,  
And it is assumed that air drag (which is proportional to the car's speed at low speeds) is what is
Opposing the motion of the car, then the problem is reduced to a simple first order system.  
Thus the motion of the car can be written as   
### mv_ + bv = u  
(where u is the input force provided by the engine to move the car at a certain velocity.)  
Constant parameters for the car i.e. mass and the drag coefficient are taken as m=1500 kg and 0.25 respectively.  

## Task 1:  
•	Find v and v_ from the dynamical model and compare it with the set point values.  
•	Find the error and use the PID controller with appropriate tuning parameter to tune the controller to an acceptable level of accuracy.  
•	The tuning parameters you choose give the system a rise time of about 10secs and maximum overshoot of less than 5%.(rise time is the time taken to reach 90% of the steady state value)
## Task 2:
• Update code to handle set point changes varying with the time of simulation.  
• Change the dynamical model of the car to handle rolling friction(u = 0.01) as well.  
• Design the controller to handle a constant slope of road.(positive or negative)
