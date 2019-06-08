import os

import csv

election_file = os.path.join('election_data.csv')

voter_id=[]
country=[]
candidate=[]

with open(election_file,newline="") as csvfile:
    election= csv.reader(csvfile,delimiter=",")
    header=next(election)
    for row in election:
        voter_id.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

tvotes=len(voter_id) # número total de votos
candidates_name=set(candidate)
CNL=list(candidates_name) #almacena nombres de los candidatos
C1=0
C2=0
C3=0
C4=0

for v in candidate:
    if v == CNL[0]:
        C1= C1 + 1
    elif v == CNL[1]:
        C2=C2+1
    elif v == CNL[2]:
        C3=C3+1
    else:
        C4=C4+1

##determinar ganador

winner=[] #almacena total de votos por candidato

winner.append(C1)
winner.append(C2)
winner.append(C3)
winner.append(C4)
w=0
for x in winner:
    if x > w:
        c_winner=x
        w=x

ganadori=winner.index(w)
ganador=CNL[ganadori] # determina ganador


p_c1="{:.2f}".format(C1/int(tvotes)*100)
p_c2="{:.2f}".format(C2/int(tvotes)*100)
p_c3="{:.2f}".format(C3/int(tvotes)*100)
p_c4="{:.2f}".format(C4/int(tvotes)*100)


Output1=(
    f"\nElection Results\n"
    f"--------------------\n"
    f"Total Votes: {tvotes}\n"
    f"--------------------\n"
    f"{CNL[0]}: {p_c1}% ({C1})\n"
    f"{CNL[1]}: {p_c2}% ({C2})\n" 
    f"{CNL[2]}: {p_c3}% ({C3})\n"
    f"{CNL[3]}: {p_c4}% ({C4})\n" 
    f"--------------------\n"
    f"Winner: {ganador}\n"
    f"--------------------\n"
)
print(Output1)

final = open("ResultadoPyPoll.txt","a")
final.write(Output1)
final.close()

