from database import *
from library import *

test = ExpenseManager("ExpenseTracker.db")
data = DBManager("ExpenseTracker.db")
"""
test.addCategory("cat")
test.addCategory("cat2")
test.addCategory("cat3")
test.addExpense("cheese", 23, 2020, 3, 16, "cat")
test.addExpense("panzer", 2, 2020, 3, 16, "cat2")
test.addExpense("Spaghetti", 2, 2020, 3, 16, "cat2")
test.addExpense("fun", 10, 2020, 6, 16, "cat2")
test.addExpense("soup", 2, 2020, 5, 16, "cat3")
#test.viewCatExpenses("test")
"""
#test.monthExpense(3)
#test.avgMonthlyExpenses(2020)
print(data.viewCategories())
#test.report(3, 2020)