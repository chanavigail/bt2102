import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.membershipCreation as membershipCreation
import lib.reserveBook as reserveBook
import lib.cancelBook as cancelBook

class ReservationsOptionsPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Reservations Options")
        master.geometry("1366x768")
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")

        # Resize the Image using resize method
        repImg = Image.open("static/reservations.png")
        resizedReportsImage= repImg.resize((450,380), Image.ANTIALIAS)
        self.reportImage= ImageTk.PhotoImage(resizedReportsImage)

        # Labels
        backgroundLabel = tk.Label(master, image=self.bg)
        topLabel = tk.Label(master, text = "Select one of the Options below:", \
            borderwidth=2, bg="light sky blue", height = 5, width = 120, justify = "center", relief = "raised")
        reservationImageLabel = tk.Label(master, image=self.reportImage, border=0)
        reservationTextLabel = tk.Label(master, text = "Reservations", bg="black", fg="white")

        # Buttons
        reserveABookButton = tk.Button(master, text = "8. Reserve a \nBook", height = 5, width = 15, command=lambda:master.frameSwitcher(reserveBook.ReservePage))
        cancelReservationButton = tk.Button(master, text = "9. Cancel \nReservation", height = 5, width = 15, command=lambda:master.frameSwitcher(cancelBook.CancelPage))
        backToMainMenuButton = tk.Button(master, text = "Back to Main Menu", height = 2, width = 120, command=lambda:master.frameSwitcher(mainPage.MainPage))

        # Text
        reserveABookTextBox = tk.Text(master, height = 6, width = 55)
        reserveABookMsg = "Book Reservation"
        reserveABookTextBox.insert(tk.END, reserveABookMsg)
        reserveABookTextBox.config(state=tk.DISABLED)

        cancelReservationTextBox = tk.Text(master, height = 6, width = 55)
        cancelReservationMsg = "Reservations Cancellation"
        cancelReservationTextBox.insert(tk.END, cancelReservationMsg)
        cancelReservationTextBox.config(state=tk.DISABLED)

        # Placings
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)
        topLabel.place(x=140, y=70)
        backToMainMenuButton.place(x=140, y=690)
        reservationImageLabel.place(x=140, y=230)
        reservationTextLabel.place(x=335, y=575)

        reserveABookButton.place(x=620, y=340)
        reserveABookTextBox.place(x=770, y=340)
        cancelReservationButton.place(x=620, y=430)
        cancelReservationTextBox.place(x=770, y=430)

if __name__ == "__main__":
    ReservationsOptions = ReservationsOptionsPage()
    ReservationsOptions.mainloop()
