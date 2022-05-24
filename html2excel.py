# Importing pandas
# Needed installs are:
# lxml
# pandas
# openpyxl
import pandas as pd
import lxml
from openpyxl import load_workbook, Workbook
from time import sleep

# The webpage URL whose table we want to extract
wb = Workbook()
name = input("Name what you want the file to be named. Do not add the .xlsx extension: ")
url = input("Insert a url to have the table taken from: ")
tablenum = input("Which table on the page do you want to convert? IMPORTANT: SUBTRACT 1 FROM THE NUMBER: ")
tableint = int(tablenum)
# Assign the table data to a Pandas dataframe
table = pd.read_html(url, skiprows=1)[tableint]

# Print the dataframe
print("Table found! This table will be sent to the file 'data.xlsx'")
print(table)
print("\n \n \n \n")
print("Removing extra rows from table.")
table = table.drop(table.index[[0]])
sleep(2)
print(table)
table.to_excel(name + ".xlsx")
