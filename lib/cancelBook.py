import tkinter as tk
from turtle import width
from tkinter import messagebox
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import tkinter.ttk as ttk
from typing import Text
from PIL import ImageTk, Image

import lib.reservationsOptions as reservationsOptions
import lib.sql_database as sql_db
import re
import datetime

class CancelPage(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Cancellation Page")
        master.geometry("1366x768")
        database = sql_db.Database()

        # Generic function for two functions in one button

        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func
        
        def cancelReservation():
            bookID = accessionNumberEntry.get()
            memberID = memberIDEntry.get()
            database.cancelReservation(bookID, memberID)
            success_popup()

        def checkFirst():
            regexID = r'^[a-zA-Z][0-9]+[a-zA-Z]$'
            regexBookID = r'^[a-zA-Z][0-9]+$'
            dateFormat = "%Y-%m-%d"
            bookID = accessionNumberEntry.get()
            id = memberIDEntry.get()
            cancel_date = cancelDateEntry.get()

            # Check empty fields
            if(len(bookID) < 1 or len(id) < 1 or len(cancel_date) < 1):
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
                datetime.datetime.strptime(cancel_date, dateFormat)
            except ValueError:
                return fail_popup("date")
            
            # Check if reserve date is before today's date
            cancelDateDatetime = datetime.datetime.strptime(cancel_date, '%Y-%m-%d').date()
            todayDateDatetime = datetime.datetime.now().date()

            if(cancelDateDatetime < todayDateDatetime):
                return fail_popup("beforetoday")

            # Check if member has this reservation
            checkReservation = database.checkReservedOwnStatus(bookID, id)
            if(checkReservation < 1):
                return fail_popup("rsvexist")
            
            return confirm_popup()

        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Cancellation Status")
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
                statusLabel = tk.Label(pop, text="Cancellation date cannot be\nbefore today's date.", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)
            elif(reason == "rsvexist"):
                statusLabel = tk.Label(pop, text="Member has no such reservation.", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)

            backButton = tk.Button(pop, text="Back to \nCancellation\nFunction", bg="red", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        def confirm_popup():
            pop = tk.Toplevel(master)
            pop.title("Cancellation Details")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Please Confirm Details to Be Correct", font='Helvetica 12 bold', bg="light green")
            msgLabel.place(x=50, y=10)

            bookID = accessionNumberEntry.get()
            bookTitle = database.getBookTitle(bookID)
            memberID = memberIDEntry.get()
            memberName = database.getMemberName(memberID)
            cancelDate = cancelDateEntry.get()
            
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

            cancelDateLabel = tk.Label(pop, text="Cancellation Date", bg="light green")
            cancelDateLabel.place(x=10, y=170)
            cancelDateDataLabel = tk.Label(pop, text=cancelDate, bg="light green")
            cancelDateDataLabel.place(x=130, y=170)

            confirmButton = tk.Button(pop, text="Confirm \nCancellation\n", bg="light green", width=12, command=combine_funcs(pop.destroy, cancelReservation))
            confirmButton.place(x=30, y= 240)

            backButton = tk.Button(pop, text="Back to \nCancellation\nFunction", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=160, y= 240)

        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Cancellation Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="Reservation cancelled successfully.", bg="light green")
            statusLabel.place(x=40, y=150)

            backButton = tk.Button(pop, text="Back to \nCancellation\nFunction", bg="light green", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        # making background
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image=self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        # define the labels
        topLabel = tk.Label(master, text="To Cancel a Reservation, Please Enter Information Below:",\
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

        cancelDateLabel = tk.Label(master, text="Cancel Date", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        cancelDateEntry = tk.Entry(master, textvariable = "Date of Reservation Cancellation", width = 60)
        cancelDateLabel.place(x=320, y=380)
        cancelDateEntry.place(x=470, y=385)
        cancelDateEntry.delete(0, END)

        cancelButton = tk.Button(master, text="Cancel Reservation", bg="#30D5C8", height = 3, width = 15, padx = 5, command=checkFirst)
        cancelButton.place(x=470, y=440)

        backButton = tk.Button(master, text="Back to\nReservations Menu", bg="#30D5C8", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(reservationsOptions.ReservationsOptionsPage))
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    Cancel = CancelPage()
    Cancel.mainloop()