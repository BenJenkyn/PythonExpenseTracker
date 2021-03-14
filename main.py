# I use cat as a short form for category
from database import *
from library import *
import datetime


# from database import *

# Temp list to be put into database later
DBManager = DBManager("ExpenseTracker.db")

def main():
    noCatMsg = "There are no categories to choose from at the moment. Try adding some!"
    expense = ExpenseManager("ExpenseTracker.db")
    selection = -1

    while selection != 0:
        selection = int(input("Please select an option\n"
                              "1. Add Expense\n"
                              "2. View Categories\n"
                              "3. Add Category\n"
                              "4. Delete Category\n"
                              "5. View Expense Report for a Month\n"
                              "6. Average Monthly Expenses\n"
                              "7. Full Report for the month\n"
                              "0. Exit\n"))
        if selection == 1:
            # Adds expenses

            if not expense.viewCategories():
                print(noCatMsg)
                continue
            else:
                category = input("Please Select a category: ")

            valid = False
            for cat in DBManager.viewCategories():
                if cat == category:
                    valid = True
            if not valid:
                print("Invalid Category")
                continue

            name = input("Please enter the name of the expense: ")
            amount = input("Please enter the expense amount: ")
            # print(DBManager.viewCategories())
            # Ensure that the user can only select a valid category

            # Adding the date to the expense object
            year = int(input("Please enter the year of the expense: "))
            month = int(input("Please enter the numerical month of the expense: "))
            day = int(input("Please enter the day of the expense: "))

            expense.addExpense(name, amount, year, month, day, category)

            """
            doesRepeat = input("Does it repeat? (y/n) ")
            repeat = False
            if input == "y":
                repeat = True

            newExpense = Expense(name, amount, category, date)
            newExpense.isRepeating(repeat)

            DBManager.addExpense(newExpense)
            """
        elif selection == 2:
            # Lists Categories
            expense.viewCategories()

        elif selection == 3:
            # Adds Categories

            name = input("Please enter a category name: ")
            expense.addCategory(name)
            """
            category = Category(name)
            
            if DBManager.checkCategory(category.catName):
                print("A category with that name already exists")
            else:
                DBManager.addCategory(category)
                print("Category successfully added!")
            """

        elif selection == 4:
            # Delete Category
            expense.viewCategories()
            print()
            toDel = input("Please Type the name of the category you would like to delete from the above list: ")
            expense.deleteCategory(toDel)
            # Come back to this to make sure that deletion works properly

        elif selection == 5:
            # Average Expense for a month
            monthNum = input("Please enter the number of the month you would like to check (1-12):")
            expense.monthExpense(monthNum)

        elif selection == 6:
            year = input("Please enter the year you would like to check:")
            expense.avgMonthlyExpenses(year)

        elif selection == 7:
            monthNum = input("Please enter the number of the month you would like to check (1-12):")
            year = input("Please enter the year you would like to check:")
            expense.report(monthNum, year)


if __name__ == '__main__':
    main()
