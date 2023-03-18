import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from turtle import color, width
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import lib.membershipsOptions as membershipsOptions
import lib.membershipCreation as membershipCreation
import lib.membershipUpdate as membershipUpdate
import lib.sql_database as sql_db
import re


class MembershipUpdateDetailsPage(tk.Frame):
    def __init__(self, master, ):
        ttk.Frame.__init__(self, master)
        database = sql_db.Database()
        master.title("Membership Update")
        master.geometry("1366x768")

        # Generic function for two functions in one button
        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func

        def update_member():
            id = memberIDEntry.get()
            name = nameEntry.get()
            faculty = facultyEntry.get()
            phoneNum = phoneNumberEntry.get()
            email = emailAddressEntry.get()

            database.updateMember((name, faculty, phoneNum, email, id))
            return success_popup()

        def checkFirst():
            regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            regexNum = r'^\d+$'
            name = nameEntry.get()
            faculty = facultyEntry.get()
            phoneNum = phoneNumberEntry.get()
            email = emailAddressEntry.get()

            # Check empty fields
            if(len(name) < 1 or len(faculty) < 1 or len(phoneNum) < 1 or len(email) < 1):
                return fail_popup("empty")

            # Check phone number
            if(len(phoneNumberEntry.get()) != 8 or not re.fullmatch(regexNum, phoneNum)):
                return fail_popup("HP")

            # Check email
            if(not re.fullmatch(regexEmail, email)):
                return fail_popup("email")

            return confirm_popup()
        
        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Membership Update Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="red")

            errorLabel = tk.Label(pop, text="Error!", bg="red", fg="yellow")
            errorLabel.place(x=130, y=70)

            if (reason == "empty"):
                statusLabel = tk.Label(pop, text="Missing or \nIncomplete fields!", bg="red", fg="yellow")
                statusLabel.place(x=90, y=150)
            elif (reason == "HP"):
                statusLabel = tk.Label(pop, text="Phone number must consist of 8 digits only!", bg="red", fg="yellow")
                statusLabel.place(x=15, y=150)
            elif (reason == "email"):
                statusLabel = tk.Label(pop, text="Please use correct email format!", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)

            backButton = tk.Button(pop, text="Back to \nUpdate \nFunction", bg="red", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)

        # Confirm popup screen
        def confirm_popup():
            pop = tk.Toplevel(master)
            pop.title("Membership Updated Details")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            msgLabel = tk.Label(pop, text="Please Confirm Details to Be Correct", font='Helvetica 12 bold', bg="light green")
            msgLabel.place(x=50, y=10)

            memberIDLabel = tk.Label(pop, text="Member ID", bg="light green")
            memberIDLabel.place(x=10, y=50)
            memberIDEntryLabel = tk.Label(pop, text=memberIDEntry.get(), bg="light green")
            memberIDEntryLabel.place(x=110, y=50)

            nameLabel = tk.Label(pop, text="Name", bg="light green")
            nameLabel.place(x=10, y=80)
            nameEntryLabel = tk.Label(pop, text=nameEntry.get(), bg="light green")
            nameEntryLabel.place(x=110, y=80)

            facultyLabel = tk.Label(pop, text="Faculty", bg="light green")
            facultyLabel.place(x=10, y=110)
            facultyEntryLabel = tk.Label(pop, text=facultyEntry.get(), bg="light green")
            facultyEntryLabel.place(x=110, y=110)

            hpLabel = tk.Label(pop, text="Phone Number", bg="light green")
            hpLabel.place(x=10, y=140)
            hpEntryLabel = tk.Label(pop, text=phoneNumberEntry.get(), bg="light green")
            hpEntryLabel.place(x=110, y=140)

            emailLabel = tk.Label(pop, text="Email Address", bg="light green")
            emailLabel.place(x=10, y=170)
            emailEntryLabel = tk.Label(pop, text=emailAddressEntry.get(), bg="light green")
            emailEntryLabel.place(x=110, y=170)

            confirmButton = tk.Button(pop, text="Confirm \nUpdate", bg="light green", width=12, command=combine_funcs(pop.destroy, update_member))
            confirmButton.place(x=30, y= 240)

            backButton = tk.Button(pop, text="Back to \nUpdate Function", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=160, y= 240)

        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Membership Update Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="ALS Membership Updated.", bg="light green")
            statusLabel.place(x=70, y=150)

            # 2 commands in 1 button
            createAnotherMemberButton = tk.Button(pop, text="Create Another \nMember\n", bg="light green", width=12, \
                command=combine_funcs(pop.destroy, lambda: master.frameSwitcher(membershipCreation.MembershipCreationPage)))
            createAnotherMemberButton.place(x=40, y= 240)

            backButton = tk.Button(pop, text="Back to \nUpdate \nFunction", bg="light green", width=10, command=pop.destroy)
            backButton.place(x=170, y= 240)

        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Membership Update Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="red")

            errorLabel = tk.Label(pop, text="Error!", bg="red", fg="yellow")
            errorLabel.place(x=120, y=70)

            if (reason == "empty"):
                statusLabel = tk.Label(pop, text="Missing or \nIncomplete fields!", bg="red", fg="yellow")
                statusLabel.place(x=80, y=150)
            elif (reason == "HP"):
                statusLabel = tk.Label(pop, text="Phone number must consist of 8 digits only!", bg="red", fg="yellow")
                statusLabel.place(x=10, y=150)
            elif (reason == "email"):
                statusLabel = tk.Label(pop, text="Please use correct email format!", bg="red", fg="yellow")
                statusLabel.place(x=50, y=150)

            backButton = tk.Button(pop, text="Back to \nUpdate \nFunction", bg="red", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)
        
        # Setup background
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text = "Please Enter Requested Information Below:", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        memberIDLabel = tk.Label(master, text = "Membership ID", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        memberIDEntry = tk.Entry(master, textvariable = "A unique alphanumeric ID that distinguishes every member", width = 60, state="disabled") # Not changeable for update
        memberIDLabel.place(x=320, y=180)
        memberIDEntry.place(x=470, y=185)
        memberIDEntry.delete(0, END)

        nameLabel = tk.Label(master, text = "Name", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        nameEntry = tk.Entry(master, textvariable = "Enter member's name", width = 60)
        nameLabel.place(x=320, y=230)
        nameEntry.place(x=470, y=235)
        nameEntry.delete(0, END)

        facultyLabel = tk.Label(master, text = "Faculty", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        facultyEntry = tk.Entry(master, textvariable = "eg. Computing, Engineering, Science, etc", width = 60)
        facultyLabel.place(x=320, y=280)
        facultyEntry.place(x=470, y=285)
        facultyEntry.delete(0, END)

        phoneNumberLabel = tk.Label(master, text = "Phone number", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        phoneNumberEntry = tk.Entry(master, textvariable = "eg. 91234567", width = 60)
        phoneNumberLabel.place(x=320, y=330)
        phoneNumberEntry.place(x=470, y=335)
        phoneNumberEntry.delete(0, END)

        emailAddressLabel = tk.Label(master, text = "Email address", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        emailAddressEntry = tk.Entry(master, textvariable = "eg. ALSuser@als.edu", width = 60)
        emailAddressLabel.place(x=320, y=380)
        emailAddressEntry.place(x=470, y=385)
        emailAddressEntry.delete(0, END)

        # Buttons
        updateButton = tk.Button(master, text = "Update Member", height = 3, width = 15, padx = 5, command=checkFirst)
        updateButton.place(x=470, y=440)

        backButton = tk.Button(master, text = "Back to Update Membership", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(membershipUpdate.MembershipUpdatePage))
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    MembershipUpdateDetails = MembershipUpdateDetailsPage()
    MembershipUpdateDetails.mainloop()
