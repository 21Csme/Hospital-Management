from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def login():
    username=entry1.get()
    password=entry2.get()

    if(username=="" and password==""):
        messagebox.showinfo("","Blank not allowed")
    elif(username=="Himanshu" and password=="User123"):
        root.destroy()
        win=Tk()
        win.state('zoomed')
        win.config(bg='black')
        def delete():
             co=mysql.connector.connect(host='localhost',username='root',password='Himanshu@123',database='himadb')
             my_cursor=co.cursor()
             querry=("delete from hospital where Refrence=%s")
             value=(RF.get(),)
             my_cursor.execute(querry,value)
             co.commit()
             co.close()
             fetch_data()
             messagebox.showinfo('Deleted','Deletion is successful')
            
        def sav():
            if e1.get()=="":
                messagebox.showerror("Error","All fields are requireds")
            else:
                co=mysql.connector.connect(host='localhost',username='root',password='Himanshu@123',database='himadb')
                my_cursor=co.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    RF.get(),
                    PN.get(),
                    PG.get(),
                    PA.get(),
                    PMO.get(),
                    PAD.get(),
                    PD.get(),
                    PAT.get(),
                    DF.get(),
                    PBP.get(),
                    PS.get(),
                ))
                co.commit()
                fetch_data()
                co.close()
                messagebox.showinfo("Success","Record has been inserted")
        def fetch_data():
            co=mysql.connector.connect(host='localhost',username='root',password='Himanshu@123',database='himadb')
            my_cursor=co.cursor()
            my_cursor.execute('select * from hospital')
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                table.delete(* table.get_children())
                for items in rows:
                    table.insert('',END,values=items)
                co.commit()
            co.close()
        def get_data(event=''):
            cursor_row=table.focus()
            data=table.item(cursor_row)
            row=data['values']
            RF.set(row[0])
            PN.set(row[1])
            PG.set(row[2])
            PA.set(row[3])
            PMO.set(row[4])
            PAD.set(row[5])
            PD.set(row[6])
            PAT.set(row[7])
            DF.set(row[8])
            PBP.set(row[9])
            PS.set(row[10])
            
        def cle():
            RF.set('')
            PN.set('')
            PG.set('')
            PA.set('')
            PMO.set('')
            PAD.set('')
            PD.set('')
            PAT.set('')
            DF.set('')
            PBP.set('')
            PS.set('')
            dataen.delete(1.0,END)
            
            
        def pre():
             dataen.insert(END, 'Refrence:\t\t\t'+PN.get()+'\n')
             dataen.insert(END, 'Patient Name:\t\t\t'+PN.get()+'\n')
             dataen.insert(END, 'Gender:\t\t\t'+PG.get()+'\n')
             dataen.insert(END, 'Patient Age:\t\t\t'+PA.get()+'\n')
             dataen.insert(END, 'Patient Mobile No:\t\t\t'+PMO.get()+'\n')
             dataen.insert(END, 'Patient Address:\t\t\t'+PAD.get()+'\n')
             dataen.insert(END, 'Patient Doctor:\t\t\t'+PD.get()+'\n')
             dataen.insert(END, 'Patient Appointment:\t\t\t'+PAT.get()+'\n')
             dataen.insert(END, 'Patient Fees:\t\t\t'+DF.get()+'\n')
             dataen.insert(END, 'Patient B.P:\t\t\t'+PBP.get()+'\n')
             dataen.insert(END, 'Patient Status:\t\t\t'+PS.get()+'\n')
        def pdf():
            pass
        def pro():
            win.destroy()
        #heading
        Label(win,text='Hospital Management System',font='impack 31 bold',bg='blue',fg='white').pack(fill=X)
         #frame1
        frame1=Frame(win,bd=16,relief=RIDGE)
        frame1.place(x=0,y=60,width=1530,height=390)
         #label1
        lf1=LabelFrame(frame1,text='Patient Information',font='ariel 15 bold',bd=10,bg='grey')
        lf1.place(x=10,y=0,width=900,height=340)
         #label2
        lf2=LabelFrame(frame1,text='Presciption',font='ariel 15 bold',bd=10,bg='grey')
        lf2.place(x=915,y=0,width=580,height=340)
         #labels for Patient information
        Label(lf1,text='Refrence No:',font='ariel 10 bold',fg='black',bg='grey').place(x=5,y=10)
        Label(lf1,text='Patient Name:',font='ariel 10 bold',fg='black',bg='grey').place(x=5,y=60)
        Label(lf1,text='Patient Gender:',font='ariel 10 bold',fg='black',bg='grey').place(x=5,y=110)
        Label(lf1,text='Patient Age:',font='ariel 10 bold',fg='black',bg='grey').place(x=5,y=160)
        Label(lf1,text='Patient Mobile No:',font='ariel 10 bold',fg='black',bg='grey').place(x=5,y=210)
        Label(lf1,text='Patient Address:',font='ariel 10 bold',fg='black',bg='grey').place(x=5,y=260)
        Label(lf1,text='Patient Doctor:',font='ariel 10 bold',fg='black',bg='grey').place(x=450,y=10)
        Label(lf1,text='Patient Appointment time:',font='ariel 10 bold',fg='black',bg='grey').place(x=450,y=60)
        Label(lf1,text='Doctor Fees:',font='ariel 10 bold',fg='black',bg='grey').place(x=450,y=110)
        Label(lf1,text='Patient B.P:',font='ariel 10 bold',fg='black',bg='grey').place(x=450,y=160)
        Label(lf1,text='Patient Status:',font='ariel 10 bold',fg='black',bg='grey').place(x=450,y=210)
        #Text Variable
        RF=StringVar()
        PN=StringVar()
        PG=StringVar()
        PA=StringVar()
        PMO=StringVar()
        PAD=StringVar()
        PD=StringVar()
        PAT=StringVar()
        DF=StringVar()
        PBP=StringVar()
        PS=StringVar()
        #fillboxes for entries
        e1=Entry(lf1,bd=4,textvariable=RF)
        e1.place(x=190,y=10,width=180)
        e1=Entry(lf1,bd=4,textvariable=PN)
        e1.place(x=190,y=60,width=180)
        e1=Entry(lf1,bd=4,textvariable=PG)
        e1.place(x=190,y=110,width=180)
        e1=Entry(lf1,bd=4,textvariable=PA)
        e1.place(x=190,y=160,width=180)
        e1=Entry(lf1,bd=4,textvariable=PMO)
        e1.place(x=190,y=210,width=180)
        e1=Entry(lf1,bd=4,textvariable=PAD)
        e1.place(x=190,y=260,width=180)
        e1=Entry(lf1,bd=4,textvariable=PD)
        e1.place(x=640,y=10,width=180)
        e1=Entry(lf1,bd=4,textvariable=PAT)
        e1.place(x=640,y=60,width=180)
        e1=Entry(lf1,bd=4,textvariable=DF)
        e1.place(x=640,y=110,width=180)
        e1=Entry(lf1,bd=4,textvariable=PBP)
        e1.place(x=640,y=160,width=180)
        e1=Entry(lf1,bd=4,textvariable=PS)
        e1.place(x=640,y=210,width=180)
        #entrydata for prescption
        dataen=Text(lf2,font='ariel 10 bold',width=580,height=340,bg='grey',fg='black')
        dataen.pack(fill=BOTH)

          #frame 2
        frame2=Frame(win,bd=15,relief=RIDGE)
        frame2.place(x=0,y=456,width=1530,height=250) 

        #button 1
        d_button=Button(win,text='Delete',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=delete)
        d_button.place(x=25,y=715,width=240)
        s_button=Button(win,text='Save',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=sav)
        s_button.place(x=266,y=715,width=240)
        pdf=Button(win,text='PDF',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=pdf)
        pdf.place(x=507,y=715,width=240)
        e_button=Button(win,text='Clear',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=cle)
        e_button.place(x=750,y=715,width=240)
        f_button=Button(win,text='Presciption',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=pre)
        f_button.place(x=990,y=715,width=240)
        f_button=Button(win,text='Exit',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=pro)
        f_button.place(x=1230,y=715,width=240)
        scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
        scroll_x.pack(side='bottom',fill='x')
        scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
        scroll_y.pack(side='right',fill='y')
        table=ttk.Treeview(frame2,columns=('RF','PN','PG','PA','PMO','PAD','PD','PAT','DF','PBP','PS'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x=ttk.Scrollbar(command=table.xview)
        scroll_y=ttk.Scrollbar(command=table.yview)
        #heading for Data
        table.heading('RF',text='Refrence')
        table.heading('PN',text='Patient Name')
        table.heading('PG',text='Patient Gender')
        table.heading('PA',text='Patient Address')
        table.heading('PMO',text='Patient Mobile No')
        table.heading('PAD',text='Patient Patient Address')
        table.heading('PD',text='Patient Doctor')
        table.heading('PAT',text='Patient Appointment Time')
        table.heading('DF',text='Doctor Fees ')
        table.heading('PBP',text='Patient B.P')
        table.heading('PS',text='Patient Status')
        table['show']='headings'
        table.pack(fill=BOTH,expand=1)
        #fjhhjklkshghhj
        table.column('RF',width=100)
        table.column('PN',width=100)
        table.column('PG',width=100)
        table.column('PA',width=100)
        table.column('PMO',width=100)
        table.column('PAD',width=100)
        table.column('PD',width=100)
        table.column('PAT',width=100)
        table.column('DF',width=100)
        table.column('PBP',width=100)
        table.column('PS',width=100)
        fetch_data()
        table.bind('<ButtonRelease-1>',get_data)
        
        scroll_x=ttk.Scrollbar(command=table.xview)
        scroll_y=ttk.Scrollbar(command=table.yview)
        

        mainloop()
        
    else:
        messagebox.showinfo("","incorrect username or password")

#first page
        
def fd():
    messagebox.showinfo("","see your id card")
root=Tk()
root.title("Hospital Management System Login")
root.geometry("1100x733+170+70")
root.configure(bg="white")
root.resizable(False,False)

img=PhotoImage(file="C:\\Users\\himanshu sachan\\Pictures\\pexels-roman-ska-10874293.png")
Label(root,image=img,bg="white").place(x=0,y=0)

global entry1
global entry2
LabelFrame(root,bg='white').place(x=100,y=300,width=450,height=340)
Label(root,text='Sign in',font='ariel 35 bold',bg='white',fg='#2f4f4f').place(x=260,y=330)
Label(root,text="Username:",font='ariel 23 bold',bg='white',fg='#2f4f4f').place(x=150,y=400)
Label(root,text="Password:",font='ariel 23 bold',bg='white',fg='#2f4f4f').place(x=150,y=460)
entry1=Entry(root,bd=2,width=31,)
entry1.place(x=320,y=410)
entry2=Entry(root,bd=2,width=31)
entry2.place(x=320,y=470)

Button(root,text="Login",command=login,font='ariel 14 bold',width=28,bg='#DC143C',fg='white').place(x=160,y=520)
Button(root,text="* Forgot Password",font='ariell 14 bold',width=20,bg='white',fg='red',bd=0,command=fd).place(x=140,y=570)
root.mainloop()


