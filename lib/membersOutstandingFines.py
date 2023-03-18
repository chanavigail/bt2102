import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.reportsOptions as reportsOptions
import lib.sql_database as sql_db

class MembersOutstandingFinesPage(tk.Frame):
    def __init__(self, master, ):
        ttk.Frame.__init__(self, master)
        master.title("Outstanding Fines Page")
        master.geometry("1366x768")
        database = sql_db.Database()

        # Generic function for two functions in one button

        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func

        def table_popup():
            pop = tk.Toplevel(master)
            pop.title("Outstanding Fines Report")
            pop.geometry("1200x600")
            pop.geometry("+80+150")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Members with Outstanding Fines Report", font='Helvetica 18 bold', bg="light green")
            msgLabel.place(x=450, y=10)
        
            table = fines_table(pop)
            table.place(x=100, y=40)

            backButton = tk.Button(pop, text="Back to \nReports Menu", bg="light green", width=12, command=combine_funcs(pop.destroy, lambda:master.frameSwitcher(reportsOptions.ReportsOptionsPage)))
            backButton.place(x=550, y= 500)
        
        def fines_table(win):
            table = ttk.Treeview(win, height = 20)

            table['columns'] = ('member id', 'name', 'faculty', 'phone', 'email', 'fine')
            table.column("#0", width=0, stretch=tk.NO)
            table.column("member id", anchor=tk.CENTER, width=150)
            table.column("name", anchor=tk.CENTER, width=200)
            table.column("faculty", anchor=tk.CENTER, width=200)
            table.column("phone", anchor=tk.CENTER, width=150)
            table.column("email", anchor=tk.CENTER, width=200)
            table.column("fine", anchor=tk.CENTER, width=100)

            table.heading("#0", text="", anchor=tk.CENTER)
            table.heading("member id", text="Membership ID", anchor=tk.CENTER)
            table.heading("name", text="Name", anchor=tk.CENTER)
            table.heading("faculty", text="Faculty", anchor=tk.CENTER)
            table.heading("phone", text="Phone No.", anchor=tk.CENTER)
            table.heading("email", text="Email Address", anchor=tk.CENTER)
            table.heading("fine", text="Fine Amount", anchor=tk.CENTER)

            results = database.getAllFines()
            for i in range(0, len(results)):
                table.insert(parent='', index=i, iid=i, text='', values=results[i])

            return table
        
        # image = Image.open("static/librarybg.png")
        self.bg = tk.PhotoImage(file="static/librarybg.png")

        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        table_popup()


if __name__ == "__main__":
    MembersOutstandingFines = MembersOutstandingFinesPage()
    MembersOutstandingFines.mainloop()
