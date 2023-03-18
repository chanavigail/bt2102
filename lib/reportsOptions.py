import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from turtle import color, width

import lib.mainPage as mainPage
import lib.membershipCreation as membershipCreation
import lib.bookSearch as bookSearch
import lib.booksOnLoan as booksOnLoan
import lib.booksOnReservation as booksOnReservation
import lib.membersOutstandingFines as membersOutstandingFines
import lib.booksOnLoanToMember as booksOnLoanToMember

class ReportsOptionsPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Reports Options")
        master.geometry("1366x768")
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")

        # Resize the Image using resize method
        repImg = Image.open("static/reports.png")
        resizedReportsImage= repImg.resize((450,380), Image.ANTIALIAS)
        self.reportImage= ImageTk.PhotoImage(resizedReportsImage)

        # Labels
        backgroundLabel = tk.Label(master, image=self.bg)
        topLabel = tk.Label(master, text = "Select one of the Options below:", \
            borderwidth=2, bg="light sky blue", height = 5, width = 120, justify = "center", relief = "raised")
        reportsImageLabel = tk.Label(master, image=self.reportImage, border=0)
        reportsTextLabel = tk.Label(master, text = "Reports", bg="black", fg="white")

        # Buttons
        bookSearchButton = tk.Button(master, text = "11. Book \nSearch", height = 5, width = 15, command=lambda:master.frameSwitcher(bookSearch.BookSearchPage))
        booksOnLoanButton = tk.Button(master, text = "12. Books on \nLoan", height = 5, width = 15, command=lambda:master.frameSwitcher(booksOnLoan.BooksOnLoanPage))
        booksOnReservationButton = tk.Button(master, text = "13. Books on \nReservation", height = 5, width = 15, command=lambda:master.frameSwitcher(booksOnReservation.BooksOnReservationPage))
        outstandingFinesButton = tk.Button(master, text = "14. Outstanding \nFines", height = 5, width = 15, command=lambda:master.frameSwitcher(membersOutstandingFines.MembersOutstandingFinesPage))
        booksOnLoanSelfButton = tk.Button(master, text = "15. Books on \nLoan to \nMember", height = 5, width = 15, command=lambda:master.frameSwitcher(booksOnLoanToMember.BooksOnLoanToMemberPage))
        backToMainMenuButton = tk.Button(master, text = "Back to Main Menu", height = 2, width = 120, command=lambda:master.frameSwitcher(mainPage.MainPage))

        # Text
        bookSearchTextBox = tk.Text(master, height = 6, width = 55)
        bookSearchMsg = "A member can perform a search on the collection of \nbooks."
        bookSearchTextBox.insert(tk.END, bookSearchMsg)
        bookSearchTextBox.config(state=tk.DISABLED)

        booksOnLoanTextBox = tk.Text(master, height = 6, width = 55)
        booksOnLoanMsg = "This function displays all the books currently on loan to members."
        booksOnLoanTextBox.insert(tk.END, booksOnLoanMsg)

        booksOnReservationTextBox = tk.Text(master, height = 6, width = 55)
        booksOnReservationMsg = "This function displays all the books that members have\nreserved."
        booksOnReservationTextBox.insert(tk.END, booksOnReservationMsg)

        outstandingFinesTextBox = tk.Text(master, height = 6, width = 55)
        outstandingFinesMsg = "This function displays all the outstanding fines issued\nto members."
        outstandingFinesTextBox.insert(tk.END, outstandingFinesMsg)

        booksOnLoanSelfTextBox = tk.Text(master, height = 6, width = 55)
        booksOnLoanSelfMsg = "This function displays all the books a member \nidentified by the membership id has borrowed."
        booksOnLoanSelfTextBox.insert(tk.END, booksOnLoanSelfMsg)

        # Placings
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)
        topLabel.place(x=140, y=70)
        backToMainMenuButton.place(x=140, y=690)
        reportsImageLabel.place(x=140, y=230)
        reportsTextLabel.place(x=335, y=575)

        bookSearchButton.place(x=620, y=200)
        bookSearchTextBox.place(x=770, y=200)

        booksOnLoanButton.place(x=620, y=290)
        booksOnLoanTextBox.place(x=770, y=290)

        booksOnReservationButton.place(x=620, y=380)
        booksOnReservationTextBox.place(x=770, y=380)

        outstandingFinesButton.place(x=620, y=470)
        outstandingFinesTextBox.place(x=770, y=470)

        booksOnLoanSelfButton.place(x=620, y=560)
        booksOnLoanSelfTextBox.place(x=770, y=560)

if __name__ == "__main__":
    ReportOptions = ReportsOptionsPage()
    ReportOptions.mainloop()
