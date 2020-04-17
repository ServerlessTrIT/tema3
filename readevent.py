import json
import boto3

"""
Función Lambda que se ejecuta por evento de un bucket
"""
def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(bucket)
    print(key)

    #documentación oficial: 
    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#object
    s3 = boto3.resource('s3')
    object = s3.Object(bucket, key)
    object.load()
    print(object.last_modified)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
