import tkinter as tk
root = tk.Tk()
root.geometry('1280x720')
root.title('SELECT TEST')
root.resizable(False, False)
bg = tk.PhotoImage(file='selecttest.png')
root.eval('tk::PlaceWindow . center')
label1 = tk.Label(root, image=bg)
label1.place(x=0,y=0)

button_mcq = tk.Button(root,
                text='STANDARD MCQ TEST',
                font='BurbankBigCondensed-Bold 40',
                bg='#c32b2b',
                fg='white',).place(x=63, y=240, width=500, height=300)

button_mcq_comp = tk.Button(root,
                text='COMPETITIVE MASTERTEST',
                font='BurbankBigCondensed-Bold 35',
                bg='#c32b2b',
                fg='white',).place(x=723, y=240, width=500, height=300)

button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0).place(x=5,y=15, width=150, height=70)

root.mainloop()