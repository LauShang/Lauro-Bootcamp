import os

import csv

budget= os.path.join('budget_data.csv')

date=[]
pnl=[]

with open(budget, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    # next(csvreader,None) #Skip headers
    for row in csvreader:
        date.append(row[0])
        pnl.append(row[1])

tmonths=len(date) # primer punto

total=0.0
for number in pnl:
    total = total + float(number)

sumat=total #sum totales punto 2

g =0
l=0
prev = int(pnl[0])
net_change=[]
for cambio in pnl:
    cambio_neto = int(cambio) - int(prev)
    prev = cambio
    net_change = net_change + [cambio_neto]

    if cambio_neto > g:
        g = cambio_neto
    
    if cambio_neto < l:
        l = cambio_neto

average = sum(net_change)/(len(net_change)-1)
average ="{:.2f}".format(average)

#calcular el índice para el nombre
gmonth = net_change.index(g)
lmonth = net_change.index(l)

gdate = date[gmonth]
ldate = date[lmonth]
#mensaje final

output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {tmonths}\n"
    f"Total : ${sumat}\n"
    f"Average Change: {average}\n"
    f"Greatest Increase in Profits: {gdate} ({g})\n"
    f"Greatest Decrease in Profits: {ldate} ({l})\n"

)
print(output)
final = open("ResultadoPyBank.txt","a")
final.write(output)
final.close()
