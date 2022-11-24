import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from control.matlab import *

root = tk.Tk()#ウインドの作成 gawe jendela
root.title("pid soft")#ウインドのタイトル gawe judul jendela
root.geometry("650x350") #ウインドの大きさ ukurane jendela
frame_1 = tk.LabelFrame(root,labelanchor="nw",text="グラフ",foreground="green")
frame_1.grid(rowspan=2, column=0)
frame_2 = tk.LabelFrame(root,labelanchor="nw",text="パラメータ",foreground="green")
frame_2.grid(row=0, column=1, sticky="nwse")
frame3=tk.LabelFrame(root,text="履歴",foreground="green")
frame3.grid(row=1,column=1,sticky="nwse")

#スケールバーが動いたらその値を読み取りグラフを更新する nalikane scale bar obah, maca value-ne lan update grafike
def graph(*args):
    graph_on_off=graph_var.get()
    if graph_on_off==0:
        ax.cla()
    Kp=scale_var.get()
    Ti=scale_var_Ti.get()
    Td=scale_var_Td.get()
    value_Kp=f"{Kp:.2f}"
    value_Ti=f"{Ti:.2f}"
    value_Td=f"{Td:.2f}"
    text_display.set(str(value_Kp))
    text_display_Ti.set(str(value_Ti))
    text_display_Td.set(str(value_Td))
    num=[Td,1,1/Ti]
    den=[1,0]
    G_ID=tf(num,den)
    G_all=feedback(G_ID*Kp*G,1)
    (y_s,t_s)=step(G_all,T=np.arange(0,10,0.01))
    (y_in,t_in)=step(1,T=np.arange(0,10,0.01))
    ax.set_xlabel('t / s')
    ax.set_ylabel('y')
    plt.style.use('ggplot')
    ax.plot(t_s,y_s)
    ax.plot(t_in,y_in,linestyle="dashed")
    ax.set_title('Kp='+str(value_Kp)+',Ti='+str(value_Ti)+',Td='+str(value_Td))
    canvas.draw()

#伝達関数の設定 ngatur transfer function
#PID制御のパラメータ parameter pangandali PID
Kp=30 #比例ゲイン gain proporsional
Ti=1.8 #積分ゲイン gain integral
Td=0.2 #微分ゲイン gain derivatif
num=[Td,1,1/Ti]
den=[1,0]
G_ID=tf(num,den)

#伝達関数の設定 ngatur transfer function
num = [0.1]
den = [0.1, 1.0, 1]
G = tf(num, den)
G_all=feedback(G_ID*Kp*G,1)

#ステップ応答 step response
(y_s,t_s)=step(G_all,T=np.arange(0,10,0.01))
(y_in,t_in)=step(1,T=np.arange(0,10,0.01))

#グラフの設定 ngatur grafik
fig=plt.Figure()
ax = fig.add_subplot(111) 
ax.plot(t_s,y_s)
ax.plot(t_in,y_in,linestyle="dashed")
ax.set_title('Kp='+str(Kp)+',Ti='+str(Ti)+',Td='+str(Td))
ax.set_xlabel('t / s')
ax.set_ylabel('y')
plt.style.use('ggplot')

#tkinterのウインド上部にグラフを表示する njedulke grafik ing papan duwur jendela tkinter
canvas = FigureCanvasTkAgg(fig, master=frame_1)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
#比例ゲインのスケール作成 scaling gain proporsional
scale_var=tk.DoubleVar()
scale_var.set(Kp)
scale_var.trace("w",graph)
scale=ttk.Scale(frame_2,from_=0,to=10,length=150,orient="h",variable=scale_var)
scale.grid(row=1,column=0)

#比例ゲインのテキスト teks gain proporsional
text=tk.Label(frame_2,text="比例ゲイン:Kp")
text.grid(row=0,column=0)

#比例ゲインの数値表示テキスト display nilai gain proporsional
text_display=tk.StringVar()
text_display.set(str(Kp))
label=tk.Label(frame_2,textvariable=text_display)
label.grid(row=1,column=1)

#積分ゲインのスケール作成 scaling gain integral
scale_var_Ti=tk.DoubleVar()
scale_var_Ti.set(Ti)
scale_var_Ti.trace("w",graph)
scale_Ti=ttk.Scale(frame_2,from_=0.01,to=3,length=150,orient="h",variable=scale_var_Ti)
scale_Ti.grid(row=3,column=0)

#積分ゲインのテキスト teks gain integral
text_ti=tk.Label(frame_2,text="積分ゲイン:Ti")
text_ti.grid(row=2,column=0)

#積分ゲインの数値表示テキスト display nilai gain integral
text_display_Ti=tk.StringVar()
text_display_Ti.set(str(Ti))
label_Ti=tk.Label(frame_2,textvariable=text_display_Ti)
label_Ti.grid(row=3,column=1)

#微分ゲインのスケール作成 scaling nilai gain derivatif
scale_var_Td=tk.DoubleVar()
scale_var_Td.set(Td)
scale_var_Td.trace("w",graph)
scale_Td=ttk.Scale(frame_2,from_=0,to=1.0,length=150,orient="h",variable=scale_var_Td)
scale_Td.grid(row=5,column=0)

#微分ゲインのテキスト teks gain derivatif
text_td=tk.Label(frame_2,text="微分ゲイン:Td")
text_td.grid(row=4,column=0)

#微分ゲインの数値表示テキスト display nilai gain derivatif
text_display_Td=tk.StringVar()
text_display_Td.set(str(Td))
label_Td=tk.Label(frame_2,textvariable=text_display_Td)
label_Td.grid(row=5,column=1)

#グラフ変化の履歴を残すか指定できるラジオボタンを作成 Histori grafik
graph_var=tk.IntVar()
graph_var.set(0)
graph_on=tk.Radiobutton(frame3,value=0,variable=graph_var,text="なし(ora ono)")
graph_on.pack()
graph_off=tk.Radiobutton(frame3,value=1,variable=graph_var,text="あり (ono)")
graph_off.pack()

root.mainloop()