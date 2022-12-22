J = 0.01;
b = 0.1;
Kt = 0.01;
Ke = 0.01;
R = 1;
L = 0.5;
s = tf('s');
P_motor = Kt/((J*s+b)*(L*s+R)+Kt*Ke);
Kp = 100;
Ki = 200;
Kd = 10;
C = pid(Kp,Ki,Kd);
sys_cl = feedback(C*P_motor,1);
step(sys_cl, 0:0.01:4)
grid
title('Respon Plant Kecepatan Motor dengan PID')