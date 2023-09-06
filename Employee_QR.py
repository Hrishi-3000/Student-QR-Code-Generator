from tkinter import*
import qrcode
from PIL import Image,ImageTk
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x500+200+50")
        self.root.title("QR Generator | Developed by BAHI SAHAB")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="  Qr Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        
        #students detail project---
        #var
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        
        emp_title=Label(emp_Frame,text="Student Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        
        lbl_emp_code=Label(emp_Frame,text="Student ID",font=("Times new Roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(emp_Frame,text="Name",font=("Times new Roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_department=Label(emp_Frame,text="Department",font=("Times new Roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_designation=Label(emp_Frame,text="Phone No",font=("Times new Roman",15,'bold'),bg='white').place(x=20,y=180)
        
        txt_emp_code=Entry(emp_Frame,font=("Times new Roman",15,),textvariable=self.var_emp_code,bg='light yellow').place(x=200,y=60)
        txt_name=Entry(emp_Frame,font=("Times new Roman",15,),textvariable=self.var_name,bg='light yellow').place(x=200,y=100)
        txt_department=Entry(emp_Frame,font=("Times new Roman",15,),textvariable=self.var_department,bg='light yellow').place(x=200,y=140)
        txt_designation=Entry(emp_Frame,font=("Times new Roman",15,),textvariable=self.var_designation,bg='light yellow').place(x=200,y=180)
        
        btn_generate=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=282,y=250,width=120,height=30)
        
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("Times new Roman",20,),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)
        
          #sqr detail project---
        #qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        #qr_Frame.place(x=550,y=100,width=250,height=380)
        
        #emp_title=Label(qr_Frame,text="Student QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        
        #self.qr_code=Label(qr_Frame,text='No Qr\nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        #self.qr_code.place(x=35,y=100,width=180,height=180)
    
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
    def generate(self):
        if self.var_designation.get()=='' or self.var_emp_code.get()=='' or self.var_department.get()=='' or self.var_name.get()=='':
          self.msg='All Fields Are Requider!!'
          self.lbl_msg.config(text=self.msg,fg='red')
        else:
            #updaintg noti
            qr_data=(f"Student ID:{self.var_emp_code.get()}\nStudent Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nPhone No:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code.save("Employee_QR/Emp_"+str(self.var_emp_code.get())+'.png')
            #self.qr_code.config(image=self.im)
            #qr code image update
            #self.im=ImageTk.PhotoImage(qr_code)
            
            self.msg='QR Code Generated Succesfully!!'
            self.lbl_msg.config(text=self.msg,fg='green')
            
                
        
root=Tk()
obj =Qr_Generator(root)
root.mainloop()    