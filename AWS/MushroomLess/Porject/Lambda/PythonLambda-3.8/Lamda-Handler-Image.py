import json
import boto3


def respond(res):
    return {
        'statusCode': '200',
        'body': json.dumps(res),
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
    }

#Lambda_handler 1
def lambda_handler(event, context):
    
    if event['httpMethod'] == "POST":
        return respond("NOTHING TO POST")

    else:
        #GET For The Image
        s3 = boto3.client("s3")
        endpoint_name = 'sagemaker-tensorflow-2020-09-15-04-21-08-261'
        client = boto3.client('runtime.sagemaker', region_name='us-east-1')
        bucket = 'data-text-or-image-2020-9-15-7-41'
        key = 'List.json'
        res = s3.get_object(Bucket=bucket, Key=key)
        content = res['Body']

        jsonObject = json.loads(content.read())
        return respond(ans)
        
    return respond("unhandled")


  
