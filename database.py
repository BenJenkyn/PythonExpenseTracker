import sqlite3

# Function to connect to the database
def connect(dbName):
    try:
        return sqlite3.connect(dbName)
    except ConnectionError:
        print("Could not connect to the database")
    except:
        print("Unexpected error")


class DBManager:
    def __init__(self, dbName):
        self.dbName = dbName
        self.conn = connect(self.dbName)
        self.curs = connect(self.dbName).cursor()

    # EXPENSE COMMANDS #
    def addExpense(self, expense):
        # Adds to the expense Table
        with self.conn:
            self.curs.execute("""INSERT INTO Expenses (Name, Amount, Repeating, Date, Category) 
                            VALUES (:Name, :Amount, :Repeating, :Date, :Category) 
                            """, {'Name': expense.name,
                                  'Amount': expense.amount,
                                  'Repeating': expense.isRepeating(),
                                  'Date': expense.date,
                                  'Category': expense.category})
            # Figure out how to add category index

    def getCategoryID(self, catName):
        # Gets the category ID for the category name
        # This function is meant to go with the "addExpense" function
        with self.conn:
            catID = self.curs.execute("""SELECT CatPK FROM Categories WHERE Name = (:catName) """, {'catName': catName})
            return catID.fetchone()
            # Figure out how to switch fetchall to int

    def getMonth(self, expense):
        with self.conn:
            self.curs.execute("""SELECT Name FROM Expenses WHERE date LIKE MONTH(:mon)""", {'mon': expense})
            # change this command

    # CATEGORY COMMANDS #

    def addCategory(self, category):
        # Adds to the Category Table
        with self.conn:
            self.curs.execute("""INSERT INTO Categories (Name) 
                            VALUES (:Category) 
                            """, {'Category': category.catName})

    def viewCategories(self):
        # Show the categories
        with self.conn:
            toReturn = []
            dbNames = self.curs.execute("""SELECT Name FROM Categories""")
            catNames = dbNames.fetchall()
            for cat in catNames:
                toReturn.append(str(cat[0]))
            return toReturn

    def checkCategory(self, check):
        with self.conn:
            toCheck = self.viewCategories()
            for cat in toCheck:
                if check == str(cat):
                    return True
        return False

    def deleteCategory(self, category):
        # Deletes a category
        with self.conn:
            self.curs.execute("""DELETE FROM Categories WHERE Name = :cat""", {'cat': category})
