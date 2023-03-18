import tkinter as tk
from turtle import width
from tkinter import messagebox
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import tkinter.ttk as ttk
from typing import Text
from PIL import ImageTk, Image
import re
import lib.sql_database as sql_db
from datetime import datetime, timedelta

import lib.loansOptions as loansOptions

class BorrowPage(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        database = sql_db.Database()
        master.title("Borrow Page")
        master.geometry("1366x768")

        def checkFirst():
            # variables
            regexID = r'^[a-zA-Z][0-9]+[a-zA-Z]$'
            regexBookID = r'^[a-zA-Z][0-9]+$'
            memberID = membershipIDEntry.get()
            bookID = accessionNumberEntry.get()

            # Check empty fields
            if(len(memberID) < 1 or len(bookID) < 1):
                return fail_popup("empty")

            # Check book format
            if(not re.fullmatch(regexBookID, bookID)):
                return fail_popup("bookformat")

            # Check book exist
            checkBook = database.checkBookExist(bookID)
            if(checkBook < 1):
                return fail_popup("bookexist")

            # Check member id format
            if(not re.fullmatch(regexID, memberID) or len(memberID) > 6):
                return fail_popup("IDformat")

            # Check member exists
            checkMem = database.checkMemberExist(memberID)
            if(checkMem < 1):
                return fail_popup("IDexist")
            
            # Check if loaned by the person
            checkLoanedByYou = database.checkLoanByYou(bookID, memberID)
            if(checkLoanedByYou > 0):
                return fail_popup("loanedbyyou")

            # Check if loaned
            checkLoaned = database.checkLoanStatus(bookID)
            if(checkLoaned > 0):
                return fail_popup("loaned")

            # Check if reserved
            checkReserved = database.checkReservedStatus(bookID)
            checkReservedOwn = database.checkReservedOwnStatus(bookID, memberID)
            if(checkReserved > 0 and not checkReservedOwn):
                return fail_popup("reserved")

            # Check if exceed max loan count
            checkBookLoanCount = database.getNumOfLoans(memberID)
            if(checkBookLoanCount == 2):
                return fail_popup("maxloan")

            # Check if have fine
            checkFine = database.getFineAmount(memberID)
            if(checkFine > 0):
                return fail_popup("fine")
            
            # Check if the book is truly yours or others (for multiple reservations)
            
            return confirm_popup()

        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Book Loan Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="red")

            errorLabel = tk.Label(pop, text="Error!", bg="red", fg="yellow")
            errorLabel.place(x=120, y=70)

            if (reason == "empty"):
                statusLabel = tk.Label(pop, text="Missing or \nIncomplete fields!", bg="red", fg="yellow")
                statusLabel.place(x=90, y=150)
            elif (reason == "IDformat"):
                statusLabel = tk.Label(pop, text="Member ID format incorrect!\nPlease follow this format:\nA101A (6 characters and below).", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)
            elif (reason == "IDexist"):
                statusLabel = tk.Label(pop, text="Member does not exist!", bg="red", fg="yellow")
                statusLabel.place(x=70, y=150)
            elif (reason == "bookformat"):
                statusLabel = tk.Label(pop, text="Accession number format incorrect!\nPlease follow this format:\nA01", bg="red", fg="yellow")
                statusLabel.place(x=40, y=150)
            elif (reason == "bookexist"):
                statusLabel = tk.Label(pop, text="Book does not exist!", bg="red", fg="yellow")
                statusLabel.place(x=80, y=150)
            elif (reason == "loanedbyyou"):
                statusLabel = tk.Label(pop, text="Book currently on loan by you!", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)
            elif (reason == "loaned"):
                bookID = accessionNumberEntry.get()
                dueDate = database.getBorrowedDate(bookID) + timedelta(days=14)
                dueDate_formatted  = dueDate.strftime('%Y-%m-%d')
                statusLabel = tk.Label(pop, text="Book currently on loan until:\n" + dueDate_formatted, bg="red", fg="yellow")
                statusLabel.place(x=60, y=150)
            elif (reason == "reserved"):
                statusLabel = tk.Label(pop, text="Book currently reserved.", bg="red", fg="yellow")
                statusLabel.place(x=70, y=150)
            elif (reason == "maxloan"):
                statusLabel = tk.Label(pop, text="Member loan quota exceeded.\nYou can only borrow 2 books at a time.", bg="red", fg="yellow")
                statusLabel.place(x=20, y=150)
            elif (reason == "fine"):
                statusLabel = tk.Label(pop, text="Member has outstanding fines.", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)

            backButton = tk.Button(pop, text="Back to \nBorrow Function", bg="red", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        def borrowBook():
            memberID = membershipIDEntry.get()
            bookID = accessionNumberEntry.get()
            isReserved = database.checkReservedOwnStatus(bookID, memberID)

            # Delete from reservation records if it was a reserved book
            if(isReserved):
                database.cancelReservation(bookID, memberID)
                
            database.borrowBook(bookID, memberID, datetime.today().strftime('%Y-%m-%d'))
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
            pop.title("Book Loan Details")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            # variable
            bookID = accessionNumberEntry.get()
            bookTitle = database.getBookTitle(bookID)
            borrowDate = datetime.today().strftime('%Y-%m-%d')
            memberID = membershipIDEntry.get()
            memberName = database.getMemberName(memberID)
            dueDate = datetime.today() + timedelta(days=14)
            dueDate_formatted  = dueDate.strftime('%Y-%m-%d')


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

            borrowDateLabel = tk.Label(pop, text="Borrow Date", bg="light green")
            borrowDateLabel.place(x=10, y=110)
            borrowDateDataLabel = tk.Label(pop, text=borrowDate, bg="light green")
            borrowDateDataLabel.place(x=130, y=110)

            membershipIDLabel = tk.Label(pop, text="Membership ID", bg="light green")
            membershipIDLabel.place(x=10, y=140)
            membershipIDDataLabel = tk.Label(pop, text=memberID, bg="light green")
            membershipIDDataLabel.place(x=130, y=140)

            memberNameLabel = tk.Label(pop, text="Member Name", bg="light green")
            memberNameLabel.place(x=10, y=170)
            memberNameDataLabel = tk.Label(pop, text=memberName, bg="light green")
            memberNameDataLabel.place(x=130, y=170)

            dueDateLabel = tk.Label(pop, text="Due Date", bg="light green")
            dueDateLabel.place(x=10, y=200)
            dueDateDataLabel = tk.Label(pop, text=dueDate_formatted, bg="light green")
            dueDateDataLabel.place(x=130, y=200)

            confirmButton = tk.Button(pop, text="Confirm \nLoan", bg="light green", width=12, command=combine_funcs(pop.destroy, borrowBook))
            confirmButton.place(x=30, y= 240)

            backButton = tk.Button(pop, text="Back to \nBorrow Function", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=160, y= 240)

        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Loan Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")
            dueDate = datetime.today() + timedelta(days=14)
            dueDate_formatted  = dueDate.strftime('%Y-%m-%d')
            
            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="Book due on: \n" + dueDate_formatted + ".", bg="light green")
            statusLabel.place(x=100, y=150)

            backButton = tk.Button(pop, text="Back to \nBorrow Function", bg="light green", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        # making background
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image=self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text="To Borrow A Book, Please Enter Information Below:",\
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        accessionNumberLabel = tk.Label(master, text="Accession Number", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        accessionNumberLabel.place(x=320, y=300)
        accessionNumberEntry = tk.Entry(master, textvariable = "Used to identify an instance of book", width = 60)
        accessionNumberEntry.place(x=470, y=305)
        accessionNumberEntry.delete(0, END)

        membershipIDLabel = tk.Label(master, text="Membership ID", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        membershipIDLabel.place(x=320, y=350)
        membershipIDEntry = tk.Entry(master, textvariable = "A unique alphanumeric id that distinguishes every member", width = 60)
        membershipIDEntry.place(x=470, y=355)
        membershipIDEntry.delete(0, END)

        borrowButton = tk.Button(master, text="Borrow Book", bg="#30D5C8", height = 3, width = 15, padx = 5, command=checkFirst)
        borrowButton.place(x=470, y=440)

        backButton = tk.Button(master, text="Back to Loans Menu", bg="#30D5C8", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(loansOptions.LoansOptionsPage))
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    Borrow = BorrowPage()
    Borrow.mainloop()