"""
Verify function for Mensa swag 2023
"""
import json


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
