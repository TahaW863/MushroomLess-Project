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

#Lambda_handler 0
def lambda_handler(event, context):
    
    if event['httpMethod'] == "POST":
        body = event['body']
        body = json.loads(body)['form_response']['answers']
        ans = which_post(body)
        data_list = []
        #ans
        #where 0 indicates The Text POST is submitted
        #where 1 indicates The Image POST is submitted
        if ans == 0:
            data_list = get_list(body)
            #upload The LIST To The S3
            s3 = boto3.client("s3")
            dat_={}
            dat_['li']=data_list
            filename_='List.json'
            upload_stream=bytes(json.dumps(dat_).encode('UTF-8'))
            s3.put_object(Bucket="data-text-or-image-2020-9-15-7-41", Key=filename_,Body=upload_stream)
        else:
            data_list = get_link(body)
            #upload The Link To The S3
            s3 = boto3.client("s3")
            dat_={}
            dat_['li']=data_list
            filename_='LINK.json'
            upload_stream=bytes(json.dumps(dat_).encode('UTF-8'))
            s3.put_object(Bucket="data-text-or-image-2020-9-15-7-41", Key=filename_,Body=upload_stream)
        return respond("POSTED")

    else:
        #GET For The TEXT
        s3 = boto3.client("s3")
        endpoint_name = 'sagemaker-tensorflow-2020-09-15-04-21-08-261'
        client = boto3.client('runtime.sagemaker', region_name='us-east-1')
        bucket = 'data-text-or-image-2020-9-15-7-41'
        key = 'List.json'
        res = s3.get_object(Bucket=bucket, Key=key)
        content = res['Body']

        jsonObject = json.loads(content.read())
    
        data_list= jsonObject['li']
        data=parse_ans_to_list(data_list)
        
        response = client.invoke_endpoint(EndpointName=endpoint_name, \
                                          Body=json.dumps(data))
        response_body = response['Body']
        ans=json.loads(response_body.read())['outputs']['score']['floatVal']
        return respond(ans)
        
    return respond("unhandled")
    


def which_post(body):
    li = []
    for item in body:
        li.append(item['type'])
        break
    type_filex = li[0]
    num = 0
    if type_filex == 'choice':
        num = 0
    else:
        num = 1
    return num


def get_list(body):
    li = []
    for item in body:
        li.append(item['choice']['label'])
    return li


def get_link(body):
    li = []
    for item in body:
        li.append(item['file_url'])
    return li[0]


def parse_ans_to_list(li):

    lix = ['free', 'close', 'narrow', 'enlarging', 'partial',
            'bell', 'conical', 'flat', 'knobbed', 'sunken',
           'convex', 'buff', 'cinnamon', 'red', 'gray',
           'brown', 'pink', 'green', 'purple',
           'white', 'yellow', 'fibrous', 'grooves',
           'smooth', 'scaly', 'almond', 'creosote',
           'foul', 'anise', 'musty', 'none',
           'pungent', 'spicy', 'fishy',
           'buff', 'red', 'gray', 'chocolate',
           'black', 'brown', 'orange', 'pink',
           'green', 'purple', 'white', 'yellow',
           'missing', 'bulbous', 'club', 'equal',
           'rooted', 'fibrous', 'silky', 'smooth',
           'scaly', 'fibrous', 'silky', 'smooth',
           'scaly', 'buff', 'cinnamon', 'red',
           'gray', 'brown', 'orange', 'pink', 'white',
           'yellow', 'buff', 'cinnamon', 'red',
           'gray', 'brown', 'orange', 'pink', 'white',
           'yellow', 'brown', 'orange', 'white',
           'yellow', 'none', 'one', 'two',
           'evanescent', 'flaring', 'large',
           'none', 'pendant', 'buff',
           'chocolate', 'black', 'brown',
           'orange', 'green', 'purple',
           'white', 'yellow', 'abundant',
           'clustered', 'numerous', 'scattered',
           'several', 'solitary', 'woods',
           'grasses', 'leaves', 'meadows',
           'paths', 'urban', 'waste'
           ]
    data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0]]
    for i in range(0,22):
        for j in range(0, 111):
            if li[i]==lix[j]:
                data[0][j]=1
        
    return data
