 cruise controller
 AIM:
 Implementing the concept of PID controller by designing cruise controller 
 Motion Model:
  The model of the cruise control system is relatively simple. If the inertia of the wheels is neglected,
	and it is assumed that air drag (which is proportional to the car's speed at low speeds) is what is
	opposing the motion of the car, then the problem is reduced to a simple first order system.
	Thus the motion of the car can be written as 
  mv_ + bv = u   (where u is the input force provided by the engine to move the car at a certain velocity.)
