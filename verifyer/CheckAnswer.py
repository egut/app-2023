# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:19:37 2023
@author: jimg
"""
import json

def get_answer(nr):
    return True

def CheckAnswer(event, context):
    """
    :param      event:    The event
    :type       event:    { type_description }
    :param      context:  The context
    :type       context:  { type_description }
    """
    #fiska ut medlemsnr och svar
    svar = event.get("queryStringParameters")['svar'] #?
    medlemsnr = event.get("queryStringParameters")['medlemsid'] #?
    correctanswer = get_answer(medlemsnr)
    if correctanswer == svar:
        #Skicka id + tid till DB (Del av response?)
        response = json.dumps({"message":"Correct"})
        return response
    else:
        response = json.dumps({"message":"Incorrect"})
        return response
    
