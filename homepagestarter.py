from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import importlib
import tkinter
from tkinter import font
from tkinter.tix import IMAGETEXT
import PIL
from PIL import Image
import tkinter as tk
import tkinter.font as font



def homepageaction():
    root = Tk()
    root.geometry("1280x720")
    root.title("PrepMasterBETA")
    root.resizable(False, False)
    

    def signout():
        root.destroy()
        from login import loginaction
        loginaction()

    def homeflash1(e):
        homeflash()
    def homemcq1(e):
        homemcq()
    def homedoubt1(e):
        homedoubt()
    def homeleader1(e):
        homeleader()
    def selectsubject1(e):
        selectsubject()
    def selecttest1(e):
        selecttest()


    


    def homeflash():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\homeflash.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 1

        root.bind('<Left>',homeleader1)
        root.bind('<Right>',homemcq1)
        root.bind('<Return>',selectsubject1)

        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#22C53A",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homemcq())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#22C53A",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homeleader())
        less_display['font'] = less_font
        less_display.place(x=5, y=332, width=80, height=100)
        display = tkinter.Button(root, 
                            text = 'GO!',
                            font='BurbankBigCondensed-Bold 25',
                            bg='#57595c',
                            fg='white',
                            command = lambda:selectsubject()).place(x=480, y=486, width=320, height=75)

        display = tk.Button(root,
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#22C53A",
                            borderwidth=0,
                            command = lambda:signout()).place(x=970, y=1.15, width=300, height=50)


    def homemcq():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\homemcq.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 2

        root.bind('<Left>',homeflash1)
        root.bind('<Right>',homedoubt1)
        root.bind('<Return>',selecttest1)

        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#D92B2B",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homedoubt())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#D92B2B",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homeflash())
        less_display['font'] = less_font
        less_display.place(x=5, y=333, width=80, height=100)

        display = tk.Button(root, 
                            text = 'GO!',
                            font='BurbankBigCondensed-Bold 25',
                            bg='#57595c',
                            fg='white',
                            command = lambda:selecttest()).place(x=480, y=486, width=320, height=75)

        display = tk.Button(root,
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#D92B2B",
                            borderwidth=0,
                            command = lambda:signout()).place(x=970, y=1.15, width=300, height=50)

    def homeleader():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\homeleader.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 3
        root.bind('<Left>',homedoubt1)
        root.bind('<Right>',homeflash1)
        root.bind('<Return>',selectsubject1)

        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#C5AE22",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homeflash())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#C5AE22",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homedoubt())
        less_display['font'] = less_font
        less_display.place(x=5, y=332, width=80, height=100)

        display = tk.Button(root, 
                            text = 'GO!',
                            font='BurbankBigCondensed-Bold 25',
                            bg='#57595c',
                            fg='white',
                            command = lambda:selectsubject()).place(x=480, y=486, width=320, height=75)

        display = tk.Button(root,
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#C5AE22",
                            borderwidth=0,
                            command = lambda:signout()).place(x=970, y=1.15, width=300, height=50)
                        
    def homedoubt():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\homedoubt.png")
        label = Label(frame, image = img)
        label.pack()
        root.bind('<Left>',homemcq1)
        root.bind('<Right>',homeleader1)

        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#B327C4",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homeleader())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#B327C4",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homemcq())
        less_display['font'] = less_font
        less_display.place(x=5, y=332, width=80, height=100)

        display = tk.Button(root, 
                            text = 'GO!',
                            font='BurbankBigCondensed-Bold 25',
                            bg='#57595c',
                            fg='white').place(x=480, y=486, width=320, height=75)

        display = tk.Button(root,
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#B327C4",
                            borderwidth=0,
                            command = lambda:signout()).place(x=970, y=1.15, width=300, height=50)





    def selecttest():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\selecttest.png")
        label = Label(frame, image = img)
        label.pack()

        root.bind('<Escape>',homemcq1)

        button_mcq = tk.Button(root,
                text='STANDARD MCQ TEST',
                font='BurbankBigCondensed-Bold 40',
                bg='#c32b2b',
                fg='white',
                command = lambda:selectsubject()).place(x=63, y=240, width=500, height=300)

        button_mcq_comp = tk.Button(root,
                text='COMPETITIVE MASTERTEST',
                font='BurbankBigCondensed-Bold 35',
                bg='#c32b2b',
                fg='white',
                command = lambda:selectsubject()).place(x=723, y=240, width=500, height=300)

        button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0,
                command = lambda:homemcq()).place(x=5,y=15, width=150, height=70)

    def selectsubject():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\selectsubject.png")
        label = Label(frame, image = img)
        label.pack()

        
        if x==1:
            button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0,
                command = lambda:homeflash()).place(x=5,y=15, width=150, height=70)
        elif x==2:
            button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0,
                command = lambda:selecttest()).place(x=5,y=15, width=150, height=70)
        elif x==3:
            button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0,
                command = lambda:homeleader()).place(x=5,y=15, width=150, height=70)

        if x==1:
            root.bind('<Escape>',homeflash1)
        elif x==2:
            root.bind('<Escape>',selecttest1)
        elif x==3:
            root.bind('<Escape>',homeleader1)


        if x == 3:
            button_sst = tk.Button(root,
                        text='SST',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#9518a4',
                        fg='white',
                        command=leadssc).place(x=86, y=350, width=325, height=195)
            button_maths = tk.Button(root,
                        text='MATHS',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#ab9623',
                        fg='white',
                        command=leadmath).place(x=496, y=350, width=325, height=195)
            button_science = tk.Button(root,
                        text='SCIENCE',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#1eaf32',
                        fg='white',
                        command=leadsci).place(x=894, y=350, width=325, height=195)
            
        else:
            button_sst = tk.Button(root,
                            text='SST',
                            font='BurbankBigCondensed-Bold 40',
                            bg='#9518a4',
                            fg='white',
                            command=chapssc).place(x=86, y=350, width=325, height=195)

            button_maths = tk.Button(root,
                            text='MATHS',
                            font='BurbankBigCondensed-Bold 40',
                            bg='#ab9623',
                            fg='white',
                            command=chapmath).place(x=496, y=350, width=325, height=195)

            button_science = tk.Button(root,
                            text='SCIENCE',
                            font='BurbankBigCondensed-Bold 40',
                            bg='#1eaf32',
                            fg='white',
                            command=chapcsi).place(x=894, y=350, width=325, height=195)

    def leadershow():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\leaderboard.png")
        label = Label(frame, image = img)
        label.pack()
        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command=selectsubject).place(x=5,y=15, width=150, height=70)



    def chapssc():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\chapbg.png")
        label = Label(frame, image = img)
        label.pack()
        label_heading = tk.Label(root,
                            text='SELECT CHAPTER',
                            justify='center',
                            font='BurbankBigCondensed-Bold 70',
                            bg='#0073FF',
                            fg='white',
                            borderwidth=0).place(x=350, y=70, width=500, height=100)

        button_1 = tk.Button(root,
                        text='The Making Of National Movement',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#FE7D05',
                        fg='white').place(x=100, y=220, width=263, height=200)

        button_2 = tk.Button(root,
                        text='Resources',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#7FD10B',
                        fg='white').place(x=470, y=220, width=263, height=200)

        button_3 = tk.Button(root,
                        text='Industries',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#FFCA34',
                        fg='white').place(x=850, y=220, width=263, height=200)

        button_4 = tk.Button(root,
                        text='The Indian Constituion',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#F00272',
                        fg='white').place(x=250, y=500, width=263, height=200)

        button_5 = tk.Button(root,
                        text='Women, Caste And Reform',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#CD043F',
                        fg='white').place(x=650, y=500, width=263, height=200)

        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command=selectsubject).place(x=5,y=15, width=150, height=70)
        root.bind('<Escape>',selectsubject1)


    def chapmath():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\chapbg.png")
        label = Label(frame, image = img)
        label.pack()
        label_heading = tk.Label(root,
                    text='SELECT CHAPTER',
                    justify='center',
                    font='BurbankBigCondensed-Bold 70',
                    bg='#0073FF',
                    fg='white',
                    borderwidth=0).place(x=350, y=70, width=500, height=100)

        button_1 = tk.Button(root,
                        text='Linear Equations',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#FE7D05',
                        fg='white').place(x=100, y=220, width=263, height=200)

        button_2 = tk.Button(root,
                        text='Mensuration',
                        font='BurbankBigCondensed-Bold 30',
                        bg='#7FD10B',
                        fg='white').place(x=470, y=220, width=263, height=200)

        button_3 = tk.Button(root,
                        text='Exponents And Powers',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#CD043F',
                        fg='white').place(x=830, y=220, width=263, height=200)

        button_4 = tk.Button(root,
                        text='Sqaure And Square Roots',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#F30C0D',
                        fg='white').place(x=300, y=500, width=263, height=200)

        button_5 = tk.Button(root,
                        text='Cube And Cube Roots',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#FFCA34',
                        fg='white').place(x=700, y=500, width=263, height=200)

        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command=selectsubject).place(x=5,y=15, width=150, height=70)
        root.bind('<Escape>',selectsubject1)

    def chapcsi():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\chapbg.png")
        label = Label(frame, image = img)
        label.pack()        
        label_heading = tk.Label(root,
                    text='SELECT CHAPTER',
                    justify='center',
                    font='BurbankBigCondensed-Bold 70',
                    bg='#0073FF',
                    fg='white',
                    borderwidth=0).place(x=350, y=70, width=500, height=100)

        button_1 = tk.Button(root,
                        text='Crop Production And Management',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#FE7D05',
                        fg='white').place(x=100, y=220, width=263, height=200)

        button_2 = tk.Button(root,
                        text='Coal And Petroleum',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#F30C0D',
                        fg='white').place(x=470, y=220, width=263, height=200)

        button_3 = tk.Button(root,
                        text='Cell - Structure And Functions',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#7FD10B',
                        fg='white').place(x=850, y=220, width=263, height=200)

        button_4 = tk.Button(root,
                        text='Force And Pressure',
                        font='BurbankBigCondensed-Bold 30',
                        bg='#FFCA34',
                        fg='white').place(x=250, y=500, width=263, height=200)

        button_5 = tk.Button(root,
                        text='Light',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#F00272',
                        fg='white').place(x=650, y=500, width=263, height=200)

        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command = selectsubject).place(x=5,y=15, width=150, height=70)
        root.bind('<Escape>',selectsubject1)


    


    ################------BIGGER FUNCTIONS-------##########################
    def leadssc():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\leaderboard.png")
        label = Label(frame, image = img)
        label.pack()
        button_back = tkinter.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command = homeleader).place(x=5,y=15, width=150, height=70)

    def leadmath():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\leaderboard.png")
        label = Label(frame, image = img)
        label.pack()
        button_back = tkinter.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command = homeleader).place(x=5,y=15, width=150, height=70)
    def leadsci():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\leaderboard.png")
        label = Label(frame, image = img)
        label.pack()
        button_back = tkinter.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command = homeleader).place(x=5,y=15, width=150, height=70)

























                            

    homeflash()
    

    root.mainloop()


homepageaction()