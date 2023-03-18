import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from turtle import color, width
import re
import lib.sql_database as sql_db
import lib.membershipsOptions as membershipsOptions


class MembershipCreationPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        database = sql_db.Database()
        master.title("Membership Creation")
        master.geometry("1366x768")
        
        def register_member():
            regexID = r'^[a-zA-Z][0-9]+[a-zA-Z]$'
            regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            regexNum = r'^\d+$'
            id = memberIDEntry.get()
            name = nameEntry.get()
            faculty = facultyEntry.get()
            phoneNum = phoneNumberEntry.get()
            email = emailAddressEntry.get()

            # Check empty fields
            if(len(id) < 1 or len(name) < 1 or len(faculty) < 1 or len(phoneNum) < 1 or len(email) < 1):
                return fail_popup("empty")

            # Check member id format
            if(not re.fullmatch(regexID, id) or len(id) > 6):
                return fail_popup("IDformat")

            # Check member exists
            checkMemDupes = database.checkMemberExist(id)
            if(checkMemDupes > 0):
                return fail_popup("IDexist")

            # Check phone number
            if(len(phoneNumberEntry.get()) != 8 or not re.fullmatch(regexNum, phoneNum)):
                return fail_popup("HP")

            # Check email
            if(not re.fullmatch(regexEmail, email)):
                return fail_popup("email")

            database.createMember((id, name, faculty, phoneNum, email))
            success_popup()

        # Fail popup screen
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
                statusLabel = tk.Label(pop, text="Member already exists!", bg="red", fg="yellow")
                statusLabel.place(x=70, y=150)
            elif (reason == "HP"):
                statusLabel = tk.Label(pop, text="Phone number must consist of 8 digits only!", bg="red", fg="yellow")
                statusLabel.place(x=15, y=150)
            elif (reason == "email"):
                statusLabel = tk.Label(pop, text="Please use correct email format!", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)

            backButton = tk.Button(pop, text="Back to \nCreate \nFunction", bg="red", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)
            
        # Success popup screen
        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Membership Creation Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="ALS Membership created.", bg="light green")
            statusLabel.place(x=70, y=150)

            backButton = tk.Button(pop, text="Back to \nCreate \nFunction", bg="light green", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)
        
        # Background setup
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        # Labels
        topLabel = tk.Label(master, text = "To create member, please enter requested information below:", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        memberIDLabel = tk.Label(master, text = "Membership ID", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        nameLabel = tk.Label(master, text = "Name", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        facultyLabel = tk.Label(master, text = "Faculty", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        phoneNumberLabel = tk.Label(master, text = "Phone number", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        emailAddressLabel = tk.Label(master, text = "Email address", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")

        # Entry
        memberIDEntry = tk.Entry(master, textvariable = "A unique alphanumeric ID that distinguishes every member", width = 60)
        nameEntry = tk.Entry(master, textvariable = "Enter member's name", width = 60)
        facultyEntry = tk.Entry(master, textvariable = "eg. Computing, Engineering, Science, etc", width = 60)
        phoneNumberEntry = tk.Entry(master, textvariable = "eg. 91234567", width = 60)
        emailAddressEntry = tk.Entry(master, textvariable = "eg. ALSuser@als.edu", width = 60)

        # Buttons
        createButton = tk.Button(master, text = "Create member", height = 3, width = 15, padx = 5, command=register_member)
        backButton = tk.Button(master, text = "Back to Membership Menu", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(membershipsOptions.MembershipsOptionsPage))

        # Placings
        topLabel.place(x=140, y=70)

        memberIDLabel.place(x=320, y=180)
        memberIDEntry.place(x=470, y=185)
        memberIDEntry.delete(0, END)

        nameLabel.place(x=320, y=230)
        nameEntry.place(x=470, y=235)
        nameEntry.delete(0, END)

        facultyLabel.place(x=320, y=280)
        facultyEntry.place(x=470, y=285)
        facultyEntry.delete(0, END)

        phoneNumberLabel.place(x=320, y=330)
        phoneNumberEntry.place(x=470, y=335)
        phoneNumberEntry.delete(0, END)

        emailAddressLabel.place(x=320, y=380)
        emailAddressEntry.place(x=470, y=385)
        emailAddressEntry.delete(0, END)

        createButton.place(x=470, y=440)
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    MembershipCreation = MembershipCreationPage()
    MembershipCreation.mainloop()
