import tkinter as tk
from turtle import width
from tkinter import messagebox
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import tkinter.ttk as ttk
from typing import Text
from PIL import ImageTk, Image

import lib.reservationsOptions as reservationsOptions
import re
import datetime
import lib.sql_database as sql_db

class ReservePage(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Reserve Page")
        master.geometry("1366x768")
        database = sql_db.Database()

        # Generic function for two functions in one button

        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func

        def reserveBook():
            bookID = accessionNumberEntry.get()
            memberID = memberIDEntry.get()
            reserveDate = reserveDateEntry.get()
            database.reserveBook(bookID, memberID, reserveDate)
            return success_popup()

        def checkFirst():
            regexID = r'^[a-zA-Z][0-9]+[a-zA-Z]$'
            regexBookID = r'^[a-zA-Z][0-9]+$'
            dateFormat = "%Y-%m-%d"
            bookID = accessionNumberEntry.get()
            id = memberIDEntry.get()
            reserve_date = reserveDateEntry.get()

            # Check empty fields
            if(len(bookID) < 1 or len(id) < 1 or len(reserve_date) < 1):
                return fail_popup("empty")

            # Check book format
            if(not re.fullmatch(regexBookID, bookID)):
                return fail_popup("bookformat")

            # Check book exist
            checkBook = database.checkBookExist(bookID)
            if(checkBook < 1):
                return fail_popup("bookexist")

            # Check member id format
            if(not re.fullmatch(regexID, id) or len(id) > 6):
                return fail_popup("IDformat")

            # Check member exists
            checkMem = database.checkMemberExist(id)
            if(checkMem < 1):
                return fail_popup("IDexist")
            
            # Check date format
            try:
                datetime.datetime.strptime(reserve_date, dateFormat)
            except ValueError:
                return fail_popup("date")
            
            # Check if reserve date is before today's date
            reserveDateDatetime = datetime.datetime.strptime(reserve_date, '%Y-%m-%d').date()
            todayDateDatetime = datetime.datetime.now().date()

            if(reserveDateDatetime < todayDateDatetime):
                return fail_popup("beforetoday")
            
            # Check if member reserved this book before
            checkReservedOwn = database.checkReservedOwnStatus(bookID, id)
            if(checkReservedOwn > 0):
                return fail_popup("reservedbefore")

            # Check if reservation count exceeded
            checkNumOfRsv = database.getNumOfReservations(id)
            if(checkNumOfRsv == 2):
                return fail_popup("maxrsv")

            fineAmt = database.getFineAmount(id)
            if(fineAmt) > 0:
                return fail_popup("fine")
            
            # Don't need to check if book is reserved already according to email stating multiple members can reserve same book.
            
            return confirm_popup()

        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Book Reservation Status")
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
            elif (reason == "IDformat"):
                statusLabel = tk.Label(pop, text="Member ID format incorrect!\nPlease follow this format:\nA101A (6 characters and below).", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)
            elif (reason == "IDexist"):
                statusLabel = tk.Label(pop, text="Member does not exist!", bg="red", fg="yellow")
                statusLabel.place(x=70, y=150)
            elif (reason == "date"):
                statusLabel = tk.Label(pop, text="Incorrect date format! YYYY-MM-DD", bg="red", fg="yellow")
                statusLabel.place(x=30, y=150)
            elif (reason == "beforetoday"):
                statusLabel = tk.Label(pop, text="Reserve date cannot be before today's date.", bg="red", fg="yellow")
                statusLabel.place(x=20, y=150)
            elif (reason == "reservedbefore"):
                statusLabel = tk.Label(pop, text="Member has already reserved this book.", bg="red", fg="yellow")
                statusLabel.place(x=30, y=150)
            elif (reason == "maxrsv"):
                statusLabel = tk.Label(pop, text="Member currently has\n2 books on reservation.", bg="red", fg="yellow")
                statusLabel.place(x=80, y=150)
            elif (reason == "fine"):
                fineAmt = database.getFineAmount(memberIDEntry.get())
                statusLabel = tk.Label(pop, text="Member has outstanding fine of: $"+ str(fineAmt) + ".\nPlease pay before reserving.", bg="red", fg="yellow")
                statusLabel.place(x=40, y=150)
            
            backButton = tk.Button(pop, text="Back to \nReserve Function", bg="red", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        def confirm_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Return Details")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Please Confirm Details to Be Correct", font='Helvetica 12 bold', bg="light green")
            msgLabel.place(x=50, y=10)

            bookID = accessionNumberEntry.get()
            bookTitle = database.getBookTitle(bookID)
            memberID = memberIDEntry.get()
            memberName = database.getMemberName(memberID)
            reserveDate = reserveDateEntry.get()

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

            reserveDateLabel = tk.Label(pop, text="Reserve Date", bg="light green")
            reserveDateLabel.place(x=10, y=170)
            reserveDateDataLabel = tk.Label(pop, text=reserveDate, bg="light green")
            reserveDateDataLabel.place(x=130, y=170)

            confirmButton = tk.Button(pop, text="Confirm \nReservation", bg="light green", width=12, command=combine_funcs(pop.destroy, reserveBook))
            confirmButton.place(x=30, y= 240)

            backButton = tk.Button(pop, text="Back to \nReserve Function", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=160, y= 240)

        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Book Reservation Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="Book reserved successfully.", bg="light green")
            statusLabel.place(x=70, y=150)

            backButton = tk.Button(pop, text="Back to \nReserve Function", bg="light green", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        # making background
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image=self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text="To Reserve A Book, Please Enter Information Below:",\
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        accessionNumberLabel = tk.Label(master, text="Accession Number", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        accessionNumberEntry = tk.Entry(master, textvariable = "Used to identify an instance of book", width = 60)
        accessionNumberLabel.place(x=320, y=280)
        accessionNumberEntry.place(x=470, y=285)
        accessionNumberEntry.delete(0, END)

        memberIDLabel = tk.Label(master, text="Membership ID", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        memberIDEntry = tk.Entry(master, textvariable = "A unique alphanumeric id that distinguishes every member", width = 60)
        memberIDLabel.place(x=320, y=330)
        memberIDEntry.place(x=470, y=335)
        memberIDEntry.delete(0, END)
        
        reserveDateLabel = tk.Label(master, text="Reserve Date", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        reserveDateEntry = tk.Entry(master, textvariable = "Date of book reservation", width = 60)
        reserveDateLabel.place(x=320, y=380)
        reserveDateEntry.place(x=470, y=385)
        reserveDateEntry.delete(0, END)

        reserveButton = tk.Button(master, text="Reserve Book", bg="#30D5C8", height = 3, width = 15, padx = 5, command=checkFirst)
        reserveButton.place(x=470, y=440)
        
        backButton = tk.Button(master, text="Back to\nReservations Menu", bg="#30D5C8", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(reservationsOptions.ReservationsOptionsPage))
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    Reserve = ReservePage()
    Reserve.mainloop()