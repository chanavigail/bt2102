import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from turtle import color, width
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import lib.reportsOptions as reportsOptions
import lib.sql_database as sql_db

class BookSearchPage(tk.Frame):
    def __init__(self, master, ):
        ttk.Frame.__init__(self, master)
        master.title("Book Search Page")
        master.geometry("1366x768")
        database = sql_db.Database()

        def table_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Search Results")
            pop.geometry("1200x600")
            pop.geometry("+80+150")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Book Search Results", font='Helvetica 18 bold', bg="light green")
            msgLabel.place(x=500, y=10)

            table = search_table(pop)
            table.place(x=50, y=40)

            backButton = tk.Button(pop, text="Back to \nSearch Function", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=550, y= 500)
        
        def search_table(win):
            table = ttk.Treeview(win, height=20)

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

            results = database.getBookSearch(titleEntry.get(), authorsEntry.get(), ISBNEntry.get(), publisherEntry.get(), publishYearEntry.get())

            for i in range(0, len(results)):
                table.insert(parent='', index=i, iid=i, text='', values=results[i])

            return table
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text = "Search based on one of the categories below:", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        titleEntry = tk.Entry(master, textvariable = "Book Name", width = 60)
        titleLabel = tk.Label(master, text = "Title", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        titleLabel.place(x=320, y=180)
        titleEntry.place(x=470, y=185)
        titleEntry.delete(0, END)

        authorsLabel = tk.Label(master, text = "Authors", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        authorsEntry = tk.Entry(master, textvariable = "There can be multiple authors for a book", width = 60)
        authorsLabel.place(x=320, y=230)
        authorsEntry.place(x=470, y=235)
        authorsEntry.delete(0, END)

        ISBNLabel = tk.Label(master, text = "ISBN", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        ISBNEntry = tk.Entry(master, textvariable = "ISBN Number", width = 60)
        ISBNLabel.place(x=320, y=280)
        ISBNEntry.place(x=470, y=285)
        ISBNEntry.delete(0, END)

        publisherLabel = tk.Label(master, text = "Publisher", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        publisherEntry = tk.Entry(master, textvariable = "Random House, Penguin, Cengage, Springer, etc.", width = 60)
        publisherLabel.place(x=320, y=330)
        publisherEntry.place(x=470, y=335)
        publisherEntry.delete(0, END)

        publishYearLabel = tk.Label(master, text = "Publication Year", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        publishYearEntry = tk.Entry(master, textvariable = "Edition year", width = 60)
        publishYearLabel.place(x=320, y=380)
        publishYearEntry.place(x=470, y=385)
        publishYearEntry.delete(0, END)

        searchButton = tk.Button(master, text = "Search Book", height = 3, width = 15, padx = 5, command=table_popup)
        searchButton.place(x=470, y=440)

        backButton = tk.Button(master, text = "Back to Reports Menu", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(reportsOptions.ReportsOptionsPage))
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    BookSearch = BookSearchPage()
    BookSearch.mainloop()
