import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

# configure Progressbar style to be flat and with the colors from the pictures
style.configure('my.Vertical.TProgressbar', background='#f7f4bf', troughcolor='#8a7852',
                pbarrelief='flat', troughrelief='flat')

pbar1 = ttk.Progressbar(root, maximum=100, value=100, orient='vertical', style='my.Vertical.TProgressbar')
pbar2 = ttk.Progressbar(root, maximum=100, value=74, orient='vertical', style='my.Vertical.TProgressbar')
pbar3 = ttk.Progressbar(root, maximum=100, value=10, orient='vertical', style='my.Vertical.TProgressbar')
pbar4 = ttk.Progressbar(root, maximum=100, value=45, orient='vertical', style='my.Vertical.TProgressbar')
pbar5 = ttk.Progressbar(root, maximum=100, value=50, orient='vertical', style='my.Vertical.TProgressbar')

pbar1.grid(row=0, column=0, padx=40, pady=10)
pbar2.grid(row=0, column=1, padx=40, pady=10)
pbar3.grid(row=0, column=2, padx=40, pady=10)
pbar4.grid(row=0, column=3, padx=40, pady=10)
pbar5.grid(row=0, column=4, padx=40, pady=10)

root.configure(bg="#231303")
root.mainloop()