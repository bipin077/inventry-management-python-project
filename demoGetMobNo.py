from tkinter import *
import GetMobNo

root=Tk()


class DemoMobNo:
    def __init__(self,root):
        self.root=root
        self.master=root


        self.btn=Button(self.root,text="getMobno",command=self.getMob)
        self.btn.pack()
        


        self.root.mainloop()

    def getMob(self):
        mobNo=GetMobNo.GetMobNo(self.master)
        userMobNo=mobNo.getMobNo()
        print("mob no"+str(userMobNo))




demo=DemoMobNo(root)

