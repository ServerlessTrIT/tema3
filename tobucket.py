import json
import boto3
"""
Función Lambda que realiza operaciones sobre un bucket
utilizado el SDK (boto3)
"""
def handler(event, context):
    print(event['Records'][0]['s3']['bucket']['name'])
    print(event['Records'][0]['s3']['object']['key'])
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    nameFile = key.split("/")[1]
    print(nameFile)
    
    s3 = boto3.resource('s3')
    s3.Bucket(bucket).download_file(key, '/tmp/'+nameFile)
    s3.Bucket(bucket).upload_file('/tmp/'+nameFile, 'photos-processed/'+nameFile)
    delete = {
        'Objects': [
            {
                'Key': key,
            }
        ]
    }
    response = s3.Bucket(bucket).delete_objects(Delete=delete)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
