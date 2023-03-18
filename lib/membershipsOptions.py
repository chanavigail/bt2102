import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.membershipCreation as membershipCreation
import lib.membershipDeletion as membershipDeletion
import lib.membershipUpdate as membershipUpdate

class MembershipsOptionsPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        master.title("Memberships Options")
        master.geometry("1366x768")
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")

        # Resize the Image using resize method
        repImg = Image.open("static/membership.png")
        resizedReportsImage= repImg.resize((450,380), Image.ANTIALIAS)
        self.reportImage= ImageTk.PhotoImage(resizedReportsImage)

        # Labels
        backgroundLabel = tk.Label(master, image=self.bg)
        topLabel = tk.Label(master, text = "Select one of the Options below:", \
            borderwidth=2, bg="light sky blue", height = 5, width = 120, justify = "center", relief = "raised")
        membershipsImageLabel = tk.Label(master, image=self.reportImage, border=0)
        membershipsTextLabel = tk.Label(master, text = "Membership", bg="black", fg="white")

        # Buttons
        creationButton = tk.Button(master, text = "1. Creation", height = 5, width = 15, command=lambda:master.frameSwitcher(membershipCreation.MembershipCreationPage))
        deletionButton = tk.Button(master, text = "2. Deletion", height = 5, width = 15, command=lambda:master.frameSwitcher(membershipDeletion.MembershipDeletionPage))
        updateButton = tk.Button(master, text = "3. Update", height = 5, width = 15, command=lambda:master.frameSwitcher(membershipUpdate.MembershipUpdatePage))
        backToMainMenuButton = tk.Button(master, text = "Back to Main Menu", height = 2, width = 120, command=lambda:master.frameSwitcher(mainPage.MainPage))

        # Text
        creationTextBox = tk.Text(master, height = 6, width = 55)
        creationMsg = "Membership creation"
        creationTextBox.insert(tk.END, creationMsg)
        creationTextBox.config(state=tk.DISABLED)

        deletionTextBox = tk.Text(master, height = 6, width = 55)
        deletionMsg = "Membership deletion"
        deletionTextBox.insert(tk.END, deletionMsg)
        deletionTextBox.config(state=tk.DISABLED)

        updateTextBox = tk.Text(master, height = 6, width = 55)
        updateMsg = "Membership update"
        updateTextBox.insert(tk.END, updateMsg)
        updateTextBox.config(state=tk.DISABLED)

        # Placings
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)
        topLabel.place(x=140, y=70)
        backToMainMenuButton.place(x=140, y=690)
        membershipsImageLabel.place(x=140, y=230)
        membershipsTextLabel.place(x=335, y=575)

        creationButton.place(x=620, y=290)
        creationTextBox.place(x=770, y=290)

        deletionButton.place(x=620, y=380)
        deletionTextBox.place(x=770, y=380)

        updateButton.place(x=620, y=470)
        updateTextBox.place(x=770, y=470)

if __name__ == "__main__":
    MembershipsOptions = MembershipsOptionsPage()
    MembershipsOptions.mainloop()
