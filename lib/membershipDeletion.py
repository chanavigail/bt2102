import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from turtle import color, width
from tkinter.constants import BOTH, CENTER, DISABLED, END, LEFT, NORMAL
import lib.mainPage as mainPage
import lib.membershipsOptions as membershipsOptions
import re
import lib.sql_database as sql_db


class MembershipDeletionPage(tk.Frame):
    def __init__(self,master):
        ttk.Frame.__init__(self, master)
        database = sql_db.Database()
        master.title("Membership Deletion")
        master.geometry("1366x768")

        # Generic function for two functions in one button

        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func

        def deleteMember():
            id = memberIDEntry.get()
            database.deleteMember(id)
            return success_popup()

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
            
            # Check loan before deletion
            checkLoan = database.checkLoansQty(id)
            if(checkLoan > 0):
                return fail_popup("loan")

            # Check reservation before deletion
            checkReservation = database.checkReservationsQty(id)
            if(checkReservation > 0):
                return fail_popup("rsv")
            
            # Check fine owed before deletion
            checkFineAmt = database.getFineAmount(id)
            if(checkFineAmt > 0):
                return fail_popup("fine")

            return confirm_popup()

        def fail_popup(reason):
            pop = tk.Toplevel(master)
            pop.title("Membership Deletion Status")
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
            elif (reason == "loan"):
                statusLabel = tk.Label(pop, text="Member has loans.\nPlease return books before deletion.", bg="red", fg="yellow")
                statusLabel.place(x=30, y=150)
            elif (reason == "rsv"):
                statusLabel = tk.Label(pop, text="Member has reservations.\nPlease cancel reservations before deletion.", bg="red", fg="yellow")
                statusLabel.place(x=20, y=150)
            elif (reason == "fine"):
                statusLabel = tk.Label(pop, text="Member has outstanding fines.\nPlease pay the fines before deletion.", bg="red", fg="yellow")
                statusLabel.place(x=40, y=150)

            backButton = tk.Button(pop, text="Back to \nDelete \nFunction", bg="red", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)

        def confirm_popup():
            pop = tk.Toplevel(master)
            pop.title("Membership Creation Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")
            
            id = memberIDEntry.get()

            msgLabel = tk.Label(pop, text="Please Confirm Details to Be Correct", font='Helvetica 12 bold', bg="light green")
            msgLabel.place(x=50, y=10)

            memberIDLabel = tk.Label(pop, text="Member ID", bg="light green")
            memberIDLabel.place(x=10, y=50)
            memberIDDataLabel = tk.Label(pop, text=id, bg="light green")
            memberIDDataLabel.place(x=130, y=50)

            name = database.getMemberName(id)
            nameLabel = tk.Label(pop, text="Name", bg="light green")
            nameLabel.place(x=10, y=80)
            nameDataLabel = tk.Label(pop, text=name, bg="light green")
            nameDataLabel.place(x=130, y=80)

            faculty = database.getMemberFaculty(id)
            facultyLabel = tk.Label(pop, text="Faculty", bg="light green")
            facultyLabel.place(x=10, y=110)
            facultyDataLabel = tk.Label(pop, text=faculty, bg="light green")
            facultyDataLabel.place(x=130, y=110)

            num = database.getMemberNo(id)
            hpLabel = tk.Label(pop, text="Phone Number", bg="light green")
            hpLabel.place(x=10, y=140)
            hpDataLabel = tk.Label(pop, text=num, bg="light green")
            hpDataLabel.place(x=130, y=140)

            email = database.getMemberEmail(id)
            emailLabel = tk.Label(pop, text="Email Address", bg="light green")
            emailLabel.place(x=10, y=170)
            emailDataLabel = tk.Label(pop, text=email, bg="light green")
            emailDataLabel.place(x=130, y=170)

            confirmButton = tk.Button(pop, text="Confirm \nDeletion", bg="light green", width=12, command=combine_funcs(pop.destroy, deleteMember))
            confirmButton.place(x=30, y= 240)

            backButton = tk.Button(pop, text="Back to \nDelete Function", bg="light green", width=12, command=pop.destroy)
            backButton.place(x=160, y= 240)

        def success_popup():
            pop = tk.Toplevel(master)
            pop.title("Membership Deletion Status")
            pop.geometry("300x300")
            pop.geometry("+550+200")
            pop.config(bg="light green")

            successLabel = tk.Label(pop, text="Success!", bg="light green")
            successLabel.place(x=120, y=70)

            statusLabel = tk.Label(pop, text="ALS Membership deleted.", bg="light green")
            statusLabel.place(x=70, y=150)

            backButton = tk.Button(pop, text="Back to \nDelete \nFunction", bg="light green", width=10, command=pop.destroy)
            backButton.place(x=100, y= 230)
        
        self.bg = tk.PhotoImage(file="static/librarybg.png")
        backgroundLabel = tk.Label(master, image = self.bg)
        backgroundLabel.place(x = 0, y = 0, relwidth=1, relheight=1)

        topLabel = tk.Label(master, text = "To Delete Member,  Please Enter Membership ID:", \
            borderwidth=2, background="teal", height = 5, width = 120, justify = "center", relief = "raised")
        topLabel.place(x=140, y=70)

        memberIDLabel = tk.Label(master, text = "Membership ID", height = 2, width = 15, borderwidth=2, relief="solid", bg="cyan")
        memberIDEntry = tk.Entry(master, textvariable = "A unique alphanumeric ID that distinguishes every member", width = 60)
        memberIDLabel.place(x=320, y=350)
        memberIDEntry.place(x=470, y=355)
        memberIDEntry.delete(0, END)

        deleteButton = tk.Button(master, text = "Delete Member", height = 3, width = 15, padx = 5, command=checkFirst)
        deleteButton.place(x=470, y=440)
        backButton = tk.Button(master, text = "Back to Membership Menu", height = 3, width = 20, padx = 5, command=lambda:master.frameSwitcher(membershipsOptions.MembershipsOptionsPage))
        backButton.place(x=750, y=440)

if __name__ == "__main__":
    MembershipDeletion = MembershipDeletionPage()
    MembershipDeletion.mainloop()
