from tkinter import *

window = Tk()
window.geometry("400x300")

label1 = Label(window,text="Enter numero 1: ")
label1.grid(column=0,row=0,sticky='w')

num1 = StringVar()

entry1 = Entry(window, textvariable=num1, width =31)
entry1.focus_set()
entry1.grid(column=1,row=0,sticky='sw',columnspan=1, padx=10)

label2 = Label(window,text="Enter numero 2: ")
label2.grid(column=0,row=1,sticky='w')

num2 = StringVar()

entry2 = Entry(window, textvariable=num2, width =31)
entry2.focus_set()
entry2.grid(column=1,row=1,sticky='sw',columnspan=1, padx=10)

label3 = Label(window,text="the sum is")
label3.grid(column=0,row=2,sticky='w')


entry3 = Label(window, text="allo", width =31)
entry3.focus_set()
entry3.grid(column=1,row=2,sticky='sw' ,columnspan=1, padx=10)

quit_button = Button(window,text="Quit", command=window.quit, pady=2)
quit_button.grid(column=0, row=3, sticky='sw', pady=20)

show_button = Button(window,text="show", pady=2)
show_button.grid(column=1, row=3, sticky='sw', pady=20)

window.mainloop()