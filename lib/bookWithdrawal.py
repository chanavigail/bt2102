from tabnanny import check
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
from PIL import Image, ImageTk
from turtle import color, width
import lib.booksOptions as booksOptions
import lib.sql_database as sql_db
import re

class BookWithdrawalPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Book Withdrawal")
        master.geometry("1366x768")
        database = sql_db.Database()

        # Generic function for two functions in one button

        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func
        
        def withdrawBook():
            bookID = accessionNumberEntry.get()

            database.removeBookDetails(bookID)
            database.removeAuthors(bookID)
            return success_popup()

        def processAuthors(authorTuple):
            result = ""
            for i in range(len(authorTuple)):
                if (i == 0):
                    result += authorTuple[i][1]
                else:
                    result += ", "
                    result += authorTuple[i][1]
            return result

        def checkFirst():
            regexBookID = r'^[a-zA-Z][0-9]+$'
            bookID = accessionNumberEntry.get()

            # Check empty fields
            if(len(bookID) < 1):
                return fail_popup("empty")

            # Check book format
            if(not re.fullmatch(regexBookID, bookID)):
                return fail_popup("bookformat")

            # Check book exist
            checkBook = database.checkBookExist(bookID)
            if(checkBook < 1):
                return fail_popup("bookexist")
            
            # Check if book is on loan
            onLoan = database.checkLoanStatus(bookID)
            if(onLoan > 0):
                return fail_popup("loan")
            
            # Check if book is reserved
            reserved = database.checkReservedStatus(bookID)
            if(reserved > 0):
                return fail_popup("reserve")
            
            return confirm_popup()

        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Book Withdrawal Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="red")

            errorLabel = tk.Label(pop, text="Error!", bg="red", fg="yellow")
            errorLabel.place(x=130, y=70)

            if (reason == "empty"):
                statusLabel = tk.Label(pop, text="Missing or \nIncomplete fields!", bg="red", fg="yellow")
                statusLabel.place(x=90, y=150)
            elif (reason == "bookformat"):
                statusLabel = tk.Label(pop, text="Accession number format incorrect!\nPlease follow this format:\nA01", bg="red", fg="yellow")
                statusLabel.place(x=40, y=150)
            elif (reason == "bookexist"):
                statusLabel = tk.Label(pop, text="Book does not exist!", bg="red", fg="yellow")
                statusLabel.place(x=80, y=150)
            elif (reason == "loan"):
                statusLabel = tk.Label(pop, text="Book is currently on loan.", bg="red", fg="yellow")
                statusLabel.place(x=70, y=150)
            elif (reason == "reserve"):
                statusLabel = tk.Label(pop, text="Book is currently reserved.", bg="red", fg="yellow")
                statusLabel.place(x=60, y=150)

            backButton = tk.Button(pop, text="Back to \nWithdrawal\nFunction", bg="red", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        def confirm_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Withdrawal Details")
            pop.geometry("480x300")
            pop.geometry("+450+200")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Please Confirm Details to Be Correct", font='Helvetica 12 bold', bg="light green")
            msgLabel.place(x=140, y=10)

            bookID = accessionNumberEntry.get()
            title = database.getBookTitle(bookID)
            authors = processAuthors(database.getAuthors(bookID))
            isbn = database.getISBN(bookID)
            publisher = database.getPublisher(bookID)
            publication_year = database.getPublishYear(bookID)
            
            accessionNumberLabel = tk.Label(pop, text="Accession Number", bg="light green")
            accessionNumberLabel.place(x=50, y=50)
            accessionNumberDataLabel = tk.Label(pop, text=accessionNumberEntry.get(), bg="light green")
            accessionNumberDataLabel.place(x=170, y=50)

            TitleLabel = tk.Label(pop, text="Title", bg="light green")
            TitleLabel.place(x=50, y=80)
            TitleDataLabel = tk.Label(pop, text=title, bg="light green")
            TitleDataLabel.place(x=170, y=80)

            authorsLabel = tk.Label(pop, text="Authors", bg="light green")
            authorsLabel.place(x=50, y=110)
            authorsDataLabel = tk.Label(pop, text=authors, bg="light green")
            authorsDataLabel.place(x=170, y=110)

            isbnLabel = tk.Label(pop, text="ISBN", bg="light green")
            isbnLabel.place(x=50, y=140)
            isbnDataLabel = tk.Label(pop, text=isbn, bg="light green")
            isbnDataLabel.place(x=170, y=140)

            publisherLabel = tk.Label(pop, text="Publisher", bg="light green")
            publisherLabel.place(x=50, y=170)
            publisherDataLabel = tk.Label(pop, text=publisher, bg="light green")
            publisherDataLabel.place(x=170, y=170)

            yearLabel = tk.Label(pop, text="Publication Year", bg="light green")
            yearLabel.place(x=50, y=200)
            yearDataLabel = tk.Label(pop, text=publication_year, bg="light green")
            yearDataLabel.place(x=170, y=200)

            confirmButton = tk.Button(pop, text="Confirm \nWithdrawal\n", bg="light green", width=12, command=combine_funcs(pop.destroy, withdrawBook))
            confirmButton.place(x=120, y= 240)

            backButton = tk.Button(pop, text="Back to \nWithdrawal\nFunction", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=250, y= 240)

        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Withdrawal Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="Book removed from system.", bg="light green")
            statusLabel.place(x=70, y=150)

            backButton = tk.Button(pop, text="Back to \nWithdrawal\nFunction", bg="light green", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text = "To Remove Outdated Books From System, Please Enter Required Information Below:", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        accessionNumberLabel = tk.Label(master, text = "Accession Number", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        accessionNumberEntry = tk.Entry(master, textvariable = "Used to identify an instance of book", width = 60)
        accessionNumberLabel.place(x=320, y=350)
        accessionNumberEntry.place(x=470, y=355)
        accessionNumberEntry.delete(0, END)

        withdrawButton = tk.Button(master, text = "Withdraw Book", height = 3, width = 15, padx = 5, command=checkFirst)
        withdrawButton.place(x=470, y=440)
        
        backButton = tk.Button(master, text = "Back to Books Menu", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(booksOptions.BooksOptionsPage))
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    Withdrawal = BookWithdrawalPage()
    Withdrawal.mainloop()
