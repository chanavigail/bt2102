import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.booksOptions as booksOptions
import lib.sql_database as sql_db
import re

class BookAcquisitionPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Book Acquisition")
        master.geometry("1366x768")
        database = sql_db.Database()

        def acquireBook():
            regexBookID = r'^[a-zA-Z][0-9]+$'
            regexNum = r'^[0-9]+$'
            regexAuthors = r'^(\w+)(,\s\s*\w+)*$'

            bookID = accessionNumberEntry.get()
            title = titleEntry.get()
            authors = authorsEntry.get()
            isbn = isbnNumberEntry.get()
            publisher = publisherEntry.get()
            publish_year = publishYearEntry.get()

            # Check empty fields
            if(len(bookID) < 1 or len(title) < 1 or len(authors) < 1 or len(isbn) < 1 or len(publisher) < 1 or len(publish_year) < 1):
                return fail_popup("empty")

            # Check accession number format
            if(not re.fullmatch(regexBookID, bookID)):
                return fail_popup("bookformat")

            # Check if accession number already in system
            checkBook = database.checkBookExist(bookID)
            if(checkBook > 0):
                return fail_popup("bookexist")

            # Check authors list
            if (not re.fullmatch(regexAuthors, authors)):
                return fail_popup("author")
            
            # Check for duplicate authors
            authors_list = authors.split(", ")
            if (len(authors_list) != len(set(authors_list))):
                return fail_popup("dup")
            
            # Check ISBN
            if (len(isbn) != 13 or not re.fullmatch(regexNum, isbn)):
                return fail_popup("isbn")
            
            # Check year
            if (len(publish_year) != 4 or not re.fullmatch(regexNum, publish_year)):
                return fail_popup("year")
            
            database.addAuthors(bookID, authors)
            database.addBook((bookID, isbn, title, publisher, publish_year))
            return success_popup()
        
        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Book Acquisition Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="red")

            errorLabel = tk.Label(pop, text="Error!", bg="red", fg="yellow")
            errorLabel.place(x=130, y=70)

            if (reason == "empty"):
                statusLabel = tk.Label(pop, text="Missing or \nIncomplete fields!", bg="red", fg="yellow")
                statusLabel.place(x=80, y=150)
            elif (reason == "bookformat"):
                statusLabel = tk.Label(pop, text="Accession number format incorrect!\nPlease follow this format:\nA01", bg="red", fg="yellow")
                statusLabel.place(x=40, y=150)
            elif (reason == "bookexist"):
                statusLabel = tk.Label(pop, text="Book exists in the system!", bg="red", fg="yellow")
                statusLabel.place(x=65, y=150)
            elif (reason == "author"):
                statusLabel = tk.Label(pop, text="Author(s) format wrong!\nPlease follow this format:\nauthor1, author2, author3", bg="red", fg="yellow")
                statusLabel.place(x=60, y=150)
            elif (reason == "dup"):
                statusLabel = tk.Label(pop, text="Please do not input\nduplicate author names.", bg="red", fg="yellow")
                statusLabel.place(x=70, y=150)
            elif (reason == "isbn"):
                statusLabel = tk.Label(pop, text="ISBN must be a numeric of length 13.", bg="red", fg="yellow")
                statusLabel.place(x=40, y=150)
            elif (reason == "year"):
                statusLabel = tk.Label(pop, text="Incorrect year format.\nPlease follow YYYY format.", bg="red", fg="yellow")
                statusLabel.place(x=60, y=150)

            backButton = tk.Button(pop, text="Back to \nAcquisition \nFunction", bg="red", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)

        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Acquisition Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="New Book added in Library.", bg="light green")
            statusLabel.place(x=70, y=150)

            backButton = tk.Button(pop, text="Back to \nAcquisition\nFunction", bg="light green", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)

        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text = "For New Book Acquisition, Please Enter Required Information Below:", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        accessionNumberLabel = tk.Label(master, text = "Accession Number", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        accessionNumberEntry = tk.Entry(master, textvariable = "Used to identify an instance of book", width = 60)
        accessionNumberLabel.place(x=320, y=180)
        accessionNumberEntry.place(x=470, y=185)
        accessionNumberEntry.delete(0, END)

        titleLabel = tk.Label(master, text = "Title", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        titleEntry = tk.Entry(master, textvariable = "Book Title", width = 60)
        titleLabel.place(x=320, y=230)
        titleEntry.place(x=470, y=235)
        titleEntry.delete(0, END)

        authorsLabel = tk.Label(master, text = "Authors", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        authorsEntry = tk.Entry(master, textvariable = "There can be multiple authors for a book", width = 60)
        authorsLabel.place(x=320, y=280)
        authorsEntry.place(x=470, y=285)
        authorsEntry.delete(0, END)

        isbnLabel = tk.Label(master, text = "ISBN", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        isbnNumberEntry = tk.Entry(master, textvariable = "ISBN Number", width = 60)
        isbnLabel.place(x=320, y=330)
        isbnNumberEntry.place(x=470, y=335)
        isbnNumberEntry.delete(0, END)
        
        publisherLabel = tk.Label(master, text = "Publisher", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        publisherEntry = tk.Entry(master, textvariable = "Random House, Penguin, Cengage, Springer, etc.", width = 60)
        publisherLabel.place(x=320, y=380)
        publisherEntry.place(x=470, y=385)
        publisherEntry.delete(0,END)

        publishYearLabel = tk.Label(master, text = "Publication Year", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        publishYearEntry = tk.Entry(master, textvariable = "Edition year", width = 60)
        publishYearLabel.place(x=320, y=430)
        publishYearEntry.place(x=470, y=435)
        publisherEntry.delete(0, END)

        addButton = tk.Button(master, text = "Add New Book", height = 3, width = 15, padx = 5, command=acquireBook)
        addButton.place(x=470, y=480)
        
        backButton = tk.Button(master, text = "Back to Books Menu", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(booksOptions.BooksOptionsPage))
        backButton.place(x=750, y=485)

if __name__ == "__main__":
    Acquisition = BookAcquisitionPage()
    Acquisition.mainloop()
