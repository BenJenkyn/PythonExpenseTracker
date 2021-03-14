from datetime import datetime
from database import *

class Expense:
    def __init__(self, name, amount, year, month, day, catID):
        self.name = name
        self.amount = amount
        self.date = datetime(year, month, day)
        self.catID = catID

    # get id class possibly

    # def getCatID(self, catName):

    def isRepeating(self, repeat):
        if repeat:
            return False
        return True

    def toStr(self):
        return "\tExpense Name: {0}\n" \
               "\tExpense Amount: {1}\n" \
               "\tExpense Date: {2}\n".format(self.name, self.amount, str(self.date.date()))


class Category:
    def __init__(self, catName):
        self.catName = catName
        # self.dataBase = DBManager(dbName)
        self.catID = self.getID()

    def getID(self):
        # 1 is a placeholder
        catID = 1  # self.dataBase.getCategoryID(self.catName)
        return catID


class ExpenseManager:
    def __init__(self, dbName):
        self.dbName = dbName
        self.database = DBManager(dbName)
        self.catList = self.database.viewCategories()
        #self.catList = [Category("Food", dbName), Category("Rent", dbName), Category("Golf", dbName)]
        self.exList = [Expense("Meat", 10, 2020, 9, 15, "Food")]

    def addCategory(self, catName):
        for cat in self.catList:
            if catName == cat.catName:
                print("That category already exists")
                return
        
        print("Category successfully added")

    def viewCategories(self):
        """
        print("Category List:")
        if len(self.catList) == 0:
            print("There are no categories to choose from at the moment. Try adding some!")
        else:
            for i, cat in enumerate(self.catList):
                print(str(i + 1) + ". " + cat.catName)
        """
        dbView = self.database.viewCategories()
        if dbView == []:
            print("There are no categories to choose from at the moment. Try adding some!")
            return False
        else:
            print("Category List:")
            for i, view in enumerate(dbView):
                print(str(i + 1) + ". " + view)
            print()
            return True
        # This function used to return a boolean which will affect some code in the main

    def deleteCategory(self, catName):
        for i, cat in enumerate(self.catList):
            if cat.catName == catName:
                self.catList.pop(i)
                print("Category successfully deleted")
                return
        print("Category does not exist")

    def addExpense(self, name, amount, year, month, day, catName):
        for cat in self.catList:
            if cat.catName == catName:
                # adding the cat name is a placeholder to be replaced by cat.catID
                self.exList.append(Expense(name, amount, year, month, day, catName))
                return
        print("Category could not be found")

    def viewCatExpenses(self, catName):
        # Allows you to view the expenses in a category
        for cat in self.catList:
            if cat.catName == catName:
                for ex in self.exList:
                    # Change name to ID when connecting to database
                    if ex.catID == catName:
                        print(ex.toStr())
                return
        print("Category could not be found")

    def monthExpense(self, monthNum):
        total = 0
        avg = 0
        avgs = []
        if len(self.exList) == 0:
            print("There are no expenses added just yet!")
            return
        for cat in self.catList:
            empty = 0
            print("Category: " + cat.catName)
            for ex in self.exList:
                if cat.catName == ex.catID and ex.date.month == int(monthNum):
                    print(ex.toStr())
                    total += ex.amount
                    empty += 1
            if empty == 0:
                print("There were no {0} expenses this month".format(cat.catName))
        avg = total / 12
        avgs.append(avg)
        return avgs

    def avgMonthlyExpenses(self, year):
        total = 0.00
        catTotal = 0.00
        catAvgs = []
        percents = []

        # Gets the average amount of expenses for the year
        for cat in self.catList:
            print("Average Monthly spending for: " + cat.catName)
            for ex in self.exList:
                if cat.catName == ex.catID and ex.date.year == int(year):
                    total += float(ex.amount)
                    catTotal = ex.amount + catTotal
            catAvg = catTotal / 12
            print("$" + "{:.2f}".format(catAvg))
            catAvgs.append(catAvg)
            catTotal = 0

        avg = (total / 12)
        print("Total annual average: $ {:.2f}".format(avg))

        for i, catAvg in enumerate(catAvgs):
            if catAvg == 0:
                print("The {0} category made up %0 of the total monthly average this year".format(cat.catName))
                percents.append(0)
            else:
                percents.append(100 * (catAvg / avg))
                print("The {0} category made up %{1:.2f} of the total monthly average this year".format(cat.catName,
                                                                                                        percents[i]))
        print()

        return catAvgs

    def report(self, monthNum, year):
        monthAvgs = self.monthExpense(monthNum)
        yearlyAvgs = self.avgMonthlyExpenses(year)

        counter = 0
        while counter < len(monthAvgs) and counter < len(yearlyAvgs):
            if monthAvgs[counter] > yearlyAvgs[counter]:
                print("The average expense for the {0} category was higher this month than usual".format(
                    self.catList[counter].catName))
            elif monthAvgs[counter] < yearlyAvgs[counter]:
                print("The average expense for the {0} category was lower this month than usual".format(
                    self.catList[counter].catName))
            else:
                print("The average expense for the {0} category was the same as the average".format(
                    self.catList[counter].catName))
            counter += 1
        print()
