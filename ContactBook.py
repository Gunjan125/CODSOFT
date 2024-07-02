from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
import pymysql
class ConnectorDB:
    def __init__(self,root):
        self.root=root
        titlespace=" "
        self.root.title(102* titlespace+"Contact Book")
        self.root.resizable(width=True, height=True)

        MainFrame =Frame(self.root,bd=10,width=770,height=700,relief=RIDGE)
        MainFrame.grid()

        TitleFrame =Frame (MainFrame,bd=7,width=770,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)

        TopFrame3=Frame(MainFrame,bd=5,width=770,height=500,relief=RIDGE)
        TopFrame3.grid(row=1,column=0)

        LeftFrame=Frame(TopFrame3,bd=5,width=770,height=400,padx=2,bg='cadet blue' ,relief=RIDGE)
        LeftFrame.pack(side=RIGHT)
        LeftFrame1=Frame(LeftFrame,bd=5,width=600,height=180,padx=12,pady=9,relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 =Frame(TopFrame3,bd=5,width=100,height=400,padx=2,bg="cadet blue",relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFramela=Frame(RightFrame1,bd=5,width=90,height=300,padx=2,pady=2,relief=RIDGE)
        RightFramela.pack(side=TOP)

        # ----------------------------------------------------------------------------------------------

        
        Name=StringVar()   
        Mobile=StringVar()
        Email=StringVar()
        Address=StringVar()
        

        def iExit():
            iExit=tkinter.messagebox.askyesno("Contact Book","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return
            
        def Reset():
            
            self.entName.delete(0,END)
            self.entMobile.delete(0,END)
            self.entEmail.delete(0,END)
            self.entAddress.delete(0,END)
          
            


        def adddata():
            if Name.get()=="" or Mobile.get()=="":
                tkinter.messagebox.showerror("Contact Book","Enter correct details")
            else:
                sqlcon=pymysql.connect(host="localhost",user="root",password="Password",database="contactbook")
                cur=sqlcon.cursor()
                cur.execute("insert into contactbook values(%s,%s,%s,%s)",(
                    Name.get(),Mobile.get(),Email.get(),Address.get()))
                sqlcon.commit()
                sqlcon.close()
                tkinter.messagebox.showinfo("Contact Book","Record added successfully!!")

        def displaydata():
            sqlcon=pymysql.connect(host="localhost",user="root",password="Password",database="contactbook")
            cur=sqlcon.cursor()
            cur.execute("select * from contactbook")
            result=cur.fetchall()
            if len(result)!=0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('',END,values=row)
            sqlcon.commit()
            sqlcon.close()
            # tkinter.messagebox.showinfo("Mysql database ","Record entered successfully")


        def Info(ev):
            viewInfo=self.student_records.focus()
            learnerdata=self.student_records.item(viewInfo)
            row=learnerdata['values']
            Name.set(row[0]),Mobile.set(row[1]),Email.set(row[2]),Address.set(row[3])



        def update():
            sqlcon=pymysql.connect(host="localhost",user="root",password="Password",database="contactbook")
            cur=sqlcon.cursor()
            cur.execute("update  contactbook set mobile=%s,email=%s,address=%s where name=%s",(Mobile.get(),Email.get(),Address.get(),Name.get()))
            sqlcon.commit()
            sqlcon.close()
            tkinter.messagebox.showinfo("Contact Book","Record updated successfully!!")


        def delete():
            sqlcon=pymysql.connect(host="localhost",user="root",password="Password",database="contactbook")
            cur=sqlcon.cursor()
            cur.execute("delete from  contactbook where  name=%s",Name.get())
            sqlcon.commit()
            sqlcon.close()
            tkinter.messagebox.showinfo("Contact Book","Record deleted successfully!!")
            # Reset()

        def search():
            try:
                sqlcon=pymysql.connect(host="localhost",user="root",password="Password",database="contactbook")
                cur=sqlcon.cursor()

                
                cur.execute("SELECT * FROM contactbook WHERE name=%s OR mobile=%s", ( Name.get(), Mobile.get() ))

                row=cur.fetchone()

                Name.set(row[0]),Mobile.set(row[1]),Email.set(row[2]),Address.set(row[3])
                
                sqlcon.commit()
            except:
                
                tkinter.messagebox.showinfo("Contact Book","No Record found!! ")
                # Reset()
            sqlcon.close()


            


        # ----------------------------------------------------------------------------------------------

        self.lbltitle=Label(TitleFrame,font=('arial',40,'bold'),text="Contact Book",bd=7,fg='dark blue')
        self.lbltitle.grid(row=0,column=0,padx=0)

        
       


        self.lblName=Label(LeftFrame1,font=('arial',12,'bold'),text="Name",bd=7)
        self.lblName.grid(row=1,column=0,sticky=W,padx=5)
        self.entName=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=Name )
        self.entName.grid(row=1,column=1,sticky=W,padx=5)


        
        self.lblMobile=Label(LeftFrame1,font=('arial',12,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=2,column=0,sticky=W,padx=5)
        self.entMobile=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left' ,textvariable=Mobile)
        self.entMobile.grid(row=2,column=1,sticky=W,padx=5)


        
        self.lblEmail=Label(LeftFrame1,font=('arial',12,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=3,column=0,sticky=W,padx=5)
        self.entEmail=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left' ,textvariable=Email)
        self.entEmail.grid(row=3,column=1,sticky=W,padx=5)


        self.lblAddress=Label(LeftFrame1,font=('arial',12,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=4,column=0,sticky=W,padx=5)
        self.entAddress=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left' ,textvariable=Address)
        self.entAddress.grid(row=4,column=1,sticky=W,padx=5)




        # ---------------------------------------------Table TreeView------------------------------------------------------------------

        scroll_y=Scrollbar(LeftFrame,orient=VERTICAL)
        

        self.student_records=ttk.Treeview(LeftFrame,height=12,columns=("Name","Mobile","Email","Address"),yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT,fill=Y)

        
        self.student_records.heading("Name",text="Name")
        self.student_records.heading("Mobile",text="Mobile")
        self.student_records.heading("Email",text="Email")
        self.student_records.heading("Address",text="Address")
        
        

        self.student_records['show']='headings'


        
        self.student_records.column("Name",width=100)
        self.student_records.column("Mobile",width=100)
        self.student_records.column("Email",width=100)
        self.student_records.column("Address",width=100)
        
        

        self.student_records.pack(fill=BOTH,expand=1)

        self.student_records.bind("<ButtonRelease-1>",Info)

        # ---------------------------------------------------------------------------------------------------------------

        self.btnAddNew=Button(RightFramela,font=('arial',16,'bold'),text='Add Contact',bd=4,bg='cadet blue',fg='white',pady=1,padx=24,width=8,height=2
                              ,command=adddata).grid(row=0,column=0,padx=1)

        self.btnDisplay=Button(RightFramela,font=('arial',16,'bold'),text='View Contact',bd=4,bg='cadet blue',fg='white',pady=1,padx=24,width=8,height=2
                               ,command=displaydata).grid(row=1,column=0,padx=1)

        self.btnSearch=Button(RightFramela,font=('arial',16,'bold'),text='Search Contact',bd=4,bg='cadet blue',fg='white',pady=1,padx=24,width=8,height=2
                              ,command=search).grid(row=2,column=0,padx=1)


        self.btnUpdate=Button(RightFramela,font=('arial',16,'bold'),text='Update Contact',bd=4,bg='cadet blue',fg='white',pady=1,padx=24,width=8,height=2
                              ,command=update).grid(row=3,column=0,padx=1)


        self.btnDelete=Button(RightFramela,font=('arial',16,'bold'),text='Delete Contact',bd=4,bg='cadet blue',fg='white',pady=1,padx=24,width=8,height=2
                              ,command=delete).grid(row=4,column=0,padx=1)


        self.btnReset=Button(RightFramela,font=('arial',16,'bold'),text='Reset',bd=4,bg='cadet blue',fg='white',pady=1,padx=24,width=8,height=2
                             ,command=Reset).grid(row=5,column=0,padx=1)


        self.btnExit=Button(RightFramela,font=('arial',16,'bold'),text='Exit',bd=4,bg='cadet blue',fg='white',pady=1,padx=24,width=8,height=2
                            ,command=iExit).grid(row=6,column=0,padx=1)


if __name__=='__main__':
    root=Tk()
    application=ConnectorDB(root)
    root.mainloop()


