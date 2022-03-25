from tkinter import *
from PIL import ImageTk,Image

class GetMobNo:
    def __init__(self,root):
        self.root=root
        self.root.geometry("300x130+500+200")
        self.root.title("")
        self.root.focus_force()
        self.root.resizable(False,False)
        self.userMobNo=""
        self.mobNoStatus=0

        self.mobNo=StringVar()

        self.icon_title=Image.open("images/phone-call.png")
        self.icon_title=self.icon_title.resize((30,30),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title=Label(self.root,text="Enter Mob No",image=self.icon_title,compound=LEFT,font=("time new roman",12,"bold"),bg="red",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1)


        self.mobNoEntry=Entry(self.root,width=20,font=("arial 15 bold"),justify="center",textvariable=self.mobNo)
        self.mobNoEntry.place(x=30,y=40)

        self.mobNoButton=Button(self.root,text="Set Mob No",font=("arial 15 bold"),bg="white",command=self.setMobNo)
        self.mobNoButton.place(x=70,y=70)


    def setMobNo(self):
        self.userMobNo=self.mobNo.get()
        messagebox.showinfo("sucess","Mob No "+self.userMobNo+" added sucessfully")
        self.root.destroy()

    def getMobNo(self):
        return self.userMobNo;


if __name__=="__main__":
    root=Tk()
    mob=GetMobNo(root)
    root.mainloop()