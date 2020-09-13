
import json



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


def lambda_handler(event, context):
    if event['httpMethod'] == "POST":
        body = event['body']
        body = json.loads(body)['form_response']['answers']
        ans = which_post(body)
        data_list = []
        if ans == 0:
            data_list = get_list(body)
            endpoint_name = 'sagemaker-tensorflow-2020-09-13-07-23-38-457'
            client = boto3.client('runtime.sagemaker', region_name='us-east-1')
            data = parse_ans_to_list(data_list)

            response = client.invoke_endpoint(EndpointName=endpoint_name, \
                                              Body=json.dumps(data))
            response_body = response['Body']

            return respond(json.loads(response_body.read())['outputs']['score']['floatVal'])
        else:
            data_list = get_link(body)

            return respond(data_list)

    else:
        return respond("GET")

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
    data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0]]

    lix = ['True','free', 'close', 'narrow', 'enlarging', 'partial',
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

    i = 0
    for item in li:
        is_there = 0
        for o in lix:
            if item == o:
                is_there = 1
                break
        data[0][i] = is_there
        i += 1

    return data


def binary_switch(i, li, st):
    val = 0
    if li[i] == st:
        val = 0
    else:
        val = 1
    return val
licc=[
  "True",
  "attached",
  "close",
  "narrow",
  "enlarging",
  "universal",
  "convex",
  "buff",
  "fibrous",
  "anise",
  "black",
  "rooted",
  "silky",
  "silky",
  "cinnamon",
  "brown",
  "white",
  "one",
  "large",
  "green",
  "clustered",
  "waste"
]
data=parse_ans_to_list(licc)
print(data)