import tkinter as tki
from tkinter import *

window = Tk()
window.title("СПИСОК САЙТОВ С ПИРАТСКИМ КОНТЕНТОМ")
window.geometry("1100x400")
window.resizable(False, False)
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )



f = open('pir.txt', 'r')
lstbox = Listbox(window, yscrollcommand=scrollbar.set, height=450)
for line in f.readlines():
    lstbox.insert(END, "\n" + str(line))
    lstbox.insert(END, "\n")
    print(line)
lstbox.pack( fill = BOTH )
scrollbar.config( command = lstbox.yview )
f.close()
window.mainloop()

