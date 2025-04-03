Criminal.py
from tkinter import *
from tkinter import Tk, ttk

import data
from PIL import Image, ImageTk
import mysql.connector

from tkinter import messagebox

class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL INVESTIGATION WITH SUSPECT PREDICTION')


        # Variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthmark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()

        lbl_title=Label(self.root,text='CRIMINAL INVESTIGATION WITH SUSPECT PREDICTION',font=('times new roman',35,'bold'),bg='black',fg='gold')
        lbl_title.place(x=20,y=0,width=1530,height=70)

        # logo
        img_logo=Image.open('images/6.jpeg')
        img_logo=img_logo.resize((60,60))
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=70,y=5,width=40,height=60)

        # Image_Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        img1=Image.open('images/7.jpeg')
        img1=img1.resize((540,160))
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        # img2
        img_2=Image.open('images/1.jpeg')
        img_2=img_2.resize((540,160))
        self.photo2 = ImageTk.PhotoImage(img_2)

        self.img_2 = Label(img_frame,image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)

        #img3
        img_3 = Image.open('images/5.jpeg')
        img_3 = img_3.resize((540, 160))
        self.photo3 = ImageTk.PhotoImage(img_3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1080, y=0, width=540, height=160)

        # Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=200,width=1500,height=560)

        # Upper Frame
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text='Criminal Information',font=('times new roman',10,'bold'),fg='red', bg='white')
        upper_frame.place(x=15, y=10, width=1470, height=270)

        # Label Entry

        # Case id
        caseid=Label(upper_frame, text='Case ID:',font=('arial', 12, 'bold'), bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial', 11, 'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        # Criminal N0
        lbl_criminal_no=Label(upper_frame,font=("arial", 12, "bold"),text="Criminal No:",bg="white")
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_criminal_no=ttk.Entry(upper_frame, textvariable=self.var_criminal_no,width=22, font=("arial", 11, "bold"))
        txt_criminal_no.grid(row=0, column=3, padx=2, pady=7)

        # Criminal Name
        lbl_name = Label(upper_frame, font=("arial", 12, "bold"), text=" Criminal Name:", bg="white")
        lbl_name.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name,width=22, font=("arial", 11, "bold"))
        txt_name.grid(row=1, column=1,sticky=W, padx=2, pady=7)

        # NickName
        lbl_nickname = Label(upper_frame, font=("arial", 12, "bold"), text=" NickName:", bg="white")
        lbl_nickname.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_nickname = ttk.Entry(upper_frame,textvariable=self.var_nickname, width=22, font=("arial", 11, "bold"))
        txt_nickname.grid(row=1, column=3, sticky=W, padx=2, pady=7)


        # Arrest Date
        lbl_arrestdate = Label(upper_frame, font=("arial", 12, "bold"), text=" Arrest Date:", bg="white")
        lbl_arrestdate.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(upper_frame,textvariable=self.var_arrest_date, width=22, font=("arial", 11, "bold"))
        txt_name.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # Date of Crime
        lbl_dateofcrime = Label(upper_frame, font=("arial", 12, "bold"), text=" Date of crime:", bg="white")
        lbl_dateofcrime.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_dateofcrime = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width=22, font=("arial", 11, "bold"))
        txt_dateofcrime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # address
        lbl_address = Label(upper_frame, font=("arial", 12, "bold"), text=" Address:", bg="white")
        lbl_address.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        # Age
        lbl_age = Label(upper_frame, font=("arial", 12, "bold"), text="Age:", bg="white")
        lbl_age.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_age = ttk.Entry(upper_frame, textvariable=self.var_age,width=22, font=("arial", 11, "bold"))
        txt_age.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        # Occupation
        lbl_occupation = Label(upper_frame, font=("arial", 12, "bold"), text=" Occupation:", bg="white")
        lbl_occupation.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_occupation = ttk.Entry(upper_frame,textvariable=self.var_occupation, width=22, font=("arial", 11, "bold"))
        txt_occupation.grid(row=4, column=1, sticky=W, padx=2, pady=7)

        #Birthmark
        lbl_birthmark = Label(upper_frame, font=("arial", 12, "bold"), text=" Birthmark:", bg="white")
        lbl_birthmark.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_birthmark = ttk.Entry(upper_frame,textvariable=self.var_birthmark, width=22, font=("arial", 11, "bold"))
        txt_birthmark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        #Crime Type
        lbl_crimetype = Label(upper_frame, font=("arial", 12, "bold"), text=" Crime Type:", bg="white")
        lbl_crimetype.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_crimetype = ttk.Entry(upper_frame,textvariable=self.var_crime_type, width=22, font=("arial", 11, "bold"))
        txt_crimetype.grid(row=0, column=5, sticky=W, padx=2, pady=7)

        # Father Name
        lbl_fathername = Label(upper_frame, font=("arial", 12, "bold"), text=" Father Name:", bg="white")
        lbl_fathername.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_fathername = ttk.Entry(upper_frame,textvariable=self.var_father_name, width=22, font=("arial", 11, "bold"))
        txt_fathername.grid(row=1, column=5, sticky=W, padx=2, pady=7)

        # gender
        lbl_gender = Label(upper_frame, font=("arial", 12, "bold"), text=" Gender:", bg="white")
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        # wanted
        lbl_wanted = Label(upper_frame, font=("arial", 12, "bold"), text=" Wanted:", bg="white")
        lbl_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        # Radio Button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
        radio_frame_gender.place(x=740,y=80,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=("arial", 8, "bold"),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        female = Radiobutton(radio_frame_gender,variable=self.var_gender, text='female', value='female', font=("arial", 8, "bold"), bg='white')
        female.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Radio Button wanted
        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        radio_frame_wanted.place(x=740, y=120, width=190, height=30)

        yes = Radiobutton(radio_frame_wanted, variable=self.var_wanted,text='Yes', value='yes', font=("arial", 8, "bold"), bg='white')
        yes.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        no = Radiobutton(radio_frame_wanted, variable=self.var_wanted ,text='No', value='no', font=("arial", 8, "bold"), bg='white')
        no.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Buttons
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=5, y=200, width=620, height=45)

        # add button
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=("arial", 12, "bold"),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        # update button
        btn_update = Button(button_frame,command=self.update_data, text='Update', font=("arial", 12, "bold"), width=14, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=3, pady=5)

        # delete button
        btn_delete = Button(button_frame,command=self.delete_data, text='Delete', font=("arial", 12, "bold"), width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        # clear button
        btn_clear = Button(button_frame,command=self.clear_data, text='Clear', font=("arial", 12, "bold"), width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=3, pady=5)

        # background right side image
        img4 = Image.open('images/4.jpeg')
        img4 = img4.resize((470, 245))
        self.photo4 = ImageTk.PhotoImage(img4)

        self.img_4 = Label(upper_frame, image=self.photo4)
        self.img_4.place(x=1000, y=0, width=470, height=245)

        # Down Frame
        down_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text='Criminal Information Data',
        font=('times new roman', 10, 'bold'), fg='red', bg='white')
        down_frame.place(x=15, y=280, width=1470, height=270)

        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text='Search Criminal Record',
        font=('times new roman', 10, 'bold'), fg='red', bg='white')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by= Label(search_frame, font=("arial", 12, "bold"), text=" Search By:", bg="red",fg='white')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame, textvariable=self.var_com_search, font=("arial", 12, "bold"), width=18, state='readonly')
        combo_search_box['value']=('Select Option','case_id','Criminal_no','Crime_Type')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W ,padx=5)

        self.var_search=StringVar()
        search_txt= ttk.Entry(search_frame,textvariable=self.var_com_search, width=18, font=("arial", 11, "bold"))
        search_txt.grid(row=0, column=2, sticky=W, padx=5)

        # search button
        btn_search = Button(search_frame, text='Search', font=("arial", 12, "bold"), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=3, pady=5)

        # all button
        btn_all = Button(search_frame, text='Show All', font=("arial", 12, "bold"), width=14, bg='blue', fg='white')
        btn_all.grid(row=0, column=4, padx=3, pady=5)

        crimeagency = Label(search_frame, font=("arial", 30, "bold"), text=" NATIONAL CRIME AGENCY", bg="white",fg='crimson')
        crimeagency.grid(row=0, column=5, sticky=W, padx=50 )

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)



        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,columns=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='Case id')
        self.criminal_table.heading('2', text='Crime No')
        self.criminal_table.heading('3', text='Criminal Name')
        self.criminal_table.heading('4', text='NickName')
        self.criminal_table.heading('5', text='Arrest Date')
        self.criminal_table.heading('6', text='Date of Crime')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name ')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2', width=100)
        self.criminal_table.column('3', width=100)
        self.criminal_table.column('4', width=100)
        self.criminal_table.column('5', width=100)
        self.criminal_table.column('6', width=100)
        self.criminal_table.column('7', width=100)
        self.criminal_table.column('8', width=100)
        self.criminal_table.column('9', width=100)
        self.criminal_table.column('10', width=100)
        self.criminal_table.column('11', width=100)
        self.criminal_table.column('12', width=100)
        self.criminal_table.column('13', width=100)
        self.criminal_table.column('14', width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    # Add function

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Kishan@1703',database='crime')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                         self.var_case_id.get(),
                                                                                                         self.var_criminal_no.get(),
                                                                                                         self.var_name.get(),
                                                                                                         self.var_nickname.get(),
                                                                                                         self.var_arrest_date.get(),
                                                                                                         self.var_date_of_crime.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_age.get(),
                                                                                                         self.var_occupation.get(),
                                                                                                         self.var_birthmark.get(),
                                                                                                         self.var_crime_type.get(),
                                                                                                         self.var_father_name.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_wanted.get(),

                                                                                                         ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has bee added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Kishan@1703', database='crime')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()

    # get cursor

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    # update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you Sure! You want to Update this record')
                if update>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Kishan@1703', database='crime')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateofcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(
                                                                                                                                                                                                                                                                     self.var_criminal_no.get(),
                                                                                                                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                                                                                                                     self.var_nickname.get(),
                                                                                                                                                                                                                                                                     self.var_arrest_date.get(),
                                                                                                                                                                                                                                                                     self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                                                                                                     self.var_age.get(),
                                                                                                                                                                                                                                                                     self.var_occupation.get(),
                                                                                                                                                                                                                                                                     self.var_birthmark.get(),
                                                                                                                                                                                                                                                                     self.var_crime_type.get(),
                                                                                                                                                                                                                                                                     self.var_father_name.get(),
                                                                                                                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                                                                                                                     self.var_wanted.get(),
                                                                                                                                                                                                                                                                     self.var_case_id.get(),


                                                                                                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal records updated successfully')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Are you Sure! You want to Delete this record')
                if delete >0:
                   conn = mysql.connector.connect(host='localhost', username='root', password='Kishan@1703', database='crime')
                   my_cursor = conn.cursor()
                   sql='delete from criminal where Case_id=%s'
                   value=(self.var_case_id.get(),)
                   my_cursor.execute(sql,value)
                else:
                     if not delete:
                         return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo('Success','Criminal record Deleted successfully')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    # search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Kishan@1703',
                                               database='crime')
                my_cursor = conn.cursor()
                my_cursor=conn.cursor('select * from criminal where' +str(self.var_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("",END,values=i)
                    conn.commit()
                    conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To {str(es)}')

if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()

