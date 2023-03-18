import tkinter as tk
from turtle import width
from tkinter import messagebox
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import tkinter.ttk as ttk
from typing import Text
from PIL import ImageTk, Image

import lib.membershipsOptions as membershipsOptions
import lib.reportsOptions as reportsOptions
import lib.finesOptions as finesOptions
import lib.reservationsOptions as reservationsOptions
import lib.loansOptions as loansOptions
import lib.booksOptions as booksOptions

class MainPage(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Main Page")
        master.geometry("1366x768")

        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        # define images

        membership_img = Image.open("static/membership.png")
        membership_img = membership_img.resize((300,240), Image.ANTIALIAS)
        membership_img = ImageTk.PhotoImage(membership_img)

        books_img = Image.open("static/books.png")
        books_img = books_img.resize((300,240), Image.ANTIALIAS)
        books_img = ImageTk.PhotoImage(books_img)

        loans_img = Image.open("static/loans.png")
        loans_img = loans_img.resize((300,240), Image.ANTIALIAS)
        loans_img = ImageTk.PhotoImage(loans_img)

        reservations_img = Image.open("static/reservations.png")
        reservations_img = reservations_img.resize((300,240), Image.ANTIALIAS)
        reservations_img = ImageTk.PhotoImage(reservations_img)

        fines_img = Image.open("static/fines.png")
        fines_img = fines_img.resize((300,240), Image.ANTIALIAS)
        fines_img = ImageTk.PhotoImage(fines_img)

        reports_img = Image.open("static/reports.png")
        reports_img = reports_img.resize((300,240), Image.ANTIALIAS)
        reports_img = ImageTk.PhotoImage(reports_img)
        
        # define & place the buttons
        membership_btn = tk.Button(master, image = membership_img, text = "Membership", compound = "top", command=lambda:master.frameSwitcher(membershipsOptions.MembershipsOptionsPage))
        membership_btn.image = membership_img
        membership_btn.place(x=180, y=100)
        
        books_btn = tk.Button(master, image = books_img, text = "Books", compound = "top", command=lambda:master.frameSwitcher(booksOptions.BooksOptionsPage))
        books_btn.image = books_img
        books_btn.place(x=520, y=100)

        loans_btn = tk.Button(master, image = loans_img, text = "Loans", compound = "top", command=lambda:master.frameSwitcher(loansOptions.LoansOptionsPage))
        loans_btn.image = loans_img
        loans_btn.place(x=860, y=100)

        reservations_btn = tk.Button(master, image = reservations_img, text = "Reservations", compound = "top", command=lambda:master.frameSwitcher(reservationsOptions.ReservationsOptionsPage))
        reservations_btn.image = reservations_img
        reservations_btn.place(x=180, y=420)

        fines_btn = tk.Button(master, image = fines_img, text = "Fines", compound = "top", command=lambda:master.frameSwitcher(finesOptions.FinesOptionsPage))
        fines_btn.image = fines_img
        fines_btn.place(x=520, y=420)

        reports_btn = tk.Button(master, image = reports_img, text = "Reports", compound = "top", command=lambda:master.frameSwitcher(reportsOptions.ReportsOptionsPage))
        reports_btn.image = reports_img
        reports_btn.place(x=860, y=420)

if __name__ == "__main__":
    MainPage = MainPage()
    MainPage.mainloop()