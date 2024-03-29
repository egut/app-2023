"""
Verify function for Mensa swag 2023
"""
import json

import csv

DELTAGAR_LIST=[]

def get_deltagare ():
    with open("./ListaDeltagareSvar.csv", encoding="utf-8") as csvfile:
        deltagare = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in deltagare:
            DELTAGAR_LIST.append(row)         
 
def correct_answer (medlems_id):
    get_deltagare() 
    for row in DELTAGAR_LIST:
        if medlems_id == row[0]:
            return row[3]
    return "Ingen sådan deltagare"

def hello(event, context):
    """
    :param      event:    The event
    :type       event:    { type_description }
    :param      context:  The context
    :type       context:  { type_description }
    """
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
