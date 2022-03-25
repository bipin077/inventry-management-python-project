from tkinter import *
from Database_files import Connection
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
from GetMobNo import GetMobNo

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventery Managment System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.mobNoStatus=0
        self.y=0

        # this is to store frame so that we have to use in flush.......
        self.dashboard_frames=[]

        self.total=0
        self.row=1
        self.user_mob_no=0

         ########### Temporary data storage area #############

        self.cartItemsData={
            "cartUseMobNo":"",
            "cartItemsName":[],
            "cartItemsPrice":[],
            "cartItemsQuantity":[]
        }

      



        #====== Title =======

        self.icon_title=Image.open("images/logo.png")
        self.icon_title=self.icon_title.resize((50,50),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title=Label(self.root,text="Inventory Managment System",image=self.icon_title,compound=LEFT,font=("time new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====== logout Button=======

        btn_logout=Button(self.root,text="logout",font=("new time roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        #=======clock======
        self.today_date=datetime.datetime.now()
        self.times=self.today_date.time()
        self.r_time=self.times.strftime("%X")
        self.lbl_clock=Label(self.root,text="Welcome To Inventory Managment System \t\t Date : "+ str(self.today_date.date()) +"\t\t Time :"+self.r_time,font=("time new roman",15,"bold"),bg="#4D636D",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)


        # ====== Left menu =======e

        self.menuLogo=Image.open("images/logo_1.png")
        self.menuLogo=self.menuLogo.resize((300,120),Image.ANTIALIAS)
        self.menuLogo=ImageTk.PhotoImage(self.menuLogo)
        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=102,width=300,height=565)
        
        lbl_menuLogo=Label(leftMenu,image=self.menuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        #self.icon_side=PhotoImage(file="images/side.jpg")
        self.icon_side=Image.open("images/side.jpg")
        self.icon_side=self.icon_side.resize((40,40),Image.ANTIALIAS)
        self.icon_side=ImageTk.PhotoImage(self.icon_side)
        lbl_menu=Label(leftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        btn_home=Button(leftMenu,text="Home",command=self.homePage,image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_insert=Button(leftMenu,text="Insert",command=self.insert,image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_update=Button(leftMenu,text="Update",command=self.update,image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_total_transaction=Button(leftMenu,text="Total Transaction",command=self.totalTransaction,image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_hold=Button(leftMenu,text="Hold",command=self.hold,image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_history=Button(leftMenu,text="History",command=self.history,image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        btn_discount=Button(leftMenu,text="Discount",command=self.discount,image=self.icon_side,bd=3,cursor="hand2",compound=LEFT,anchor="w",font=("times new roman",20,"bold")).pack(side=TOP,fill=X)
        


        # ============= center menu==============

        self.centerMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        self.centerMenu.place(x=300,y=102,width=800,height=565)
        #self.dashboard_frames.append(self.centerMenu)     
        
        self.homePage()        
        
        

        #======== Content =========================




        # =============footer================

        footer=Label(self.root,text="IMS : Inventory Managment System \n for any help please contact 9927948007",font=("time new roman",10,"bold"),bg="#4D636D",fg="white").pack(side=BOTTOM,fill=X)



    def setTotal(self):
        self.totalTitle=Label(self.rightMenu,text="Total : "+str(self.total)+u"\u20B9",pady=10,fg="blue",font="arial 18 bold",bg="white")
        self.totalTitle.place(x=10,y=400)




    def homePage(self):
        self.dashboardFlush()

        
        self.searchProductEntry=StringVar()
        self.productQuantityEntry=StringVar()

        self.searchProductFrame=Frame(self.centerMenu,bd=4,relief=RIDGE,bg="white")
        self.searchProductFrame.place(x=10,y=20,width=770,height=50)
        self.dashboard_frames.append(self.searchProductFrame)

        self.scanner_icon=Image.open("images/scanner_11.png")
        self.scanner_icon=self.scanner_icon.resize((50,40),Image.ANTIALIAS)
        self.scanner_icon=ImageTk.PhotoImage(self.scanner_icon)
        scanner_icon=Label(self.searchProductFrame,image=self.scanner_icon,padx=20).place(x=5,y=0)


        self.searchEntry=Entry(self.searchProductFrame,textvariable=self.searchProductEntry,bd=2,width=25,font="arial 15 bold")
        self.searchEntry.place(x=70,y=5)

        self.x_label=Label(self.searchProductFrame,text="X",bd=2,padx=10)
        self.x_label.place(x=380,y=10)

        self.quantityEntry=Entry(self.searchProductFrame,bd=2,textvariable=self.productQuantityEntry,width=5,font="arial 15 bold",justify=CENTER)
        self.quantityEntry.insert(0,"1")
        self.quantityEntry.place(x=450,y=7)

        self.searchButton=Button(self.searchProductFrame,text="Search Product",command=self.searchProduct,pady=5,font="arial 13 bold")
        self.searchButton.place(x=550,y=5)


        self.searchProductDetailFrame=Frame(self.centerMenu,bd=2,relief=RIDGE,bg="white")
        self.searchProductDetailFrame.place(x=10,y=100,width=770,height=450)
        self.dashboard_frames.append(self.searchProductDetailFrame)
        self.headerAddProduct()

        
        
        # ========= Right Menu=======

        self.rightMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        self.rightMenu.place(x=1100,y=102,width=200,height=565)
        self.dashboard_frames.append(self.rightMenu)


        lbl_cart_lbl=Label(self.rightMenu,text="Cart Products",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        self.listProducts=Text(self.rightMenu,width=30)
        self.listProducts.pack()

        

        self.checkout_btn=Button(self.rightMenu,text="Checkout ",command=self.checkout,pady=10,fg="white",font="arial 18 bold",bg="blue",width=20,cursor="hand2")
        self.checkout_btn.pack(side=BOTTOM)
        self.setTotal()





    def searchProduct(self):
        uniqueNo=self.searchProductEntry.get()
    
        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        query=self.cursor.execute("select product_name,price,quantity from products_detail where unique_id='"+uniqueNo+"'")
        record=self.cursor.fetchall()

        if len(record)<1:
            messagebox.showerror("error","Data not found in database")

        else:
            if int(self.productQuantityEntry.get())>int(record[0][2]):
                messagebox.showinfo("info",str(record[0][0])+" not enough this item available")
                self.homepage()

            else:            
                for data in record:
                    self.cartItemsData["cartItemsName"].append(data[0])
                    self.cartItemsData["cartItemsPrice"].append(data[1])
                    self.cartItemsData["cartUseMobNo"]="0"

                    self.total=self.total+data[1] 
 
                    self.addProductToDeshboard()  
                    self.setTotal()

    ################ showing title of name price & quantity ##########           

    def headerAddProduct(self):
        #self.dashboard_frames.append(frame)

        self.labelProductName=Label(self.searchProductDetailFrame,text="Product Name ",bg="white",font="arial 15 bold",width=18,pady=1,fg="blue")
        self.labelProductName.place(x=30,y=0)
      
        self.labelProductPrice=Label(self.searchProductDetailFrame,text="\t Price ",bg="white",font="arial 15 bold",width=18,pady=1,fg="blue")
        self.labelProductPrice.place(x=200,y=0)

        self.labelProductQuantity=Label(self.searchProductDetailFrame,text="\t Quantity",bg="white",width=18,font="arial 15 bold",pady=1,fg="blue")
        self.labelProductQuantity.place(x=400,y=0)

        

    
    def addProductToDeshboard(self):
        self.searchEntry.insert(0,"")

        self.y=self.y+30        

        for j in self.cartItemsData["cartItemsName"]:
            self.p_price=Label(self.searchProductDetailFrame,text=j,bg="white",font="arial 15 bold",width=18,pady=1,fg="black")
            self.p_price.place(x=20,y=self.y)
            

        for i in self.cartItemsData["cartItemsPrice"]:
            self.p_name=Label(self.searchProductDetailFrame,text=str(i)+" Rs",bg="white",font="arial 15 bold",width=18,pady=1,fg="black")
            self.p_name.place(x=240,y=self.y)
            

        self.cartItemsData["cartItemsQuantity"].append(self.productQuantityEntry.get())

        self.setQuantityLabel=Label(self.searchProductDetailFrame,text=self.productQuantityEntry.get(),bg="white",font="arial 15 bold",width=18,pady=1,fg="black")
        self.setQuantityLabel.place(x=440,y=self.y)

        self.setQuantityLabel=Button(self.searchProductDetailFrame,text="remove",font="arial 12 bold",fg="black",bg="white")
        self.setQuantityLabel.place(x=630,y=self.y)



        self.listProducts.insert(INSERT,"\n  "+str(j)+": \t X   "+str(self.productQuantityEntry.get())+" \t = "+str(i))
        
        self.row=self.row+1
    


    ######### screen Flush ##############

    def dashboardFlush(self):
        for i in self.dashboard_frames:
            i.destroy()




    def insert(self):
        self.dashboardFlush()


        self.insertFrameGui=Frame(self.centerMenu,bg="white")
        self.insertFrameGui.pack(expand=True)

        self.dashboard_frames.append(self.insertFrameGui)

        self.productName_q=StringVar()
        self.productName_e=StringVar()
        self.productPrice_e=StringVar()
        self.productCategory_e=StringVar()
        self.productQuantity_e=StringVar()

        self.productIdNo=Label(self.insertFrameGui,text="Insert Product : ",bg="white",padx=20,pady=10,font="arial 24 bold")
        self.productIdNo.grid(row=0,columnspan=2)
        self.dashboard_frames.append(self.productIdNo)

        self.productIdNo=Label(self.insertFrameGui,text="QR Code : ",bg="white",padx=20,pady=10,font="arial 15 bold")
        self.productIdNo.grid(row=1,column=0)
        self.dashboard_frames.append(self.productIdNo)

        self.productIdNoEntry=Entry(self.insertFrameGui,width=40,textvariable=self.productName_q)
        self.productIdNoEntry.grid(row=1,column=1)
        self.dashboard_frames.append(self.productIdNoEntry)

        self.productName=Label(self.insertFrameGui,text="Product Name : ",bg="white",padx=20,pady=10,font="arial 15 bold")
        self.productName.grid(row=2,column=0)
        self.dashboard_frames.append(self.productName)

        self.productNameEntry=Entry(self.insertFrameGui,bg="white",width=40,textvariable=self.productName_e)
        self.productNameEntry.grid(row=2,column=1)
        self.dashboard_frames.append(self.productNameEntry)

        self.productPrice=Label(self.insertFrameGui,text="Product Price : ",bg="white",padx=20,pady=10,font="arial 15 bold")
        self.productPrice.grid(row=3,column=0)
        self.dashboard_frames.append(self.productPrice)

        self.productPriceEntry=Entry(self.insertFrameGui,width=40,textvariable=self.productPrice_e)
        self.productPriceEntry.grid(row=3,column=1)
        self.dashboard_frames.append(self.productPriceEntry)

        self.productCateory=Label(self.insertFrameGui,text="Product Category : ",bg="white",padx=20,pady=10,font="arial 15 bold")
        self.productCateory.grid(row=4,column=0)
        self.dashboard_frames.append(self.productCateory)

        self.productCateoryEntry=Entry(self.insertFrameGui,width=40,textvariable=self.productCategory_e)
        self.productCateoryEntry.grid(row=4,column=1)
        self.dashboard_frames.append(self.productCateoryEntry)


        self.productQuantity=Label(self.insertFrameGui,text="Total Quantity : ",bg="white",padx=20,pady=10,font="arial 15 bold")
        self.productQuantity.grid(row=5,column=0)
        self.dashboard_frames.append(self.productQuantity)

        self.productQuantityEntry=Entry(self.insertFrameGui,width=40,textvariable=self.productQuantity_e)
        self.productQuantityEntry.grid(row=5,column=1)
        self.dashboard_frames.append(self.productQuantityEntry)

        self.addProduct=Button(self.insertFrameGui,text="Add Product",bg="white",font="arial 15 bold",command=self.insertItems)
        self.addProduct.grid(row=6,columnspan=2)
        self.dashboard_frames.append(self.addProduct)


    def insertItems(self):
        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()

        query="""insert into products_detail(product_name,unique_id,price,category,quantity) values (?,?,?,?,?);"""
        data_tupple=(self.productName_e.get(),self.productName_q.get(),self.productPrice_e.get(),self.productCategory_e.get(),self.productQuantity_e.get())
        self.cursor.execute(query,data_tupple)
        self.conn.commit()
        messagebox.showinfo("sucess","Product Inserted Sucessfully")
        self.cursor.close()
        self.conn.close()
        self.insert()
    
        

    def update(self):
        self.dashboardFlush()

        self.updateFrame=Frame(self.centerMenu)
        self.updateFrame.place(x=0,y=50,width=800,height=100)
        self.dashboard_frames.append(self.updateFrame)

        self.tkvar1 = StringVar(self.root)
        self.tkvar2 = StringVar(self.root)

        self.tkvar1.set("None")
        self.tkvar2.set("None")


        self.connection=Connection()
        self.conn=self.connection.getConnection()
        self.cursor=self.connection.getCursor()
        
        

        self.chooseCategoryLabel=Label(self.updateFrame, text="Choose A Category : ",pady=10,width=30,font="arial 13 bold")
        self.chooseCategoryLabel.place(x=50,y=10)

        query="select distinct category from products_detail"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        data=[]
        for row in records:
            data.append(row[0])
        

        self.chooseCategory=OptionMenu(self.updateFrame,self.tkvar1,*data)
        self.chooseCategory.place(x=400,y=15)
        

        self.getProductDetails=Button(self.updateFrame,text="Get Products",command=self.getProductc)
        self.getProductDetails.place(x=550,y=15)


    def getProductc(self):
        if self.tkvar1.get()!="None":
    
            self.chooseProductLabel=Label(self.updateFrame, text="Choose Product : ",width=20,pady=10,font="arial 13 bold")
            self.chooseProductLabel.place(x=100,y=50)
            


            query="select product_name from products_detail where category= '"+self.tkvar1.get()+"'"
            #tuple1=tuple(self.tkvar1.get())
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            data=[]
            for row in records:
                data.append(row[0])


            self.chooseProduct=OptionMenu(self.updateFrame,self.tkvar2,*data)
            self.chooseProduct.place(x=400,y=50)
            


            self.getProductDetails=Button(self.updateFrame,text="Get Product Detail",command=self.getUpdatedProduct)
            self.getProductDetails.place(x=550,y=50)
            

        else:
            messagebox.showerror("error","no category found")
    



    def getUpdatedProduct(self):

        self.updateFrameData=Frame(self.centerMenu)
        self.updateFrameData.place(x=0,y=200,width=800,height=300)
        self.dashboard_frames.append(self.updateFrameData)


        name=""
        price=0
        category=""
        quantity=0
        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        query="select product_name,price,category,quantity from products_detail where product_name='"+self.tkvar2.get()+"'"
        self.cursor.execute(query)
        result=self.cursor.fetchall()
        for data in result:
            name=data[0]
            price=data[1]
            category=data[2]
            quantity=data[3]
            

        self.g_productName_e=StringVar()
        self.g_productPrice_e=StringVar()
        self.g_productCategory_e=StringVar()
        self.g_productQuantity_e=StringVar()


        self.g_productName=Label(self.updateFrameData,text="Product Name : ",padx=20,pady=10,font="arial 15 bold")
        self.g_productName.grid(row=3,column=0)

        self.g_productNameEntry=Entry(self.updateFrameData,width=40,textvariable=self.g_productName_e)
        self.g_productNameEntry.insert(0,name)
        self.g_productNameEntry.grid(row=3,column=1)

        self.g_productPrice=Label(self.updateFrameData,text="Product Price : ",padx=20,pady=10,font="arial 15 bold")
        self.g_productPrice.grid(row=4,column=0)

        self.g_productPriceEntry=Entry(self.updateFrameData,width=40,textvariable=self.g_productPrice_e)
        self.g_productPriceEntry.insert(0,price)
        self.g_productPriceEntry.grid(row=4,column=1)

        self.g_productCateory=Label(self.updateFrameData,text="Product category : ",padx=20,pady=10,font="arial 15 bold")
        self.g_productCateory.grid(row=5,column=0)

        self.g_productCateoryEntry=Entry(self.updateFrameData,width=40,textvariable=self.g_productCategory_e)
        self.g_productCateoryEntry.insert(0,category)
        self.g_productCateoryEntry.grid(row=5,column=1)


        self.g_productQuantity=Label(self.updateFrameData,text="Product Quantity : ",padx=20,pady=10,font="arial 15 bold")
        self.g_productQuantity.grid(row=6,column=0)

        self.g_productQuantityEntry=Entry(self.updateFrameData,width=40,textvariable=self.g_productQuantity_e)
        self.g_productQuantityEntry.insert(0,quantity)
        self.g_productQuantityEntry.grid(row=6,column=1)

        self.g_addProduct=Button(self.updateFrameData,text="Update Product",font="arial 15 bold",command=self.updateDatabase)
        self.g_addProduct.grid(row=7,columnspan=2)


        self.cursor.close()
        self.conn.close()



    def updateDatabase(self):
        self.db=Connection()
        self.conn=self.db.getConnection()
        self.cursor=self.db.getCursor()

        name=self.g_productName_e.get()
        price=self.g_productPrice_e.get()
        category=self.g_productCategory_e.get()
        quantity=self.g_productQuantity_e.get()


        tuple1=(name,price,category,quantity,name)
        #update products_detail set product_name="pepsi",price=22 ,category="drinks" ,quantity=100 where product_name="pepsi";
        #query="""update products_detail set product_name='"+,price=?,category=? ,quantity=? where product_name=?"""
        self.cursor.execute("update products_detail set product_name='"+name+"', price='"+price+"', category='"+category+"', quantity='"+quantity+"' where product_name='"+name+"'")
        self.conn.commit()
        messagebox.showinfo("sucess","Data updated sucessfully")

        self.cursor.close()
        self.conn.close()



    def totalTransaction(self):
        pass


    def hold(self):
        pass


    def history(self):
        self.dashboardFlush()
        db_con=Connection()
        conn=db_con.getConnection()
        cursor=db_con.getCursor()

        dates_act=[]

        sql="select distinct date from Transactions"
        cursor.execute(sql)
        record=cursor.fetchall()
        for dates in record:
            dates_act.append(dates)  

        
        self.data = StringVar(self.root)
        self.data.set("Today")      



        self.productHistoryFilterFrame=Frame(self.centerMenu,bd=1,width=100,padx=20,pady=10)
        self.productHistoryFilterFrame.place(x=0,y=50,width=800,height=50)
        self.dashboard_frames.append(self.productHistoryFilterFrame)


        self.filterLabel=Label(self.productHistoryFilterFrame,text="Choose date : ",font="arial 15 bold")
        self.filterLabel.place(x=50,y=0)

        self.chooseFilter=OptionMenu(self.productHistoryFilterFrame,self.data,*dates_act)
        self.chooseFilter.place(x=250,y=0)

        self.filterButton=Button(self.productHistoryFilterFrame,text="Filter History",font="arial 15 bold",command=self.productHistoryDefault)
        self.filterButton.place(x=400,y=0)


        

        self.productHistoryDefault()



    def productHistoryDefault(self):

        selectedDate=self.data.get()
        org_date=selectedDate[2:12]

        if selectedDate=="Today":
            # present date
            datetime_now=datetime.datetime.now()
            date=datetime_now.date()
            
        else:
            date=org_date

        row_1=0

        db_con=Connection()
        conn=db_con.getConnection()
        cursor=db_con.getCursor()

        query="select * from Transactions where date='"+str(date)+"'"
        cursor.execute(query)
        records=cursor.fetchall()

        if(len(records)<1):
            messagebox.showwarning("Error","No data found of this date")

        self.productHistoryFrame=Frame(self.centerMenu,pady=10)
        self.productHistoryFrame.place(x=0,y=150,width=800,height=400)
        self.dashboard_frames.append(self.productHistoryFrame)


        self.date_1=Label(self.productHistoryFrame,text=" Date ",font="arial 15 bold",padx=20)
        self.date_1.grid(row=row_1,column=0)

        self.time_1=Label(self.productHistoryFrame,text="Time ",font="arial 15 bold",padx=20)
        self.time_1.grid(row=row_1,column=1)

        self.userMobNo_1=Label(self.productHistoryFrame,text=" Mob No ",font="arial 15 bold",padx=20)
        self.userMobNo_1.grid(row=row_1,column=2)

        self.paymentMode_1=Label(self.productHistoryFrame,text=" Payment Mode ",font="arial 15 bold",padx=20)
        self.paymentMode_1.grid(row=row_1,column=3)


        self.totalBill_1=Label(self.productHistoryFrame,text="Total Bill ",font="arial 15 bold",padx=20)
        self.totalBill_1.grid(row=row_1,column=4)
        
        for i in records:
            self.date=Label(self.productHistoryFrame,text=i[0],font="arial 15 bold",padx=20)
            self.date.grid(row=row_1+1,column=0)

            self.time=Label(self.productHistoryFrame,text=i[1],font="arial 15 bold",padx=20)
            self.time.grid(row=row_1+1,column=1)

            self.userMobNo=Label(self.productHistoryFrame,text=i[2],font="arial 15 bold",padx=20)
            self.userMobNo.grid(row=row_1+1,column=2)

            self.paymentMode=Label(self.productHistoryFrame,text=i[3],font="arial 15 bold",padx=20)
            self.paymentMode.grid(row=row_1+1,column=3)

            self.totalBill=Label(self.productHistoryFrame,text=i[4],font="arial 15 bold",padx=20)
            self.totalBill.grid(row=row_1+1,column=4)

            row_1=row_1+1


    def checkout(self):
        self.dashboardFlush()

        if self.total==0:
            messagebox.showerror("error","please buy something for doing checkout")
            self.homePage()

        else:

            self.radio=IntVar()

            self.paymentFrame=Frame(self.centerMenu)
            self.paymentFrame.place(x=0,y=10,width=800,height=200)
            self.dashboard_frames.append(self.paymentFrame)

            self.paymentTitle=Label(self.paymentFrame,text="Select Payment Mode",font="arial 20 bold",padx=30,pady=10)
            self.paymentTitle.place(x=200,y=10)
            

            self.byCard=Radiobutton(self.paymentFrame,text="By Debit/Credit Card",value=1,variable=self.radio,padx=30,font="arial 15 bold",pady=10)
            self.byCard.place(x=150,y=60)
            

            self.byCash=Radiobutton(self.paymentFrame,text="By Cash",padx=30,font="arial 15 bold",value=2,variable=self.radio,pady=10)
            self.byCash.place(x=450,y=60)
            

            self.pay=Button(self.paymentFrame,text="Generate Bill",padx=30,font="arial 15 bold",pady=10,command=self.payForm)
            self.pay.place(x=300,y=110)

            

####################### Selecting Payment Mode ##########################

    def payForm(self):

        self.paymentBillFrame=Frame(self.centerMenu)
        self.paymentBillFrame.place(x=0,y=220,width=800,height=150)
        self.dashboard_frames.append(self.paymentBillFrame)

        if self.radio.get()==1:
            self.payment_mode="card"
            
            self.payedAmountLabel=Label(self.paymentBillFrame,text="Total Bill Amount  : "+str(self.total)+" Rs",padx=30,font="arial 15 bold",pady=10)
            self.payedAmountLabel.place(x=200,y=10)
            

            self.totalAmount=Button(self.paymentBillFrame,text="Print Bill",padx=30,font="arial 15 bold",pady=10,command=self.totalPayBillTransaction)
            self.totalAmount.place(x=300,y=60)
            

        elif self.radio.get()==2:
            self.payment_mode="cash"
            self.payedAmountLabel=Label(self.paymentBillFrame,text="Total amount Payed : ",padx=30,font="arial 15 bold",pady=10)
            self.payedAmountLabel.place(x=200,y=10)
            

            self.payedAmountEntry=Entry(self.paymentBillFrame)
            self.payedAmountEntry.place(x=450,y=20)
            

            self.totalAmountLabel=Label(self.paymentBillFrame,text="Total Bill amount : ",padx=30,font="arial 15 bold",pady=10)
            self.totalAmountLabel.place(x=200,y=60)
            

            self.totalAmountEntry=Entry(self.paymentBillFrame)
            self.totalAmountEntry.place(x=450,y=70)
            

            self.totalAmount=Button(self.paymentBillFrame,text="Total Bill",padx=30,font="arial 15 bold",pady=10,command=self.totalPayBillTransaction)
            self.totalAmount.place(x=300,y=110)
            

        else:
            messagebox.showerror("error","select a payment mode first")

        

    def totalPayBillTransaction(self):
        datetime_now=datetime.datetime.now()

        # present time

        time=datetime_now.time()
        r_time=time.strftime("%X")
        
        # present date
        date=datetime_now.date()
    

    ################# setting user Mob No ############

        self.getActualMobNo()

        # connecting to database

        db_con=Connection()
        conn=db_con.getConnection()
        cursor=db_con.getCursor()

        cursor.execute("insert into Transactions('date','time','user_mob_no','payment_mode','total_bill') values('"+str(date)+"','"+str(r_time)+"','"+str(self.user_mob_no)+"','"+str(self.payment_mode)+"','"+str(self.total)+"')")
        conn.commit()

        cursor.close()
        conn.close()


        #updating data to database

        db_con=Connection()
        conn=db_con.getConnection()
        cursor=db_con.getCursor()

        for i in range(0,len(self.cartItemsData["cartItemsName"])):
            item=self.cartItemsData["cartItemsName"][i]
            quantity=self.cartItemsData["cartItemsQuantity"][i]

            query="select quantity from products_detail where product_name='"+item+"'"
            cursor.execute(query)
            quantity_real=cursor.fetchone()

            if int(quantity)>int(quantity_real[0]):
                messagebox.showinfo("info","not enough this item available")

            if int(quantity_real[0])<=10:
                messagebox.showinfo("info",item+" is going to empty please refill")

            quantity_updated=int(quantity_real[0])-int(quantity)
            cursor.execute("update products_detail set quantity='"+str(quantity_updated)+"' where product_name='"+item+"'")
            conn.commit()

        cursor.close()
        conn.close()


        messagebox.showinfo("sucess","Order sucessfullly")         

        self.total=0
        self.setTotal()
        self.user_mob_no=0
        self.mobNoStatus=0
        self.homePage()
        

 
        


    def discount(self):
        pass

    def getMobNo(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=GetMobNo(self.new_win)

    def getActualMobNo(self):
        mob=self.new_obj.getMobNo()
        self.user_mob_no=mob
        

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()