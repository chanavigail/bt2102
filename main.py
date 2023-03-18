import tkinter as tk
from lib.mainPage import MainPage
from lib.booksOnLoan import BooksOnLoanPage
from lib.booksOnLoanToMember import BooksOnLoanToMemberPage
from lib.membershipCreation import MembershipCreationPage
from lib.membershipDeletion import MembershipDeletionPage
from lib.membershipUpdate import MembershipUpdatePage
from lib.membershipUpdateDetails import MembershipUpdateDetailsPage
from lib.borrowBook import BorrowPage
from lib.returnBook import ReturnPage
from lib.bookAcquisition import BookAcquisitionPage
from lib.bookWithdrawal import BookWithdrawalPage
from lib.reserveBook import ReservePage
from lib.cancelBook import CancelPage
from lib.payFine import PayFinePage
from lib.bookSearch import BookSearchPage

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = None
        self.frameSwitcher(MainPage)

    def frameSwitcher(self, frame_class):
        newFrame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = newFrame
        self.frame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
