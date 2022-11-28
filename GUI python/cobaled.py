import serial
from tkinter import *
import tkinter as tk

port = 'COM4'
ser = serial.Serial(port, baudrate = 9600, timeout = 1)

def OnLED():
    ser.write(b'ON')

def OffLED():
    ser.write(b'OFF')

#buat window
root = Tk()
root.title('Nyoba aja ini kak')

btn_on = tk.Button(root, text="Turn ON", command=OnLED)
btn_on.grid(row=0, column=0)

btn_off = tk.Button(root, text="Turn OFF", command=OffLED)
btn_off.grid(row=1, column=1)

root.geometry("350x350")
root.mainloop()