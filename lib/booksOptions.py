import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.membershipCreation as membershipCreation
import lib.bookAcquisition as bookAcquisition
import lib.bookWithdrawal as bookWithdrawal

class BooksOptionsPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Books Options")
        master.geometry("1366x768")
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")

        # Resize the Image using resize method
        repImg = Image.open("static/books.png")
        resizedReportsImage= repImg.resize((450,380), Image.ANTIALIAS)
        self.reportImage= ImageTk.PhotoImage(resizedReportsImage)

        # Labels
        backgroundLabel = tk.Label(master, image=self.bg)
        topLabel = tk.Label(master, text = "Select one of the Options below:", \
            borderwidth=2, bg="light sky blue", height = 5, width = 120, justify = "center", relief = "raised")
        booksImageLabel = tk.Label(master, image=self.reportImage, border=0)
        booksTextLabel = tk.Label(master, text = "Books", bg="black", fg="white")

        # Buttons
        acquisitionButton = tk.Button(master, text = "4. Acquisition", height = 5, width = 15, command=lambda:master.frameSwitcher(bookAcquisition.BookAcquisitionPage))
        withdrawalButton = tk.Button(master, text = "5. Withdrawal", height = 5, width = 15, command=lambda:master.frameSwitcher(bookWithdrawal.BookWithdrawalPage))
        backToMainMenuButton = tk.Button(master, text = "Back to Main Menu", height = 2, width = 120, command=lambda:master.frameSwitcher(mainPage.MainPage))

        # Text
        acquisitionTextBox = tk.Text(master, height = 6, width = 55)
        acquisitionMsg = "Book Acquisition"
        acquisitionTextBox.insert(tk.END, acquisitionMsg)
        acquisitionTextBox.config(state=tk.DISABLED)

        withdrawalTextBox = tk.Text(master, height = 6, width = 55)
        withdrawalMsg = "Book Withdrawal"
        withdrawalTextBox.insert(tk.END, withdrawalMsg)
        withdrawalTextBox.config(state=tk.DISABLED)

        # Placings
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)
        topLabel.place(x=140, y=70)
        backToMainMenuButton.place(x=140, y=690)
        booksImageLabel.place(x=140, y=230)
        booksTextLabel.place(x=335, y=575)

        acquisitionButton.place(x=620, y=340)
        acquisitionTextBox.place(x=770, y=340)
        withdrawalButton.place(x=620, y=430)
        withdrawalTextBox.place(x=770, y=430)

if __name__ == "__main__":
    BooksOptions = BooksOptionsPage()
    BooksOptions.mainloop()
