J = 3.2284E-6;
b = 3.5077E-6;
Kt = 0.0274;
Ke = 0.0274;
R = 4;
L = 2.75E-6;
s = tf('s');
P_motor = Kt/((J*s+b)*(L*s+R)+Kt*Ke);
t = 0:0.001:0.2;
sys_cl = feedback(P_motor,1)
step(sys_cl,t)
