import json
import boto3
import logging

Row_Get_Path = "/Emp"
Row_Post_Path = "/Emp"
table_name = 'Employee'
client = boto3.client('dynamodb')


def lambda_handler(event, context):
    # body = json.dumps(json.loads(json.dumps(event['body'])))

    emp = {'Emp_ID': {'N': event["Emp_ID"]}
        , 'F_Name': {'S': event['F_Name']}
        , 'L_Name': {'S': event['L_Name']}
        , 'Salary': {'S': event['Salary']}
           }
    # call Insert Item
    res = client.put_item(TableName=table_name, Item=emp)
    body = {
        "Emp_ID": event['Emp_ID'],
        "F_Name": event['F_Name'],
        "Salary": event['Salary']

    }
    #  return {
    # 'statusCode': 200,
    # 'body': json.dumps(body)
    #  }
    return json.dumps(event)

    #   decodedjson=json.loads.event['body']
    #  Emp_ID=decodedjson['Emp_ID']
    #  F_Name=decodedjson['F_Name']
    # L_Name=decodedjson['L_Name']
    #  Salary=decodedjson['Salary']

    # Save_Employee(55,'pompo','koko',1000)

#   decodedjson=json.loads.event['body']
#  Emp_ID=decodedjson['Emp_ID']
#  F_Name=decodedjson['F_Name']
# L_Name=decodedjson['L_Name']
#  Salary=decodedjson['Salary']




