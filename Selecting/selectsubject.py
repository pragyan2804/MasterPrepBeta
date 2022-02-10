import tkinter as tk
root = tk.Tk()
root.geometry('1280x720')
root.title('SELECT TEST')
root.resizable(False, False)
bg = tk.PhotoImage(file='selectsubject.png')
root.eval('tk::PlaceWindow . center')
label1 = tk.Label(root, image=bg)
label1.place(x=0,y=0)

button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0).place(x=5,y=15, width=150, height=70)

button_sst = tk.Button(root,
                text='SST',
                font='BurbankBigCondensed-Bold 40',
                bg='#9518a4',
                fg='white',).place(x=86, y=350, width=325, height=195)

button_maths = tk.Button(root,
                text='MATHS',
                font='BurbankBigCondensed-Bold 40',
                bg='#ab9623',
                fg='white',).place(x=496, y=350, width=325, height=195)

button_maths = tk.Button(root,
                text='SCIENCE',
                font='BurbankBigCondensed-Bold 40',
                bg='#1eaf32',
                fg='white',).place(x=894, y=350, width=325, height=195)

root.mainloop()