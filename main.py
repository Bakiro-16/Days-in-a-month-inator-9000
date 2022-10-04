
def jmmjaod():
    print('There are 31 days in '+month+" or 2678400 seconds.")


def asjn():
    print('There are 30 days in '+month+' or 2,592,000 seconds.')


print("Welcome to the Days-in-a-month-inator 9000")
month = input('Please insert the month you want to check the days of --->  ')
if month == "september" or month == 'September' or month == "april" or month == 'April' or month == "june" or month =='June' or month == "november" or month == 'November':
    asjn()
if month == 'january' or month == 'January' or month == "may" or month == "May" or month == "march" or month == "March" or month == "july" or month == "July" or month == "august" or month == "August" or month == "october" or month == "October" or month == "december" or month == "December":
    jmmjaod()
if month == "february" or month == "February":
    print('There are 28 days in February (or 29 if it is a leap year.) or 2,505,600 seconds.')


input('Press Enter to exit')