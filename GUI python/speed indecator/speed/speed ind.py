from tkinter import *
from PIL import ImageTk, Image
import serial

ser = serial.Serial('/dev/ttyACM0',9600)

win = Tk()
win.geometry("450x470")
win.config(bg="white")
Btn = Button(win, text="ok", activebackground='gray',bg='white', bd=0)

path = "/home/bodhi/GUI python/speed indecator/speed/"
List = ['0.png', '1.png', '2.png','3.png', '4.png',
        '5.png', '6.png', '7.png', '8.png', '9.png',
        '10.png', '11.png', '12.png',
        '13.png', '14.png', '15.png', '16.png', '17.png',
        '18.png', '19.png',  '20.png', '21.png',
        '22.png', '23.png', '24.png', '25.png', '26.png',
        '27.png', '28.png', '29.png',  '30.png',
       ]

def to_pil2(img, button, x, y, w, h):
    image = Image.open(img)
    image = image.resize((w, h), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)
    button['image'] = pic
    button.image = pic
    button.place(x=x, y=y)

label = Label(win,font=('Stencil',30,'bold'),bg='white',fg='red')
label.place(x=205,y=370)
def run():
    read = ser.readline().decode('utf-8')
    to_pil2(path + List[int(read)], Btn, 50, 100, 340, 250)
    label['text']=read
    win.after(50, run)

run()
Btn["command"] =lambda: print('ok')
win.mainloop()