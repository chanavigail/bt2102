from tabnanny import check
import tkinter as tk
import mysql.connector

class Database():
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="Bt2102Sucks.")
        self.c = self.connection.cursor(buffered = True)
        self.c.execute("USE {}".format("bt2102db"))

    ############### membershipCreation checks################
    def createMember(self, memInfo):
        query = ("INSERT INTO librarymembers "
               "(member_id, name, faculty, phone_number, email_address, payment_amount, payment_date)"
               "VALUES (%s, %s, %s, %s, %s, 0, null)")
        self.c.execute(query, memInfo)
        self.connection.commit()

    def checkMemberExist(self, memInfo):
        query = ("SELECT * FROM librarymembers WHERE member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.rowcount
        return result
        
    def checkPhoneNumExist(self, number):
        query = ("SELECT * FROM librarymembers WHERE phone_number = %s")
        self.c.execute(query, (number,))
        result = self.c.rowcount
        return result

    def checkEmailAddressExist(self, email):
        query = ("SELECT * FROM librarymembers WHERE email_address = %s")
        self.c.execute(query, (email,))
        result = self.c.rowcount
        return result
    ############### membershipCreation checks ################

    ############### membershipDelete checks ################
    def deleteMember(self, memInfo):
        query = "DELETE FROM librarymembers WHERE member_id = %s"
        self.c.execute(query, (memInfo,))
        self.connection.commit()
    
    def getMemberName(self, memInfo):
        query = ("SELECT name from librarymembers WHERE member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.fetchone()[0]
        return result
    
    def getMemberFaculty(self, memInfo):
        query = ("SELECT faculty from librarymembers WHERE member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.fetchone()[0]
        return result
    
    def getMemberNo(self, memInfo):
        query = ("SELECT phone_number from librarymembers WHERE member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.fetchone()[0]
        return result
    
    def getMemberEmail(self, memInfo):
        query = ("SELECT email_address from librarymembers WHERE member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.fetchone()[0]
        return result

    def checkLoansQty(self, memInfo):
        query = ("SELECT * from borrowedbooks WHERE member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.rowcount
        return result

    def checkReservationsQty(self, memInfo):
        query = ("SELECT * from reservedbooks WHERE member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.rowcount
        return result
    ############### membershipDelete checks ################

    ############### membershipUpdate checks ################
    def updateMember(self, memInfo):
        query = ("UPDATE librarymembers SET name = %s, faculty = %s, phone_number = %s, email_address = %s WHERE member_id = %s")
        self.c.execute(query, memInfo)
        self.connection.commit()
    ############### membershipUpdate checks ################

    ############### borrowBook checks ################
    def borrowBook(self, bookInfo, memInfo, date):
        query = ("INSERT INTO borrowedbooks(accession_no, member_id, borrow_date) VALUES (%s, %s, CAST(%s as DATE))")
        self.c.execute(query, (bookInfo, memInfo, date))
        self.connection.commit()
    
    def cancelReservation(self, bookInfo, memInfo):
        query = ("DELETE FROM reservedbooks WHERE accession_no = %s AND member_id = %s")
        self.c.execute(query, (bookInfo, memInfo))
        self.connection.commit()
        
    def checkBookExist(self, bookInfo):
        query = ("SELECT * FROM librarybooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.rowcount
        return result
    
    def checkLoanByYou(self, bookInfo, memInfo):
        query = ("SELECT * from borrowedbooks WHERE accession_no = %s AND member_id = %s")
        self.c.execute(query, (bookInfo, memInfo))
        result = self.c.rowcount
        return result

    def checkLoanStatus(self, bookInfo):
        query = ("SELECT * from borrowedbooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.rowcount
        return result
    
    def checkReservedStatus(self, bookInfo):
        query = ("SELECT * from reservedbooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.rowcount
        return result

    def checkReservedOwnStatus(self, bookInfo, memInfo):
        query = ("SELECT * from reservedbooks WHERE accession_no = %s AND member_id = %s")
        self.c.execute(query, (bookInfo, memInfo))
        result = self.c.rowcount
        return result

    def getNumOfLoans(self, memInfo):
        query = ("SELECT * FROM borrowedbooks where member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.rowcount
        return result

    def getNumOfReservations(self, memInfo):
        query = ("SELECT * FROM reservedbooks where member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.rowcount
        return result
    
    def getBookTitle(self, bookInfo):
        query = ("SELECT title from librarybooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.fetchone()[0]
        return result
    
    def getBorrowedDate(self, bookInfo):
        query = ("SELECT borrow_date from borrowedbooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.fetchone()[0]
        return result
    ############### borrowBook checks ################

    ############### returnBook checks ################
    def returnBook(self, bookInfo):
        query = ("DELETE FROM borrowedbooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo, ))
        self.connection.commit()
    ############### returnBook checks ################

    ############### reserveBook checks ################
    def reserveBook(self, bookInfo, memInfo, date):
        query = ("INSERT INTO reservedbooks(accession_no, member_id, reserve_date) VALUES (%s, %s, CAST(%s as DATE))")
        self.c.execute(query, (bookInfo, memInfo, date))
        self.connection.commit()
    ############### reserveBook checks ################

    ############### cancelBook checks ################
    def cancelReservation(self, bookInfo, memInfo):
        query = ("DELETE FROM reservedbooks WHERE accession_no = %s AND member_id = %s")
        self.c.execute(query, (bookInfo, memInfo))
        self.connection.commit()
    ############### cancelBook checks ################
    
    ############### payFine checks ################
    def removeFine(self, memID, date):
        query = ("UPDATE librarymembers SET payment_amount = 0, payment_date = %s WHERE member_id = %s")
        self.c.execute(query, (date, memID))
        self.connection.commit()
        
    def getFineAmount(self, memInfo):
        query = ("SELECT payment_amount FROM librarymembers WHERE member_id = %s")
        self.c.execute(query, (memInfo,))
        result = self.c.fetchone()[0]
        return result
    
    def getBorrowerID(self, bookInfo):
        query = ("SELECT member_id FROM borrowedbooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.fetchone()[0]
        return result

    def addToExistingFine(self, payAmt, memInfo):
        query = ("UPDATE librarymembers SET payment_amount = payment_amount + %s WHERE member_id = %s")
        self.c.execute(query, (payAmt, memInfo))
        self.connection.commit()
    ############### payFine checks ################

    ############### bookAcquisition checks ################
    def addAuthors(self, bookInfo, authorsInfo):
        authors_list = authorsInfo.split(", ")
        query = ("INSERT INTO authors(accession_no, name) VALUES (%s, %s)")
        for author in authors_list:
            self.c.execute(query, (bookInfo, author))
            self.connection.commit()
    
    def addBook(self, bookDetails):
        query = ("INSERT INTO librarybooks(accession_no, isbn, title, publisher, publication_year) VALUES (%s, %s, %s, %s, %s)")
        self.c.execute(query, bookDetails)
        self.connection.commit()

    def getAuthors(self, bookInfo):
        query = ("SELECT * FROM authors WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.fetchall()
        return result
    
    def getISBN(self,bookInfo):
        query = ("SELECT isbn FROM librarybooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.fetchone()[0]
        return result

    def getPublisher(self,bookInfo):
        query = ("SELECT publisher FROM librarybooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.fetchone()[0]
        return result
    
    def getPublishYear(self,bookInfo):
        query = ("SELECT publication_year FROM librarybooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        result = self.c.fetchone()[0]
        return result
    
    def removeBookDetails(self, bookInfo):
        query = ("DELETE FROM librarybooks WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        self.connection.commit()

    def removeAuthors(self, bookInfo):
        query = ("DELETE FROM authors WHERE accession_no = %s")
        self.c.execute(query, (bookInfo,))
        self.connection.commit()
    ############### bookAcquisition checks ################

    def getBookSearch(self, title, author, isbn, publisher, year):
        query = ("SELECT accession_no, title, group_concat(a.name) AS authors, isbn, publisher, publication_year "
                "FROM librarybooks "
                "INNER JOIN authors AS a USING(accession_no) "
                "GROUP BY accession_no ")
        if len(title) > 0:
            query += "HAVING (title LIKE '" + title + " %' OR title LIKE '% " + title +"' or title like '% " \
                + title + " %' or title = '" + title + "')"
        if len(isbn) > 0:
            if len(title) > 0:
                query += " AND "
            else:
                query += " HAVING "
            query += "isbn = '" + isbn + "'"
        if len(publisher) > 0:
            if len(title) + len(isbn) > 0:
                query += " AND "
            else:
                query += " HAVING "
            query += "(publisher LIKE '" + publisher + " %' or publisher LIKE '% " + publisher + "' or publisher LIKE '% " \
                + publisher + " %' or publisher = '" + publisher + "')"
        if len(year) > 0:
            if len(title) + len(isbn) + len(publisher) > 0:
                query += " AND "
            else:
                query += " HAVING "
            query += "publication_year = " + year
        if len(author) > 0:
            if len(title) + len(isbn) + len(publisher) + len(year) > 0:
                query += " AND "
            else:
                query += " HAVING "
            query += "accession_no in (SELECT accession_no FROM authors WHERE name = '" + author + "' or name like '% " \
                + author + "' or name like '" + author + " %' or name like '% " + author + " %')"
        self.c.execute(query)
        results = self.c.fetchall()
        return results

    def getAllReservations(self):
        query = ("SELECT r.accession_no, title, r.member_id, name FROM reservedbooks as r "
                "INNER JOIN librarybooks USING(accession_no) "
                "INNER JOIN librarymembers USING(member_id)")
        self.c.execute(query)
        results = self.c.fetchall()
        return results
    
    def getAllFines(self):
        query = ("SELECT member_id, name, faculty, phone_number, email_address, payment_amount FROM librarymembers "
                "WHERE payment_amount > 0")
        self.c.execute(query)
        results = self.c.fetchall()
        return results

    def getBookOnLoanToMember(self, info):
        query = ("SELECT b.accession_no, l.title, group_concat(a.name), l.isbn, l.publisher, l.publication_year FROM borrowedbooks as b "
                "INNER JOIN authors AS a USING(accession_no) "
                "INNER JOIN librarybooks as l USING(accession_no) "
                "WHERE member_id = %s "
                "GROUP BY accession_no ")
        self.c.execute(query, (info,))
        results = self.c.fetchall()
        return results

    def getBookOnLoan(self):
        query = ("SELECT b.accession_no, l.title, group_concat(a.name), l.isbn, l.publisher, l.publication_year FROM borrowedbooks as b "
                "INNER JOIN authors AS a USING(accession_no) "
                "INNER JOIN librarybooks as l USING(accession_no) "
                "GROUP BY accession_no")
        self.c.execute(query)
        results = self.c.fetchall()
        return results