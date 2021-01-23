import tkinter as tk
import tkinter.ttk as ttk
from datetime import *


class Application(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x750')
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.root.title("Signin page")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="#EA8915")

        # Time & Date
        clock = tk.Label(self.root, font="bold")
        clock.grid(row=0, column=0)

        time = datetime.now()
        clock.config(text=time.strftime('Date: ' + "%d/%m/%y\n" + 'Time: ' + "%H:%M:%S %p"), font='times 15', fg='black', bg='yellow')

        self.heading = tk.Label(self.root, text='- IN & OUT FORM -',font=("times new roman", 35), bg="yellow", fg="black")
        self.heading.grid(row=0, column=1)

        # Define the different GUI widgets
        self.name_label = tk.Label(self.root, text="Name:",  font='arial 15 bold italic', fg='black', bg='yellow')
        self.name_label.grid(row=1, column=0)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, pady=10)

        self.purpose_label = tk.Label(self.root, text="Purpose", font='arial 15 bold italic', fg='black', bg='yellow')
        self.purpose_label.grid(row=2, column=0)

        self.box = ttk.Combobox(self.root, state="readonly", font=("arial", 12, "bold"), width=22)
        self.box['values'] = ('SELECT', 'THERAPY', 'LIFE SKILLS', 'IT', 'VISITOR')
        self.box.current(0)
        self.box.grid(row=2, column=1, pady=40)


        self.gen_lab = tk.Label(self.root, text="Gender", font=('arial 15 bold italic'), bg='yellow', fg='black')
        self.gen_lab.grid(row=3, column=0)

        com = ttk.Combobox(self.root, state="readonly")
        com['values'] = ('Male', "Female", "Other")
        com.grid(row=3, column=1, pady=20)

        self.insert_btn = tk.Button(self.root, text="Insert", width=15,bg="yellow",
                                    command=self.insert_data)
        self.insert_btn.grid(row=5, column=0)

        self.reg_btn = tk.Button(self.root, text="Register", width=15,bg="yellow",
                                    command=self.regi)
        self.reg_btn.grid(row=5, column=1)

        self.erase_btn = tk.Button(self.root, text="Delete", width=15,bg="yellow",
                                   command=self.delete_data)
        self.erase_btn.grid(row=5, column=2)

        self.exit_btn = tk.Button(self.root, text="Exit", width=15,bg="yellow",
                                  command=self.root.quit)
        self.exit_btn.grid(row=5, column=3, pady=40)

        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Name', 'Position', 'Status', 'Time','DAY'))

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Status')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='Course')
        self.tree.heading('#3', text='Time')
        self.tree.heading('#4', text='DAY')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)
        self.tree.column('#4', stretch=tk.YES)

        self.tree.grid(row=6, columnspan=5, rowspan=10)
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def regi(self):
        self.root.destroy()
        import register
        register.verify()


    def insert_data(self):
        day = datetime.now()
        time = day.strftime('%H:%M')
        self.treeview.insert('', 'end', iid=self.iid, text="Signed_In" + str(self.id),
                             values=(self.name_entry.get(),
                                     self.box.get(),time, day))
        self.iid = self.iid + 1
        self.id = self.id + 1


    def delete_data(self):
        row_id = int(self.tree.focus())
        self.treeview.delete(row_id)


app = Application(tk.Tk())
app.root.mainloop()
