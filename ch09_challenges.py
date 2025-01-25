import os
import csv

##filepath = 'C:\\Users\\benja\\computing\\python\\the-self-taught-programmer\\pyfile1.py'
##with open(filepath,'r') as f:
##    print(f.read())
##    

##savings = input("How much money have you got? ")
##with open("savings.txt","w") as f:
##    f.write(savings)

##filecontents = []
##with open("savings.txt","r") as f:
##    filecontents.append(f.read())
##
##print(filecontents[0])

listoflists = [["Top Gun","Risky Business","Minority Report"],
               ["Titanic","The Revenant","Inception"],
               ["Training Day","Man On Fire","Flight"]
               ]

##with open("listoflists.csv","w",newline="") as f:
##    w = csv.writer(f,delimiter=",")
##    for eachlist in listoflists:
##        w.writerow([eachlist])

with open("listoflists.csv","r") as f:
    r = csv.reader(f,delimiter=",")        
    for row in r:
        print(",".join(row))
        
