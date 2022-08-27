import json
import boto3
import logging

table_name = 'Employee'
client = boto3.client('dynamodb')


def lambda_handler(event, context):
    emp = {
        'Emp_ID': {'N': event['Emp_ID']}
        , 'F_Name': {'S': event['F_Name']
                     }
    }

    # update Item
    sal=float(event['Salary'])
    new_sal = sal * (0.1)


    response = client.update_item(
    ExpressionAttributeNames={
        '#S': 'Salary',
    },
    ExpressionAttributeValues={
        ':S': {
            'S': str(new_sal),
        },
    },
    Key=emp,
    ReturnValues='ALL_NEW',
    TableName='Employee',
    UpdateExpression='SET  #S = :S',
)

#  return {
# 'statusCode': 200,
# 'body': json.dumps(body)
#  }
    return {"message": "Update employee Successfully",
            "New_Salary": new_sal
            }






