import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.membershipCreation as membershipCreation
import lib.payFine as payFine

class FinesOptionsPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Fines Options")
        master.geometry("1366x768")
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")

        # Resize the Image using resize method
        repImg = Image.open("static/fines.png")
        resizedReportsImage= repImg.resize((450,380), Image.ANTIALIAS)
        self.reportImage= ImageTk.PhotoImage(resizedReportsImage)

        # Labels
        backgroundLabel = tk.Label(master, image=self.bg)
        topLabel = tk.Label(master, text = "Select one of the Options below:", \
            borderwidth=2, bg="light sky blue", height = 5, width = 120, justify = "center", relief = "raised")
        finesImageLabel = tk.Label(master, image=self.reportImage, border=0)
        finesTextLabel = tk.Label(master, text = "Fines", bg="black", fg="white")

        # Buttons
        paymentButton = tk.Button(master, text = "10. Payment", height = 5, width = 15, command=lambda:master.frameSwitcher(payFine.PayFinePage))
        backToMainMenuButton = tk.Button(master, text = "Back to Main Menu", height = 2, width = 120, command=lambda:master.frameSwitcher(mainPage.MainPage))

        # Text
        paymentTextBox = tk.Text(master, height = 6, width = 55)
        paymentMsg = "Fine Payment"
        paymentTextBox.insert(tk.END, paymentMsg)
        paymentTextBox.config(state=tk.DISABLED)

        # Placings
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)
        topLabel.place(x=140, y=70)
        backToMainMenuButton.place(x=140, y=690)
        finesImageLabel.place(x=140, y=230)
        finesTextLabel.place(x=335, y=575)

        paymentButton.place(x=620, y=380)
        paymentTextBox.place(x=770, y=380)

if __name__ == "__main__":
    FinesOptions = FinesOptionsPage()
    FinesOptions.mainloop()
