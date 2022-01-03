from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Clock")
root.geometry("310x110")
root.config(bg="black")
# global h, m, s
def time():
    h=strftime('%I')
    m=strftime('%M')
    s=strftime('%S')
    sex="{:2}".format(h)+":"+"{:2}".format(m)+":"+"{:2}".format(s)
    # string=strftime('%I:%M %p')
    label.config(text=sex)
    label.after(1000, time)

label=Label(root, font=("ds-digital", 80), background='black', foreground='cyan')
label.pack(side="left", expand=FALSE)
# print(strftime(str('%-10H:-10%M:%-10S')))
# h=strftime('%I')
# m=strftime('%M')
# s=strftime('%S')
# print("{:5}".format(h)+"{:5}".format(m)+"{:5}".format(s))
time()
mainloop()