import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.membershipCreation as membershipCreation
import lib.borrowBook as borrowBook
import lib.returnBook as returnBook

class LoansOptionsPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Loans Options")
        master.geometry("1366x768")
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")

        # Resize the Image using resize method
        repImg = Image.open("static/loans.png")
        resizedReportsImage= repImg.resize((450,380), Image.ANTIALIAS)
        self.reportImage= ImageTk.PhotoImage(resizedReportsImage)

        # Labels
        backgroundLabel = tk.Label(master, image=self.bg)
        topLabel = tk.Label(master, text = "Select one of the Options below:", \
            borderwidth=2, bg="light sky blue", height = 5, width = 120, justify = "center", relief = "raised")
        loansImageLabel = tk.Label(master, image=self.reportImage, border=0)
        loansTextLabel = tk.Label(master, text = "Loans", bg="black", fg="white")

        # Buttons
        borrowABookButton = tk.Button(master, text = "6. Borrow", height = 5, width = 15, command=lambda:master.frameSwitcher(borrowBook.BorrowPage))
        returnABookButton = tk.Button(master, text = "7. Return", height = 5, width = 15, command=lambda:master.frameSwitcher(returnBook.ReturnPage))
        backToMainMenuButton = tk.Button(master, text = "Back to Main Menu", height = 2, width = 120, command=lambda:master.frameSwitcher(mainPage.MainPage))

        # Text
        borrowABookTextBox = tk.Text(master, height = 6, width = 55)
        borrowABookMsg = "Book Borrowing"
        borrowABookTextBox.insert(tk.END, borrowABookMsg)
        borrowABookTextBox.config(state=tk.DISABLED)

        returnABookTextBox = tk.Text(master, height = 6, width = 55)
        returnABookMsg = "Book Returning"
        returnABookTextBox.insert(tk.END, returnABookMsg)
        returnABookTextBox.config(state=tk.DISABLED)

        # Placings
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)
        topLabel.place(x=140, y=70)
        backToMainMenuButton.place(x=140, y=690)
        loansImageLabel.place(x=140, y=230)
        loansTextLabel.place(x=335, y=575)

        borrowABookButton.place(x=620, y=340)
        borrowABookTextBox.place(x=770, y=340)
        returnABookButton.place(x=620, y=430)
        returnABookTextBox.place(x=770, y=430)

if __name__ == "__main__":
    LoansOptions = LoansOptionsPage()
    LoansOptions.mainloop()
