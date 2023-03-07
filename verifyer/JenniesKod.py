import csv
def get_deltagare ():
    with open("./ListaDeltagareSvar.csv", encoding="utf-8") as csvfile:
        deltagare = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in deltagare:
            print(row)
    return deltagare
            

#print(deltagare[1])
variabel_deltagare = get_deltagare()
print(variabel_deltagare)

medlems_id = ("20100050")
"""
def correct_answer (medlems_id):
    for row in get_deltagare():
        if (medlems_id == list(0)):
            return (list(3))
    return ("Ingen sådan deltagare")

print(correct_answer())
 
"""
