# -*- coding: utf-8 -*-
Tinf1 = 20
Tinf2 = -10
H = 0.8
W = 1.5
t = 0.004
k_glass  = 0.78
air_gap = 0.01
k_air = 0.026
h1 = 10
h2 = 40
A = H*W
R_Conv_i = 1/(h1*A)
R_Conv_o = 1/(h2*A)
R_Cond_g = t/(k_glass*A)
R_Cond_air = air_gap/(k_air*A)
R_tot = R_Conv_i + R_Conv_o + 2*R_Cond_g + R_Cond_air

Q = A*(Tinf1 - Tinf2)/R_tot
print ("The heat flux through the wall is " + str(Q) + " W ")

T1 = Tinf1 - (Q/A)*R_Conv_i
print ("The temperature of the inner wall is " + str(T1) + " °C ")
