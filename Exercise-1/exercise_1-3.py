"""
// Author: Fahad Kamraan
// Date : 29/01/20
"""

import csv
import time

roll_no = int(input("Enter a roll number to do a linear search:"))
tic = time.perf_counter()
csv_file = csv.reader(open('NewFile.csv', "r"), delimiter=",")
def search():
    for row in csv_file:
        if(str(roll_no) in row):
            return(row)
toc = time.perf_counter()
a = search()
if a != None:
    print(a)
else:
    print("Record not found")
print(f"Record searched in {toc - tic:0.4f} seconds")