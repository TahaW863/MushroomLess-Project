import json
import boto3
import numpy as np
import os

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

#another Lambda_handler 1
def lambda_handler(event, context):
    
    if event['httpMethod'] == "GET":
 	s3 = boto3.client("s3")
	endpoint_name = 'ENDPOINT-FOR-THE-IMAGE-CALSSIFIER'

	filename="/tmp/LIST.txt"
        fileObj = s3.get_object(Bucket="S3BucketName", Key=filename)
       	link=fileObj["Body"].read().decode('utf-8')
	dow=#way to download the image locally here
	result=clssify_deployed(dow,calsses)
	return respond(result)
    return("NOICE try")

classes=[#Will be written latter 
]


def classify_deployed(image_file, classes):
    payload = None
    with open(image_file, 'rb') as f:
        payload = f.read()
        payload = bytearray(payload)
    endpoint_name="IMAGE-EndPoint"
    res = client.invoke_endpoint(EndpointName=endpoint_name,
							ContentType='application/x-image',
							Body=payload)
    result = json.loads(res)
    best_prob_index = np.argmax(result)
    return (classes[best_prob_index], result[best_prob_index])