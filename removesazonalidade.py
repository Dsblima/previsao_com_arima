import csv
from pandas import read_csv

def GetData(fileName):
    return read_csv(fileName, header=0, parse_dates=[0], index_col=0).values

def RemoverSazonalidade(filename):
    ActualData = GetData(filename+"/"+filename+".csv")
    NumberOfElements = len(ActualData)

    c = csv.writer(open(filename+"/"+filename+"sem.csv", "w"))

    x=0
    ano = 1934

    while(x < NumberOfElements):

        if x+1 < NumberOfElements:            
            c.writerow(ActualData[x]-ActualData[x+1])        
        x+=1

meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]

y=0

while( y< len(meses)):
    RemoverSazonalidade(meses[y])
    y+=1