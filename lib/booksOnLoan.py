import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.reportsOptions as reportsOptions
import lib.sql_database as sql_db


class BooksOnLoanPage(tk.Frame):
    def __init__(self, master, ):
        ttk.Frame.__init__(self, master)
        master.title("Books On Loan Page")
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
            pop.title("Books on Loan Report")
            pop.geometry("1200x600")
            pop.geometry("+80+150")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Books on Loan Report", font='Helvetica 18 bold', bg="light green")
            msgLabel.place(x=500, y=10)

            backButton = tk.Button(pop, text="Back to \nReports Menu", bg="light green", width=12, command=combine_funcs(pop.destroy, lambda:master.frameSwitcher(reportsOptions.ReportsOptionsPage)))
            backButton.place(x=550, y= 500)

            table = search_table(pop)
            table.place(x=50, y=40)

        def search_table(win):
            table = ttk.Treeview(win, height = 15)

            table['columns'] = ('Accession No.', 'Title', 'Authors', 'ISBN', 'Publisher', 'Year')
            table.column("#0", width=0, stretch=tk.NO)
            table.column("Accession No.", anchor=tk.CENTER, width=100)
            table.column("Title", anchor=tk.CENTER, width=300)
            table.column("Authors", anchor=tk.CENTER, width=300)
            table.column("ISBN", anchor=tk.CENTER, width=150)
            table.column("Publisher", anchor=tk.CENTER, width=150)
            table.column("Year", anchor=tk.CENTER, width=100)

            table.heading("#0", text="", anchor=tk.CENTER)
            table.heading("Accession No.", text="Accession No.", anchor=tk.CENTER)
            table.heading("Title", text="Title", anchor=tk.CENTER)
            table.heading("Authors", text="Authors", anchor=tk.CENTER)
            table.heading("ISBN", text="ISBN", anchor=tk.CENTER)
            table.heading("Publisher", text="Publisher", anchor=tk.CENTER)
            table.heading("Year", text="Year", anchor=tk.CENTER)

            results = database.getBookOnLoan()      
            for i in range(0, len(results)):
                table.insert(parent='', index=i, iid=i, text='', values=results[i])

            return table
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        table_popup()


if __name__ == "__main__":
    BooksOnLoan = BooksOnLoanPage()
    BooksOnLoan.mainloop()
