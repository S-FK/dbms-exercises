"""
// Author: Fahad Kamraan
// Date : 29/01/20
"""

# importing required libraries
import random
import csv
import names
import time

def gen_data():
    a = random.sample(range(1, 1000001),1)
    datawriter.writerow([a[0], names.get_first_name(), random.choice(['CSE', 'ECE', 'Mech','EEE', 'Civil']), random.randint(16,22)])

with open('data.csv', 'w') as csvfile:
    datawriter = csv.writer(csvfile)
    datawriter.writerow(['rollno', 'name', 'branch','age'])
    tic = time.perf_counter()
    for i in range(0,1000001):
        gen_data()
    toc = time.perf_counter()
    print(f"Data created in {toc - tic:0.4f} seconds")



