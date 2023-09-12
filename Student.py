######################################################################
# -------------------------------------------------------------------#
#|                       Programmer Info                            |#
#--------------------------------------------------------------------#
#|                  Author     :   Abhishek Patel                   |#
#|                  Programmer :   Abhishek Patel                   |#
#|                  Blog       :   codewithmobile.tech.blog         |#
#|                  Product    :   Student Management System        |#
#|                 __Copyright__ By CodeWithMobile                  |#
#|                 __License__ By CodeWithMobile                    |#
#--------------------------------------------------------------------#
######################################################################

from tkinter import *
from tkinter import ttk
import pymysql #pip install pymysql
from tkinter import messagebox
from PIL import ImageTk,Image #pip install pillow
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------Start-------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1430x830+0+0")
        self.root.resizable(0,0)
        # self.root.wm_iconbitmap('python.ico')
        self.Normal='Cyan'
        self.green='lightgreen'
        self.yellow='yellow'
        self.Welcome=Label(self.root,text="Student Management System",bd=3,relief=RIDGE,font="Times 30 bold",bg="cyan")
        self.Welcome.pack(side=TOP,fill=X)
        self.bli()
        self.root.config(bg="#dddefe")

#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#-------------------------------Manage Frame Store Entry--------------------------
#=================================================================================
        self.Var_Roll=IntVar()
        self.Var_Name=StringVar()
        self.Var_Father_Name=StringVar()
        self.Var_Mother_Name=StringVar()
        self.Var_Gender=StringVar()
        self.Var_Class=StringVar()
        self.Var_Contact=StringVar()
        self.Var_DOB=StringVar()
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#-------------------------------Data Frame Store Entry----------------------------
#=================================================================================
        self.SearchBy=StringVar()
        self.S_E=StringVar()
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        #=================================================================================
        #------------------------------Manage Or Entry Frame------------------------------
        #=================================================================================
        ManageFrame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        ManageFrame.place(x=20,y=65,width=450,height=750)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        
        self.M_title=Label(ManageFrame,text="Manage Student",bg="white",fg='#3A3B3C',font="Times 30 bold")
        self.M_title.grid(row=0,columnspan=2,pady=20,padx=75)


#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.M_Roll=Label(ManageFrame,text="Roll No.",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.M_Roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")
        self.E_Roll=Entry(ManageFrame,bg="lightgrey",textvariable=self.Var_Roll,font="Times 15 bold",bd=0)
        self.E_Roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")
        self.E_Roll.delete('0',END)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.M_Name=Label(ManageFrame,text="Name",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.M_Name.grid(row=2,column=0,pady=10,padx=10,sticky="w")
        self.E_Name=Entry(ManageFrame,bg="lightgrey",textvariable=self.Var_Name,font="Times 15 bold",bd=0)
        self.E_Name.grid(row=2,column=1,pady=10,padx=10,sticky="w")
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.M_Father_Name=Label(ManageFrame,text="Father Name",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.M_Father_Name.grid(row=3,column=0,pady=10,padx=10,sticky="w")
        self.E_Father_Name=Entry(ManageFrame,bg="lightgrey",textvariable=self.Var_Father_Name,font="Times 15 bold",bd=0)
        self.E_Father_Name.grid(row=3,column=1,pady=10,padx=10,sticky="w")
#-------self.---------------------------------------------------------------------------------------------------------------------
#-------self.---------------------------------------------------------------------------------------------------------------------
        self.M_Mother_Name=Label(ManageFrame,text="Mother Name",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.M_Mother_Name.grid(row=4,column=0,pady=10,padx=10,sticky="w")
        self.E_Mother_Name=Entry(ManageFrame,bg="lightgrey",textvariable=self.Var_Mother_Name,font="Times 15 bold",bd=0)
        self.E_Mother_Name.grid(row=4,column=1,pady=10,padx=10,sticky="w")
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.M_Gender=Label(ManageFrame,text="Gender",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.M_Gender.grid(row=5,column=0,pady=10,padx=10,sticky="w")
        self.ComboGender=ttk.Combobox(ManageFrame,font="Times 13 bold",state='readonly',textvariable=self.Var_Gender)
        self.ComboGender['values']=('Male','Female','Other')
        self.ComboGender.grid(row=5,column=1,pady=10,padx=10,sticky="w")
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.M_Class=Label(ManageFrame,text="Class",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.M_Class.grid(row=6,column=0,pady=10,padx=10,sticky="w")
        self.ComboClass=ttk.Combobox(ManageFrame,font="Times 13 bold",state='readonly',textvariable=self.Var_Class)
        self.ComboClass['values']=('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th')
        self.ComboClass.grid(row=6,column=1,pady=10,padx=10,sticky="w")
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.M_Contact=Label(ManageFrame,text="Contact",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.M_Contact.grid(row=7,column=0,pady=10,padx=10,sticky="w")
        self.E_Contact=Entry(ManageFrame,bg="lightgrey",textvariable=self.Var_Contact,font="Times 15 bold",bd=0)
        self.E_Contact.grid(row=7,column=1,pady=10,padx=10,sticky="w")
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.M_DOB=Label(ManageFrame,text="D.O.B",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.M_DOB.grid(row=8,column=0,pady=10,padx=10,sticky="w")
        self.E_DOB=Entry(ManageFrame,bg="lightgrey",textvariable=self.Var_DOB,font="Times 15 bold",bd=0)
        self.E_DOB.grid(row=8,column=1,pady=10,padx=10,sticky="w")
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        M_Address=Label(ManageFrame,text="Address",bg="white",fg="#3A3B3C",font="Times 20 bold")
        M_Address.grid(row=9,column=0,pady=10,padx=10,sticky="w")
        self.E_Address=Text(ManageFrame,width=20,height=4,font="Times 15 bold",bg="lightgrey",bd=0)
        self.E_Address.grid(row=9,column=1,pady=10,padx=10,sticky="w")
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#-----------------------------------Btn Frame-------------------------------------
#=================================================================================
        btnFrame=Frame(ManageFrame,bd=1,relief=RIDGE,bg="lightgrey")
        btnFrame.place(x=8,y=664,width=430,height=70)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        Add=Button(btnFrame,text="Add",width=10,command=self.Add).grid(row=0,column=0,pady=22,padx=14)
        Update=Button(btnFrame,text="Update",width=10,command=self.Update).grid(row=0,column=1,pady=22,padx=14)
        Delete=Button(btnFrame,text="Delete",width=10,command=self.Delete_Data).grid(row=0,column=2,pady=22,padx=14)
        Clear=Button(btnFrame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,pady=22,padx=14)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#-----------------------------------Data Frame------------------------------------
#=================================================================================
        DataFrame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        DataFrame.place(x=500,y=65,width=900,height=750)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.D_labl1=Label(DataFrame,text="Search By",bg="white",fg="#3A3B3C",font="Times 20 bold")
        self.D_labl1.grid(row=0,column=0,pady=10,padx=10,sticky="w")
        self.ComboSearch=ttk.Combobox(DataFrame,width=14,textvariable=self.SearchBy,font="Times 13 bold",state='readonly')
        self.ComboSearch['values']=('Roll','Name','Contact')
        self.ComboSearch.grid(row=0,column=1,pady=10,padx=10,sticky="w")
        self.Searchlbl1=Entry(DataFrame,bg="lightgrey",font="Times 15 bold",textvariable=self.S_E,bd=0,fg="#3A3B3C")
        self.Searchlbl1.grid(row=0,column=2,pady=10,padx=10,sticky="w")
        self.Searchbtn=Button(DataFrame,text="Search",command=self.Find,width=20,font="Times 10 bold",bg="#3A3B3C",fg="White").grid(row=0,column=3,pady=22,padx=14)
        self.Showallbtn=Button(DataFrame,text="Show All",command=self.fetch_data,width=20,font="Times 10 bold",bg="#3A3B3C",fg="White").grid(row=0,column=4,pady=22,padx=14)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        #=================================================================================
        #------------------------------Table Frame----------------------------------------
        #=================================================================================
        TbFrame=Frame(DataFrame,bd=3,relief=RIDGE,bg="lightgrey")
        TbFrame.place(x=10,y=65,width=872,height=670)
        x_scroll=Scrollbar(TbFrame,orient=HORIZONTAL)
        y_scroll=Scrollbar(TbFrame,orient=VERTICAL)
        self.Student_Tb=ttk.Treeview(TbFrame,column=('Roll','Name','Father Name','Mother Name','Gender','Class','Contact','D.O.B','Address'),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)
        x_scroll.pack(side=BOTTOM,fill=X)
        y_scroll.pack(side=RIGHT,fill=Y)
        x_scroll.config(command=self.Student_Tb.xview)
        y_scroll.config(command=self.Student_Tb.yview)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
        self.Student_Tb.heading("Roll",text="Roll No.")
        self.Student_Tb.heading("Name",text="Name")
        self.Student_Tb.heading("Father Name",text="Father Name")
        self.Student_Tb.heading("Mother Name",text="Mother Name")
        self.Student_Tb.heading("Gender",text="Gender")
        self.Student_Tb.heading("Class",text="Class")
        self.Student_Tb.heading("Contact",text="Contact")
        self.Student_Tb.heading("D.O.B",text="D.O.B")
        self.Student_Tb.heading("Address",text="Address")
        self.Student_Tb['show']='headings'
        self.Student_Tb.column("Roll",width=100)
        self.Student_Tb.column("Name",width=200)
        self.Student_Tb.column("Father Name",width=200)
        self.Student_Tb.column("Mother Name",width=200)
        self.Student_Tb.column("Gender",width=100)
        self.Student_Tb.column("Class",width=100)
        self.Student_Tb.column("Contact",width=100)
        self.Student_Tb.column("D.O.B",width=100)
        self.Student_Tb.column("Address",width=250)
        self.Student_Tb.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_Tb.bind("<ButtonRelease-1>",self.cursors)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#------------------------------Add Function---------------------------------------
#=================================================================================







    def Add(self):
        if self.E_Roll.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Roll.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)

        elif self.E_Roll.get()[0] in (' ','<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)

            
        
        elif self.E_Roll.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)
        

        
 

        elif self.E_Name.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Name.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
            self.E_Name.delete(0,END)

        elif self.E_Name.get()[0] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
            self.E_Name.delete(0,END)

            
        
        elif self.E_Name.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
            self.E_Name.delete(0,END)
        elif self.E_Father_Name.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Father_Name.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Father Name. !!!")
            self.E_Father_Name.delete(0,END)

        elif self.E_Father_Name.get()[0] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Father Name. !!!")
            self.E_Father_Name.delete(0,END)

            
        
        elif self.E_Father_Name.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            messagebox.showerror("Wrong Value","Please Type Valid Father Name. !!!")


        elif self.E_Mother_Name.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Mother_Name.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Mother Name. !!!")
            self.E_Mother_Name.delete(0,END)

        elif self.E_Mother_Name.get()[0] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Mother Name. !!!")
            self.E_Mother_Name.delete(0,END)

            
        
        elif self.E_Mother_Name.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            messagebox.showerror("Wrong Value","Please Type Valid Mother Name. !!!")
        elif self.ComboGender.get()=="":            
            messagebox.showerror("Error","All Feild Are required!!!")
        elif self.ComboClass.get()=="":            
            messagebox.showerror("Error","All Feild Are required!!!")

            
        elif self.E_Contact.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")
        elif self.E_Contact.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Contact No. !!!")
            self.E_Contact.delete(0,END)

        elif self.E_Contact.get()[0] in (' ','<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Contact No. !!!")
            self.E_Contact.delete(0,END)

            
        
        elif self.E_Contact.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Contact No. !!!")
            self.E_Contact.delete(0,END)
        elif self.Var_DOB.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")
        elif self.E_DOB.get()[::1] in ('<','>',' ',',','.',';',':','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid D.O.B !!!")
            self.E_DOB.delete(0,END)

        elif self.E_DOB.get()[::-1] in (" ",'<','>',',',' ','.',';',':','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid D.O.B !!!")
            self.E_DOB.delete(0,END)

            
        
        elif self.E_DOB.get()[-1::] in ('<','>',' ',',','.',';',':','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid D.O.B !!!")
            self.E_DOB.delete(0,END)


        elif self.E_Address.get()=="":
                messagebox.showerror("Empty","Feild Are required!!!")
        elif self.E_Address.get()[::1] in ('<','>','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"','1','2','3','4','5','6','7','8','9','0'):
            messagebox.showerror("Wrong Value","Please Type Valid Address. !!!")
            self.E_Address.delete(0,END)

        elif self.E_Address.get()[0] in (' ','<','>','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Address. !!!")
            self.E_Address.delete(0,END)

            
        
        elif self.E_Address.get()[-1::] in ('<','>','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Address. !!!")
            self.E_Address.delete(0,END)
        else:
            conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
            cur=conn.cursor()
            cur.execute("select * from student_management_system where Roll=%s",self.Var_Roll.get())
            if cur.fetchone():
                messagebox.showerror('Error','This Roll Number Is Already Exists')
            else:
                conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
                cur=conn.cursor()
                cur.execute("insert into student_management_system values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Var_Roll.get(),self.Var_Name.get(),self.Var_Father_Name.get(),self.Var_Mother_Name.get(),self.Var_Gender.get(),self.Var_Class.get(),self.Var_Contact.get(),self.Var_DOB.get(),self.E_Address.get('1.0',END)))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                messagebox.showinfo("Data Inserted","Success")









#=================================================================================
#------------------------------Add Data Function End------------------------------
#=================================================================================



#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------








#=================================================================================
#------------------------------Fetch Data Function--------------------------------
#=================================================================================
    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
        cur=conn.cursor()
        cur.execute("select * from student_management_system")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Tb.delete(*self.Student_Tb.get_children())
            for row in rows:
                self.Student_Tb.insert('',END,values=row)
                conn.commit()
        conn.close()
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#------------------------------Clear Function---------------------------------------
#=================================================================================
    def clear(self):
        self.Var_Roll.set("")
        self.Var_Name.set("")
        self.Var_Father_Name.set("")
        self.Var_Mother_Name.set("")
        self.Var_Gender.set("")
        self.Var_Class.set("")
        self.Var_Contact.set("")
        self.Var_DOB.set("")
        self.E_Address.delete('1.0',END)
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#------------------------------Cursor Function---------------------------------------
#=================================================================================
    def cursors(self,ev):
        curso=self.Student_Tb.focus()
        content=self.Student_Tb.item(curso)
        row=content['values']
        self.Var_Roll.set(row[0])
        self.Var_Name.set(row[1])
        self.Var_Father_Name.set(row[2])
        self.Var_Mother_Name.set(row[3])
        self.Var_Gender.set(row[4])
        self.Var_Class.set(row[5])
        self.Var_Contact.set(row[6])
        self.Var_DOB.set(row[7])
        self.E_Address.delete('1.0',END)
        self.E_Address.insert(END,row[8])
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#------------------------------Update Function------------------------------------
#=================================================================================
    def Update(self):
        if self.E_Roll.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Roll.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)

        elif self.E_Roll.get()[0] in (' ','<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)

            
        
        elif self.E_Roll.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)


        elif self.E_Name.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Name.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
            self.E_Name.delete(0,END)

        elif self.E_Name.get()[0] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
            self.E_Name.delete(0,END)

            
        
        elif self.E_Name.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
            self.E_Name.delete(0,END)
        elif self.E_Father_Name.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Father_Name.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Father Name. !!!")
            self.E_Father_Name.delete(0,END)

        elif self.E_Father_Name.get()[0] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Father Name. !!!")
            self.E_Father_Name.delete(0,END)

            
        
        elif self.E_Father_Name.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            messagebox.showerror("Wrong Value","Please Type Valid Father Name. !!!")


        elif self.E_Mother_Name.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Mother_Name.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Mother Name. !!!")
            self.E_Mother_Name.delete(0,END)

        elif self.E_Mother_Name.get()[0] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Mother Name. !!!")
            self.E_Mother_Name.delete(0,END)

            
        
        elif self.E_Mother_Name.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            messagebox.showerror("Wrong Value","Please Type Valid Mother Name. !!!")


            
        elif self.E_Contact.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")
        elif self.E_Contact.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Contact No. !!!")
            self.E_Contact.delete(0,END)

        elif self.E_Contact.get()[0] in (' ','<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Contact No. !!!")
            self.E_Contact.delete(0,END)

            
        
        elif self.E_Contact.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Contact No. !!!")
            self.E_Contact.delete(0,END)
        elif self.Var_DOB.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")
        elif self.E_DOB.get()[::1] in ('<','>',' ',',','.',';',':','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid D.O.B !!!")
            self.E_DOB.delete(0,END)

        elif self.E_DOB.get()[0] in ('<','>',',',' ','.',';',':','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid D.O.B !!!")
            self.E_DOB.delete(0,END)

            
        
        elif self.E_DOB.get()[-1::] in ('<','>',' ',',','.',';',':','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid D.O.B !!!")
            self.E_DOB.delete(0,END)
        elif self.E_Address.get('1.0',END)=="":
                messagebox.showerror("Empty","Feild Are required!!!")
        elif self.E_Address.get('1.0',END)[::1] in ('<','>','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"','1','2','3','4','5','6','7','8','9','0'):
            messagebox.showerror("Wrong Value","Please Type Valid Address. !!!")
            self.E_Address.delete('1.0',END)

        elif self.E_Address.get('1.0',END)[0] in (' ','<','>','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Address. !!!")
            self.E_Address.delete('1.0',END)

            
        
        elif self.E_Address.get('1.0',END)[-1::] in ('<','>','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                '1','2','3','4','5','6','7','8','9','0'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Address. !!!")
            self.E_Address.delete('1.0',END)
        else:
            conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
            cur=conn.cursor()
            cur.execute(f"select * from student_management_system WHERE Roll={self.Var_Roll.get()}")
            if not cur.fetchall():
                messagebox.showerror("Roll No.","This Roll Number Is Not Exist")
            elif self.E_Name.get()=="":
                messagebox.showerror("Error","All Feild Are required!!!")
            elif self.E_Contact.get()=="":
                messagebox.showerror("Error","All Feild Are required!!!")
            elif self.E_DOB.get()=="":
                messagebox.showerror("Error","All Feild Are required!!!")
            else:
                conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
                cur=conn.cursor()
                cur.execute(f"UPDATE `student_management_system` SET `Roll`='{self.Var_Roll.get()}',`Name`='{self.Var_Name.get()}',`Father_Name`='{self.Var_Father_Name.get()}',`Mother_Name`='{self.Var_Mother_Name.get()}',`Gender`='{self.Var_Gender.get()}',`Class`='{self.Var_Class.get()}',`Contact`='{self.Var_Contact.get()}',`DOB`='{self.Var_DOB.get()}',`Address`='{self.E_Address.get('1.0',END)}' WHERE Roll={self.Var_Roll.get()}")
                conn.commit()
                messagebox.showinfo("Update","Data Updated")
                self.fetch_data()
                self.clear()
                conn.close()
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#------------------------------Delete Function------------------------------------
#=================================================================================
    def Delete_Data(self):
        if self.E_Roll.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")

        elif self.E_Roll.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)

        elif self.E_Roll.get()[0] in (' ','<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)

            
        
        elif self.E_Roll.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
            #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            
            messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
            self.E_Roll.delete(0,END)
        elif self.E_Name.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")
        elif self.E_Contact.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")
        elif self.E_DOB.get()=="":
            messagebox.showerror("Error","All Feild Are required!!!")
        else:
            conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
            cur=conn.cursor()
            cur.execute("delete from student_management_system where Roll=%s",self.Var_Roll.get())
            conn.commit()
            messagebox.showinfo("Delete","Data Deleted")
            self.fetch_data()
            self.clear()
            conn.close()
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#=================================================================================
#------------------------------Find Function--------------------------------------
#=================================================================================
    def Find(self):
        if self.SearchBy.get()=="":
            messagebox.showerror("SearchBy","Please Select Search Method")
            self.Searchlbl1.delete(0,END)
            self.Searchlbl1.focus_force()
        elif self.ComboSearch.get()=="Roll":
            if self.Searchlbl1.get()=="":
                messagebox.showerror("Empty","Feild Are required!!!")

            elif self.Searchlbl1.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                    'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
                self.Searchlbl1.delete(0,END)

            elif self.Searchlbl1.get()[0] in (' ','<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                    'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
                self.Searchlbl1.delete(0,END)

                
            
            elif self.Searchlbl1.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                    'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Roll No. !!!")
                self.Searchlbl1.delete(0,END)
            else:
                conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
                cur=conn.cursor()
                cur.execute(f"select * from student_management_system where {str(self.SearchBy.get())} LIKE '%{str(self.S_E.get())}%'")
                if not cur.fetchall():
                    messagebox.showerror("Empty","No Data Found")
                else:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
                    cur=conn.cursor()
                    cur.execute(f"select * from student_management_system where {str(self.SearchBy.get())} LIKE '%{str(self.S_E.get())}%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                        self.Student_Tb.delete(*self.Student_Tb.get_children())
                        for row in rows:
                            self.Student_Tb.insert('',END,values=row)
                        conn.commit()
                    conn.close()

        elif self.ComboSearch.get()=="Name":
            if self.Searchlbl1.get()=="":
                messagebox.showerror("Empty","Feild Are required!!!")
            elif self.Searchlbl1.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    '1','2','3','4','5','6','7','8','9','0'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
                self.Searchlbl1.delete(0,END)


                
            elif self.Searchlbl1.get()[0] in (' ','<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    '1','2','3','4','5','6','7','8','9','0'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
                self.Searchlbl1.delete(0,END)

                
            
            elif self.Searchlbl1.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    '1','2','3','4','5','6','7','8','9','0'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Name. !!!")
                self.Searchlbl1.delete(0,END)
            else:
                conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
                cur=conn.cursor()
                cur.execute(f"select * from student_management_system where {str(self.SearchBy.get())} LIKE '%{str(self.S_E.get())}%'")
                if not cur.fetchall():
                    messagebox.showerror("Empty","No Data Found")
                else:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
                    cur=conn.cursor()
                    cur.execute(f"select * from student_management_system where {str(self.SearchBy.get())} LIKE '%{str(self.S_E.get())}%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                        self.Student_Tb.delete(*self.Student_Tb.get_children())
                        for row in rows:
                            self.Student_Tb.insert('',END,values=row)
                            conn.commit()
                    conn.close()
                
        elif self.ComboSearch.get()=="Contact":
            if self.Searchlbl1.get()=="":
                messagebox.showerror("Empty","Feild Are required!!!")

            elif self.Searchlbl1.get()[::1] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                    'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Contact. !!!")
                self.Searchlbl1.delete(0,END)

            elif self.Searchlbl1.get()[0] in (' ','<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                    'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Contact. !!!")
                self.Searchlbl1.delete(0,END)

                
            
            elif self.Searchlbl1.get()[-1::] in ('<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"',
                                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                                    'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
                #'<','>',',','.',';',':','/','?','{','}','[',']','|','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=',"'",'"'
                #'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                #'A','B','C','D','E','F','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
                
                messagebox.showerror("Wrong Value","Please Type Valid Contact. !!!")
                self.Searchlbl1.delete(0,END)
            else:
                conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
                cur=conn.cursor()
                cur.execute(f"select * from student_management_system where {str(self.SearchBy.get())} LIKE '%{str(self.S_E.get())}%'")
                if not cur.fetchall():
                    messagebox.showerror("Empty","No Data Found")
                else:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="codewithmobile")
                    cur=conn.cursor()
                    cur.execute(f"select * from student_management_system where {str(self.SearchBy.get())} LIKE '%{str(self.S_E.get())}%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                        self.Student_Tb.delete(*self.Student_Tb.get_children())
                        for row in rows:
                            self.Student_Tb.insert('',END,values=row)
                            conn.commit()
                    conn.close()





    def bli(self):
        self.Col=self.Normal
        self.Normal=self.green
        self.green=self.yellow
        self.yellow=self.Col
        self.Welcome.config(fg=self.Col)
        self.Welcome.after(200,self.bli)

    
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
root=Tk()
ob=Student(root)
root.mainloop()


#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#--------------------------------------------------------The End-------------------------------------------------------------------
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================