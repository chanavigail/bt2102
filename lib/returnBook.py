import tkinter as tk
from turtle import width
from tkinter import messagebox
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import tkinter.ttk as ttk
from typing import Text
from PIL import ImageTk, Image
import re
import lib.sql_database as sql_db
import datetime

import lib.loansOptions as loansOptions

class ReturnPage(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        database = sql_db.Database()
        master.title("Return Page")
        master.geometry("1366x768")

        def fine_or_not(fine):
            if (fine <= 14):
                return str(0)
            else:
                return str(fine - 14)

        def checkFirst():
            dateFormat = "%Y-%m-%d"
            regexBookID = r'^[a-zA-Z][0-9]+$'
            bookID = accessionNumberEntry.get()
            returnDate = returnDateEntry.get()
            
            # Check empty fields
            if(len(bookID) < 1 or len(returnDate) < 1):
                return fail_popup("empty")
            
            # Check book format
            if(not re.fullmatch(regexBookID, bookID)):
                return fail_popup("bookformat")

            # Check book exist
            checkBook = database.checkBookExist(bookID)
            if(checkBook < 1):
                return fail_popup("bookexist")

            # Check date format
            try:
                datetime.datetime.strptime(returnDate, dateFormat)
            except ValueError:
                return fail_popup("date")

            # Check if book is loaned
            checkLoaned = database.checkLoanStatus(bookID)
            if(checkLoaned < 1):
                return fail_popup("notloaned")
            
            # Check if return date is before borrow date
            borrowDate = database.getBorrowedDate(bookID)
            borrowDateDatetime = datetime.datetime.combine(borrowDate, datetime.time()).date()
            returnDateDatetime = datetime.datetime.strptime(returnDate, '%Y-%m-%d').date()

            if(returnDateDatetime < borrowDateDatetime):
                return fail_popup("wrongdate")
            
            # Check if return date is before today's date
            todayDateDatetime = datetime.datetime.now().date()

            if(returnDateDatetime < todayDateDatetime):
                return fail_popup("beforetoday")
                
            return confirm_popup()
        
        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Book Return Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="red")

            errorLabel = tk.Label(pop, text="Error!", bg="red", fg="yellow")
            errorLabel.place(x=130, y=70)

            if (reason == "empty"):
                statusLabel = tk.Label(pop, text="Missing or \nIncomplete fields!", bg="red", fg="yellow")
                statusLabel.place(x=90, y=150)
            elif (reason == "bookformat"):
                statusLabel = tk.Label(pop, text="Accession number format incorrect!", bg="red", fg="yellow")
                statusLabel.place(x=40, y=150)
            elif (reason == "bookexist"):
                statusLabel = tk.Label(pop, text="Book does not exist!", bg="red", fg="yellow")
                statusLabel.place(x=80, y=150)
            elif (reason == "date"):
                statusLabel = tk.Label(pop, text="Incorrect date format! YYYY-MM-DD", bg="red", fg="yellow")
                statusLabel.place(x=30, y=150)
            elif (reason == "notloaned"):
                statusLabel = tk.Label(pop, text="Book is not on loan.", bg="red", fg="yellow")
                statusLabel.place(x=80, y=150)
            elif (reason == "wrongdate"):
                statusLabel = tk.Label(pop, text="Return date cannot be before borrow date.", bg="red", fg="yellow")
                statusLabel.place(x=20, y=150)
            elif (reason == "beforetoday"):
                statusLabel = tk.Label(pop, text="Return date cannot be before today's date.", bg="red", fg="yellow")
                statusLabel.place(x=20, y=150)

            backButton = tk.Button(pop, text="Back to \nReturn Function", bg="red", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        def returnBook():
            bookID = accessionNumberEntry.get()
            memberID = database.getBorrowerID(bookID)

            # check fine amount
            returnDate = returnDateEntry.get()
            returnDateDatetime = datetime.datetime.strptime(returnDate, '%Y-%m-%d')
            borrowDate = database.getBorrowedDate(bookID)
            borrowDateDatetime = datetime.datetime.combine(borrowDate, datetime.time())
            fine = returnDateDatetime - borrowDateDatetime
            fineInt = fine.days

            fineAmt = int(fine_or_not(fineInt))

            database.addToExistingFine(fineAmt, memberID)
            database.returnBook(bookID)
            fineAmt = database.getFineAmount(memberID)
            if (fineAmt):
                return total_fine_fail_popup(fineAmt)
            else:
                return success_popup()

        # Generic function for two functions in one button

        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func

        # Status popups

        def confirm_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Return Details")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            # variable
            bookID = accessionNumberEntry.get()
            returnDate = returnDateEntry.get()
            bookTitle = database.getBookTitle(bookID)
            memberID = database.getBorrowerID(bookID)
            memberName = database.getMemberName(memberID)
            returnDateDatetime = datetime.datetime.strptime(returnDate, '%Y-%m-%d')
            borrowDate = database.getBorrowedDate(bookID)
            borrowDateDatetime = datetime.datetime.combine(borrowDate, datetime.time())
            fine = returnDateDatetime - borrowDateDatetime
            fineInt = fine.days

            msgLabel = tk.Label(pop, text="Please Confirm Details to Be Correct", font='Helvetica 12 bold', bg="light green")
            msgLabel.place(x=50, y=10)

            accessionNumberLabel = tk.Label(pop, text="Accession Number", bg="light green")
            accessionNumberLabel.place(x=10, y=50)
            accessionNumberDataLabel = tk.Label(pop, text=bookID, bg="light green")
            accessionNumberDataLabel.place(x=130, y=50)

            bookTitleLabel = tk.Label(pop, text="Book Title", bg="light green")
            bookTitleLabel.place(x=10, y=80)
            bookTitleDataLabel = tk.Label(pop, text=bookTitle, bg="light green")
            bookTitleDataLabel.place(x=130, y=80)

            membershipIDLabel = tk.Label(pop, text="Membership ID", bg="light green")
            membershipIDLabel.place(x=10, y=110)
            membershipIDDataLabel = tk.Label(pop, text=memberID, bg="light green")
            membershipIDDataLabel.place(x=130, y=110)

            memberNameLabel = tk.Label(pop, text="Member Name", bg="light green")
            memberNameLabel.place(x=10, y=140)
            memberNameDataLabel = tk.Label(pop, text=memberName, bg="light green")
            memberNameDataLabel.place(x=130, y=140)

            returnDateLabel = tk.Label(pop, text="Return Date", bg="light green")
            returnDateLabel.place(x=10, y=170)
            returnDateDataLabel = tk.Label(pop, text=returnDate, bg="light green")
            returnDateDataLabel.place(x=130, y=170)

            fineLabel = tk.Label(pop, text="Fine", bg="light green")
            fineLabel.place(x=10, y=200)
            fineDataLabel = tk.Label(pop, text=fine_or_not(fineInt), bg="light green")
            fineDataLabel.place(x=130, y=200)

            confirmButton = tk.Button(pop, text="Confirm \nReturn", bg="light green", width=12, command=combine_funcs(pop.destroy, returnBook))
            confirmButton.place(x=30, y= 240)

            backButton = tk.Button(pop, text="Back to \nReturn Function", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=160, y= 240)

        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Return Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="Book returned successfully.", bg="light green")
            statusLabel.place(x=70, y=150)

            backButton = tk.Button(pop, text="Back to \nReturn Function", bg="light green", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        def total_fine_fail_popup(fineAmt):
            pop = tk.Toplevel(master)
            pop.title("Book Return Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="red")

            errorLabel = tk.Label(pop, text="Error!", bg="red", fg="yellow")
            errorLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="Book returned successfully \nbut you still have a fine of $" + str(fineAmt) +".", bg="red", fg="yellow")
            statusLabel.place(x=50, y=150)

            backButton = tk.Button(pop, text="Back to \nReturn Function", bg="red", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)



        # making background
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image=self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text="To Return A Book, Please Enter Information Below:",\
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        accessionNumberLabel = tk.Label(master, text="Accession Number", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        accessionNumberLabel.place(x=320, y=300)
        accessionNumberEntry = tk.Entry(master, textvariable = "Used to identify an instance of book", width = 60)
        accessionNumberEntry.place(x=470, y=305)
        accessionNumberEntry.delete(0, END)

        returnDateLabel = tk.Label(master, text="Return Date", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        returnDateLabel.place(x=320, y=350)
        returnDateEntry = tk.Entry(master, textvariable = "Date of book return", width = 60)
        returnDateEntry.place(x=470, y=355)
        returnDateEntry.delete(0, END)

        returnButton = tk.Button(master, text="Return Book", bg="#30D5C8", height = 3, width = 15, padx = 5, command=checkFirst)
        returnButton.place(x=470, y=440)
        backButton = tk.Button(master, text="Back to Loans Menu", bg="#30D5C8", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(loansOptions.LoansOptionsPage))
        backButton.place(x=750, y=440)
        
if __name__ == "__main__":
    Return = ReturnPage()
    Return.mainloop()