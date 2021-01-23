import tkinter
import mysql.connector
from tkinter import *
from tkinter import messagebox


# function to open this module
def popup():
    pass


# GUI properties/styles
window = Tk()
window.geometry("540x500")
window.title('Lifechoices')
window.configure(background='#EA8F15')

mydb = mysql.connector.connect(user='root', password='@Lifechoices314', database='Lifechoicesonline',
                               host='127.0.0.1',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


def verify():
    user_verification = Username.get()
    pass_verification = Password.get()
    sql = "select * from admin where name = %s and password = %s"
    mycursor.execute(sql, [(user_verification), (pass_verification)])
    results = mycursor.fetchall()
    if results:
        for x in results:
            logged()
            break
    else:
        failed()


def logged():
    messagebox.showinfo(" WLCOME ", "Successfully Logged In")
    window.destroy()
    import table
    table.initialize_user_interface()


def failed():
    messagebox.showerror("Admin 0nly", 'UNKNOWN USER')
    Username.delete(0, END)
    Password.delete(0, END)


head = Label(window, text='Life Choices Online', font='times 12 bold ',
             fg='black',
             bg='yellow')
head.pack()

reg_frame = Frame(window)
reg_frame.pack(pady=30)

heading = Label(reg_frame, text='--LOGIN PAGE--',font=("times new roman", 35), bg="yellow", fg="black")

heading.pack(pady=10)

entry_log = Label(window, text="Enter Name:", font='arial 15 bold italic', fg='black', bg='yellow')
entry_log.pack(pady=10)

Username = Entry(width=25)
Username.pack(pady=15)

entry_log = Label(window, text="Enter Password:",font='arial 15 bold italic', fg='black', bg='yellow')
entry_log.pack(pady=10)

Password = Entry(width=20, show='*')
Password.pack(pady=10)

myButton = Button(window, text="lOGIN", width=15, bg='yellow', fg='black', command=verify)
myButton.pack(pady=11)

window.mainloop()
