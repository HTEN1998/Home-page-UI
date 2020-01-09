from tkinter import *
from tkinter import messagebox


class CURD():

    def __init__(self):
        self.root = Tk()
        self.root.geometry("480x480")
        


    def fetchData(self):
        pass

    def InsertData(self):
        messagebox.showinfo("Successfull", "Data Inserted")
        #self.root.update()


    def Oprs(self):
        title = Label(self.root,text="Insert Data\n",font = ("Courier bold", 11)).pack(side='top')
        Label(self.root, text="Email Id").pack()#(side='left')
        e1 = Entry(self.root).pack()
        Label(self.root, text="Name").pack()#(side='left')
        e2 = Entry(self.root).pack()#side='bottom')
        Label(self.root, text="Class").pack()#(side='left')
        e3 = Entry(self.root).pack()#side='bottom')
        Label(self.root, text="Department").pack()#(side='left')
        e4 = Entry(self.root).pack()#side='bottom')
        Label(self.root, text="Roll No").pack()#(side='left')
        e5 = Entry(self.root).pack()#side='bottom')
        Button(self.root , text ="Insert data").pack()








 

        Label(self.root, text="\n\nFetch Data\n",font=("courier bold",13)).pack()

        Label(self.root, text="Enter Email Id of the data to be fetched").pack()#(side='left')
        fetch_entry = Entry(self.root).pack()
        Button(self.root , text ="Fetch Data").pack()


        self.root.mainloop()


CURD().Oprs()
        


