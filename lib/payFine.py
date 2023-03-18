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

import lib.finesOptions as finesOptions

class PayFinePage(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        database = sql_db.Database()
        master.title("Fine Payment Page")
        master.geometry("1366x768")
        
        # Generic function for two functions in one button
        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func

        # Check fields    
        def checkFirst():
            regexID = r'^[a-zA-Z][0-9]+[a-zA-Z]$'
            regexAmt = r'^[0-9]+$'
            dateFormat = "%Y-%m-%d"
            id = membershipIDEntry.get()
            payDate = paymentDateEntry.get()
            payAmt = paymentAmountEntry.get()

            # Check empty fields
            if(len(id) < 1 or len(payDate) < 1 or len(payAmt) < 1):
                return fail_popup("empty")

            # Check member id format
            if(not re.fullmatch(regexID, id) or len(id) > 6):
                return fail_popup("IDformat")

            # Check member exists
            checkMem = database.checkMemberExist(id)
            if(checkMem < 1):
                return fail_popup("IDexist")
            
            # Check date format
            try:
                datetime.datetime.strptime(payDate, dateFormat)
            except ValueError:
                return fail_popup("date")
            
            # Check if payment date is before today's date
            payDateDatetime = datetime.datetime.strptime(payDate, '%Y-%m-%d').date()
            todayDateDatetime = datetime.datetime.now().date()

            if(payDateDatetime < todayDateDatetime):
                return fail_popup("beforetoday")

            # Check Payment Amount
            if(not re.fullmatch(regexAmt, payAmt)):
                return fail_popup("payformat")

            checkAmt = str(database.getFineAmount(id))

            if(checkAmt == "0"):
                return fail_popup("zero")

            if(payAmt != checkAmt):
                return fail_popup("amt")
            
            return confirm_popup()
        
        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Fine Payment Status")
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
                statusLabel = tk.Label(pop, text="Member does not exist!", bg="red", fg="yellow")
                statusLabel.place(x=70, y=150)
            elif (reason == "date"):
                statusLabel = tk.Label(pop, text="Incorrect date format! YYYY-MM-DD", bg="red", fg="yellow")
                statusLabel.place(x=30, y=150)
            elif (reason == "beforetoday"):
                statusLabel = tk.Label(pop, text="Payment date cannot be before today's date.", bg="red", fg="yellow")
                statusLabel.place(x=10, y=150)
            elif (reason == "payformat"):
                statusLabel = tk.Label(pop, text="Payment amount needs to be an integer!", bg="red", fg="yellow")
                statusLabel.place(x=30, y=150)   
            elif (reason == "amt"):
                fineAmt = database.getFineAmount(membershipIDEntry.get())
                statusLabel = tk.Label(pop, text="Incorrect Fine Payment Amount.\n" + "Please pay $"+ str(fineAmt) + ".", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)
            elif (reason == "zero"):
                statusLabel = tk.Label(pop, text="Member has no fine.", bg="red", fg="yellow")
                statusLabel.place(x=80, y=150)

            backButton = tk.Button(pop, text="Back to \nPayment\nFunction", bg="red", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)
        
        # Pay up!
        def payFine():
            id = membershipIDEntry.get()
            payDate = paymentDateEntry.get()

            database.removeFine(id, payDate)
            success_popup()

        # Confirmation popup screen
        def confirm_popup():
            pop = tk.Toplevel(master)
            pop.title("Fine Payment Details")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Please Confirm Details to Be Correct", font='Helvetica 12 bold', bg="light green")
            msgLabel.place(x=50, y=10)

            paymentDueLabel = tk.Label(pop, text="Payment Due", bg="light green")
            paymentDueLabel.place(x=15, y=50)
            paymentDueDataLabel = tk.Label(pop, text=paymentAmountEntry.get(), bg="light green")
            paymentDueDataLabel.place(x=15, y=80)

            exactFeeLabel = tk.Label(pop, text="Exact Fee Only", bg="light green")
            exactFeeLabel.place(x=10, y=150)

            membershipIDLabel = tk.Label(pop, text="Member ID", bg="light green")
            membershipIDLabel.place(x=190, y=50)
            membershipIDDataLabel = tk.Label(pop, text=membershipIDEntry.get(), bg="light green")
            membershipIDDataLabel.place(x=190, y=80)

            paymentDateLabel = tk.Label(pop, text="Payment Date", bg="light green", width=12)
            paymentDateLabel.place(x=180, y=150)
            paymentDateDataLabel = tk.Label(pop, text=paymentDateEntry.get(), bg="light green")
            paymentDateDataLabel.place(x=190, y=180)

            confirmButton = tk.Button(pop, text="Confirm \nPayment\n", bg="light green", width=12, command=combine_funcs(pop.destroy, payFine))
            confirmButton.place(x=30, y= 240)

            backButton = tk.Button(pop, text="Back to \nPayment\nFunction", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=160, y= 240)

        # Success popup screen
        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Fine Payment Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="Fine has been paid successfully.", bg="light green")
            statusLabel.place(x=50, y=150)

            backButton = tk.Button(pop, text="Back to \nPayment\nFunction", bg="light green", width=15, command=pop.destroy)
            backButton.place(x=80, y= 230)

        # Making background
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image=self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        # Define the labels
        topLabel = tk.Label(master, text="To Pay a Fine, Please Enter Information Below:",\
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        membershipIDLabel = tk.Label(master, text="Membership ID", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        paymentDateLabel = tk.Label(master, text="Payment Date", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        paymentAmountLabel = tk.Label(master, text="Payment Amount", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")

        # Define the entry
        membershipIDEntry = tk.Entry(master, textvariable = "A unique alphanumeric id that distinguishes every member", width = 60)
        paymentDateEntry = tk.Entry(master, textvariable = "Date of Payment Received", width = 60)
        paymentAmountEntry = tk.Entry(master, textvariable = "Date of Amount Received", width = 60)

        # Define buttons
        payFineButton = tk.Button(master, text="Pay Fine", bg="#30D5C8", height = 3, width = 15, padx = 5, command=checkFirst)
        backButton = tk.Button(master, text="Back to\nFines Menu", bg="#30D5C8", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(finesOptions.FinesOptionsPage))

        # Place labels & entry
        topLabel.place(x=140, y=70)
        
        membershipIDLabel.place(x=320, y=280)
        membershipIDEntry.place(x=470, y=285)
        membershipIDEntry.delete(0, END)

        paymentDateLabel.place(x=320, y=330)
        paymentDateEntry.place(x=470, y=335)
        paymentDateEntry.delete(0, END)
        
        paymentAmountLabel.place(x=320, y=380)
        paymentAmountEntry.place(x=470, y=385)
        paymentAmountEntry.delete(0, END)

        # Place buttons
        payFineButton.place(x=470, y=440)
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    Fine = PayFinePage()
    Fine.mainloop()