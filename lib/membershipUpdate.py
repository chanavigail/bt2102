import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
from PIL import Image, ImageTk
from turtle import color, width
import lib.mainPage as mainPage
import lib.membershipsOptions as membershipsOptions
import lib.membershipUpdateDetails as membershipUpdateDetails
import re
import lib.sql_database as sql_db


class MembershipUpdatePage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        database = sql_db.Database()
        master.title("Membership Update")
        master.geometry("1366x768")

        def checkFirst():
            regexID = r'^[a-zA-Z][0-9]+[a-zA-Z]$'
            id = memberIDEntry.get()

            # Check empty fields
            if(len(id) < 1):
                return fail_popup("empty")

            # Check member id format
            if(not re.fullmatch(regexID, id) or len(id) > 6):
                return fail_popup("IDformat")

            # Check member exists
            checkMemExist = database.checkMemberExist(id)
            if(checkMemExist < 1):
                return fail_popup("IDexist")
            
            master.frameSwitcher(membershipUpdateDetails.MembershipUpdateDetailsPage)
            
        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Membership Creation Status")
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

            backButton = tk.Button(pop, text="Back to \nUpdate \nFunction", bg="red", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)

        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text = "To Update a Member,  Please Enter Membership ID:", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)
        
        memberIDLabel = tk.Label(master, text = "Membership ID", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        memberIDEntry = tk.Entry(master, textvariable = "A unique alphanumeric ID that distinguishes every member", width = 60)
        memberIDLabel.place(x=320, y=350)
        memberIDEntry.place(x=470, y=355)
        memberIDEntry.delete(0, END)

        updateButton = tk.Button(master, text = "Update Member", height = 3, width = 15, padx = 5, command=checkFirst)
        updateButton.place(x=470, y=440)
        backButton = tk.Button(master, text = "Back to Membership Menu", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(membershipsOptions.MembershipsOptionsPage))
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    MembershipUpdate = MembershipUpdatePage()
    MembershipUpdate.mainloop()
