from tkinter import *
from PIL import Image,ImageTk

class HomePage:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventery Managment System")
        self.root.geometry("780x510+380+160")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)
        self.focus_force()

        #====== Title =======

        self.icon_title=Image.open("images/logo.png")
        self.icon_title=self.icon_title.resize((50,50),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title=Label(self.root,text="Inventory Managment System",image=self.icon_title,compound=LEFT,font=("time new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)











if __name__=="__main__":
    root=Tk()
    obj=HomePage(root)
    root.mainloop()