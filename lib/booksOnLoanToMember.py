import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import lib.reportsOptions as reportsOptions
import lib.sql_database as sql_db
import re


class BooksOnLoanToMemberPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Book Withdrawal")
        master.geometry("1366x768")
        database = sql_db.Database()

        def checkFirst():
            # variables
            regexID = r'^[a-zA-Z][0-9]+[a-zA-Z]$'
            memberID = membershipIDEntry.get()

            # Check empty fields
            if(len(memberID) < 1):
                return fail_popup("empty")

            # Check member id format
            if(not re.fullmatch(regexID, memberID) or len(memberID) > 6):
                return fail_popup("IDformat")

            # Check member exists
            checkMem = database.checkMemberExist(memberID)
            if(checkMem < 1):
                return fail_popup("IDexist")
            
            return table_popup()
            
        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Book Loan Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="red")

            errorLabel = tk.Label(pop, text="Error!", bg="red", fg="yellow")
            errorLabel.place(x=130, y=70)

            if (reason == "empty"):
                statusLabel = tk.Label(pop, text="Missing or \nIncomplete fields!", bg="red", fg="yellow")
                statusLabel.place(x=90, y=150)
            elif (reason == "IDformat"):
                statusLabel = tk.Label(pop, text="Member ID format incorrect!\nPlease follow this format:\nA101A (6 characters and below).", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)
            elif (reason == "IDexist"):
                statusLabel = tk.Label(pop, text="Member already exists!", bg="red", fg="yellow")
                statusLabel.place(x=70, y=150)
            
            backButton = tk.Button(pop, text="Back to \nSearch Function", bg="red", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        def table_popup():
            pop = tk.Toplevel(master)
            pop.title("Books on Loan to Member Report")
            pop.geometry("1200x600")
            pop.geometry("+80+150")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Books on Loan to Member", font='Helvetica 18 bold', bg="light green")
            msgLabel.place(x=500, y=10)

            backButton = tk.Button(pop, text="Back to \nReports Menu", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=550, y= 500)

            table = search_table(pop)
            table.place(x=50, y=40)

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

            results = database.getBookOnLoanToMember(membershipIDEntry.get())      
            for i in range(0, len(results)):
                table.insert(parent='', index=i, iid=i, text='', values=results[i])

            return table

        # image = Image.open("static/librarybg.png")
        self.bg = tk.PhotoImage(file="static/librarybg.png")

        # Labels
        backgroundLabel = tk.Label(master, image = self.bg)
        topLabel = tk.Label(master, text = "Books on Loan to Member", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        membershipIDLabel = tk.Label(master, text = "Membership ID", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")

        # Entry
        membershipIDEntry = tk.Entry(master, textvariable = "A unique alphanumeric id that distinguishes every member", width = 60)

        # Buttons
        searchButton = tk.Button(master, text = "Search Member\n", height = 3, width = 15, padx = 5, command=checkFirst)
        backButton = tk.Button(master, text = "Back to \nReports Menu", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(reportsOptions.ReportsOptionsPage))

        # Place
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)
        topLabel.place(x=140, y=70)

        membershipIDLabel.place(x=320, y=350)
        membershipIDEntry.place(x=470, y=355)
        membershipIDEntry.delete(0, END)

        searchButton.place(x=470, y=440)
        backButton.place(x=750, y=440)



if __name__ == "__main__":
    BooksOnLoanToMember = BooksOnLoanToMemberPage()
    BooksOnLoanToMember.mainloop()
