from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import *
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector


wara = Tk ()
wara.title("lifechoises sign in")
wara.geometry("700x700")
wara.config(background="#EAB615")

# Time & Date
clock = tk.Label(wara, font="bold")
clock.place(x=20, y=20)

time = datetime.now()
clock.config(text=time.strftime('Date: ' + "%d/%m/%y\n" + 'Time: ' + "%H:%M:%S %p"), font='times 15', fg='black', bg='#ABC895')

def verify():
        pass




mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Lifechoices314",
    database="lifechoicesonline",
    auth_plugin="mysql_native_password"
)

my_cursor = mydb.cursor(buffered=True)

#INSERT FUNCTION
def insert():
    if "@" and ".com" not in email_entry.get():
        kal = tk.messagebox.showinfo(" INVALID DETAILS", "ENTER VALID EMAIL ADDRESS")
        email_entry.delete(0, END)
    else:
        msg = tk.messagebox.askyesno("Form filling confarmation",
                                          " WARNING: All data will be erase after 'YES' for new applicant")
        if msg > 0:
            NAME = name_entry.get()
            SUR = surname_entry.get()
            EMAIL = email_entry.get()
            COURSE = box.get()
            ID = ID_no.get()

            sql = 'INSERT INTO register (name,surname, email, courses, id ) VALUES(%s, %s, %s, %s, %s)'
            val = (NAME, SUR, EMAIL,COURSE, ID )
            my_cursor.execute(sql, val)
            mydb.commit()

        golu()


def golu():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    email_entry.delete(0, END)
    box.set("SELECT")
    ID_no.delete(0, END)


#DELETE Function
def delete():
    number = str(name_entry.get())
    sql_Delete_query = "DELETE FROM register WHERE name=%s"

    my_cursor.execute(sql_Delete_query, [number])

    messagebox.showinfo("ADMIN"," delete succesfully")
    name_entry.delete(0, END)

    mydb.commit()

def update():
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()
    courses = box.get()
    id = ID_no.get()

    sql = "Update register SET name=%s,surname =%s,email=%s,courses=%s where id =%s;"


    my_cursor.execute(sql, [(name), (email), (id), (courses), (surname)])

    mydb.commit()


def display():
    my_cursor.execute("Select * from register")
    for i in my_cursor:
        diplay_names.insert(END, i)


def clear_all():
    surname_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    ID_no.delete(0, END)
    diplay_names.delete(0, END)


heading_lbl = Label(wara, text="Students Registraton",font=("times new roman", 35), bg="yellow", fg="black")
heading_lbl.place(x=200, y=20)

diplay_names = Listbox(wara, bg="white", fg="black", width=60, selectbackground="white", selectforeground="black")
diplay_names.place(x=130, y=400)

name_lbl = Label(wara, text="NAME :")
name_lbl.place(x=20, y=100)

name_entry = Entry(wara)
name_entry.place(x=170, y=100)


surname_lbl = Label(wara, text="Enter Surname")
surname_lbl.place(x=20, y=150)

surname_entry = Entry(wara)
surname_entry.place(x=170, y=150)

email_lbl = Label(wara, text="Enter Email")
email_lbl.place(x=20, y=200)

email_entry = Entry(wara)
email_entry.place(x=170, y=200)

course_lbl = Label(wara, text="Enter Course")
course_lbl.place(x=20, y=250)

box = ttk.Combobox(wara, state="readonly", font=("arial", 12, "bold"), width=22)
box['values'] = ('SELECT', 'THERAPY', 'LIFE SKILLS', 'IT')
box.current(0)
box.place(x=170, y=250)

id_lbl = Label(wara, text="Enter ID_no")
id_lbl.place(x=20, y=300)

ID_no = Entry(wara)
ID_no.place(x=170, y=300)

insert_button = Button(wara,text="INSERT",bg="yellow",command=insert)
insert_button.place(x=80,y=350)

get_button = Button(wara, text="GET", bg="yellow", command=display)
get_button.place(x=170,y=350)

delete_button = Button(wara,text="DELETE",bg="yellow",command=delete)
delete_button.place(x=240,y=350)

update_button = Button(wara,text="UPDATE",bg="yellow",command=update)
update_button.place(x=330,y=350)

clear_button = Button(wara,text="Clear",bg="yellow",command=clear_all)
clear_button.place(x=10,y=350)



wara.mainloop()
