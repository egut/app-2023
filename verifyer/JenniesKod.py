import csv

Jenkas_list=[]

def get_deltagare ():
    with open("./ListaDeltagareSvar.csv", encoding="utf-8") as csvfile:
        deltagare = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in deltagare:
            Jenkas_list.append(row)         
 
def correct_answer (medlems_id):
    get_deltagare() 
    for row in Jenkas_list:
        if medlems_id == row[0]:
            return row[3]
    return "Ingen sådan deltagare"

print(correct_answer("20100050"))
 

