J = 3.2284E-6;
b = 3.5077E-6;
Kt = 0.0274;
Ke = 0.0274;
R = 4;
L = 2.75E-6;
s = tf('s');
P_motor = Kt/((J*s+b)*(L*s+R)+Kt*Ke);

Kp = 100;
Ki = 200;
Kd = 10;
C = pid(Kp,Ki,Kd);
sys_cl = feedback(C*P_motor,1);
step(sys_cl, 0:0.01:4)
grid
title('PID Control with Large Ki and Large Kd')