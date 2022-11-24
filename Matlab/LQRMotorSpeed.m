%% Mendefinisikan Parameter-parameter yang diperlukan
J = 0.01;
b = 0.1;
K = 0.01;
R = 1;
L = 0.5;

%% Matriks State-Space

A = [-b/J    K/J
     -K/L    -R/L];
B = [0
     1/L];
C = [1  0];
D=0;

%% Cek Controllability Sistem
Co = ctrb(A,B)
rank(Co)

%% LQR
Q = [1    0
     0    1];
R = 1;

K = lqr(A, B, Q, R)

%% Opened Loop Sistem
 sys_ol= ss(A,B,C,D)
 figure(1), step(sys_ol,0:0.01:10)
 grid on
 title('Opened-Loop Kendali Kecepatan'), xlabel('Waktu'),ylabel('Kecepatan')
 
%% Closed Loop sistem
 A_cl = A-B*K   
 sys_cl= ss(A_cl,B,C,D)
 figure(2), step(sys_cl,0:0.01:10)
 grid on
 title('Closed-Loop Kendali Kecepatan'), xlabel('Waktu'),ylabel('Kecepatan')