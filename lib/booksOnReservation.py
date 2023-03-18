import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.reportsOptions as reportsOptions
import lib.sql_database as sql_db

class BooksOnReservationPage(tk.Frame):
    def __init__(self, master, ):
        ttk.Frame.__init__(self, master)
        master.title("Books On Reservation Page")
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
            pop.title("Books on Reservation Report")
            pop.geometry("900x600")
            pop.geometry("+230+150")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Books on Reservation Report", font='Helvetica 18 bold', bg="light green")
            msgLabel.place(x=330, y=10)

            table = reservations_table(pop)
            table.place(x=80, y=40)

            backButton = tk.Button(pop, text="Back to \nReports Menu", bg="light green", width=12, command=combine_funcs(pop.destroy, lambda:master.frameSwitcher(reportsOptions.ReportsOptionsPage)))
            backButton.place(x=400, y= 500)
        
        def reservations_table(win):
            table = ttk.Treeview(win, height = 15)

            table['columns'] = ('Accession No.', 'Title', 'Membership ID', 'Name')
            table.column("#0", width=0, stretch=tk.NO)
            table.column("Accession No.", anchor=tk.CENTER, width=100)
            table.column("Title", anchor=tk.CENTER, width=300)
            table.column("Membership ID", anchor=tk.CENTER, width=150)
            table.column("Name", anchor=tk.CENTER, width=200)

            table.heading("#0", text="", anchor=tk.CENTER)
            table.heading("Accession No.", text="Accession No.", anchor=tk.CENTER)
            table.heading("Title", text="Title", anchor=tk.CENTER)
            table.heading("Membership ID", text="Membership ID", anchor=tk.CENTER)
            table.heading("Name", text="Name", anchor=tk.CENTER)

            results = database.getAllReservations()
            for i in range(0, len(results)):
                table.insert(parent='', index=i, iid=i, text='', values=results[i])

            return table


        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text = "Search based on one of the categories below:", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        table_popup()


if __name__ == "__main__":
    BooksOnReservation = BooksOnReservationPage()
    BooksOnReservation.mainloop()
