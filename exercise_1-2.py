import csv
import time

import sys, operator
data = csv.reader(open('data.csv'),delimiter=',')
tic = time.perf_counter()
sortedlist = sorted(data)   
toc = time.perf_counter() 
print(f"Data sorted in {toc - tic:0.4f} seconds")

with open('NewFile.csv', 'w') as csvfile:
    datawriter = csv.writer(csvfile)
    datawriter.writerow(['rollno', 'name', 'branch','age'])
    tic1 = time.perf_counter()
    for i in range(0, 1000000):
        datawriter.writerow(sortedlist[i])
    toc1 = time.perf_counter()
    print(f"Data written in {toc1 - tic1:0.4f} seconds")

    