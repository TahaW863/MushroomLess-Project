import json
import boto3
import urllib3
import base64
import os
import ast
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
    
    s3 = boto3.client("s3")
        
    bucket = 'data-text-or-image-2020-9-15-7-41'
    key = 'LINK.json'
    res = s3.get_object(Bucket=bucket, Key=key)
    content = res['Body']
    jsonObject = json.loads(content.read())
    image_url= jsonObject['li']
    http = urllib3.PoolManager()
    file = http.request('GET',image_url,headers={'Content-Type': 'image/jpeg'})
    res_x=classify_deployed(file.data)
    #print(file.headers)
    return respond(res_x)
        
    
    
def classify_deployed(image_file):
    payload = image_file
    endpoint="IC-MushroomLess-1600254408"
    runtime = boto3.Session().client(service_name='sagemaker-runtime', region_name='us-east-1')
    res = runtime.invoke_endpoint(EndpointName=endpoint, ContentType='application/x-image', Body=payload)
    probs = res['Body'].read().decode("utf-8", errors="replace")
    probs=ast.literal_eval(probs)
    maxIndx=0
    for i in range(0,127):
        if maxIndx < probs[i]:
            maxIndx=probs[i]
    for i in range(0,127):
        if maxIndx == probs[i]:
            maxIndx=i
    return (classes[i], probs[i])


classes=['Agaricus bisporus',
'Agrocybe praecox',
'Amethyst deceiver',
'Bay Boltete',
'Beefasteak fungus',
'Birch bolete',
'Bitter beech bolete',
'Bitter bolete',
'Black truffle',
'Blackening brittlegill',
'Bloody Milk cap',
'Blusher',
'Blushing bracket',
'Bovine bolete',
'Brick cap',
'Brown roll-rim',
'Buttery Collybia',
"Caesar's Mushroom",
'Cep',
'Chanterelle',
'Charcoal burner',
'Chicken of the Wood',
'Clouded agaric',
'Collared earthstar',
'Common Puffbal',
'Common Stinkhorn',
'Coprinellus micaceus',
'Coprinus comatus',
'Dark Cep',
"Dead man's fingers",
'Deadly dapperling',
'Deadly webcap',
'Death cap',
'Deceiving bolete',
'Destroying angel',
'Earthy inocybe',
'False champignon',
'False chanterelle',
'False saffron milkcap',
'False turkey tail',
'Field Mushroom',
'Fly agaric',
"Fool's mushroom",
'Fools webcap',
'Fried chicken mushroom',
'Funnel Chanterelle',
'Galerina marginata',
'Gassy webcap',
'Gemmed Amanita',
'Goblet funnel cap',
'Gypsy Mushroom',
'Gyromitra esculent',
'Hedgehog',
'Hen of the Woods',
'Honey fungus',
'Horn of plenty',
'Horse Musroom',
'Inky cap',
'Inocybe Rimosa',
'Inocybe erubescens',
'King trumpet Mushroom',
'Lacrymaria lacrymabunda',
'Latticed stinkhorn',
'Leccinum aurantiacum',
'Lilac bonnet',
'Lingzhi mushroom',
'Livid entoloma',
'Lurid bolete',
'Lyophyllum connatum',
'Macrolepiota Procera',
'Megacollybia platyphylla',
'Miller',
'Morchella',
"Mower's Mushroom",
'Neoboletus luridiformis',
'Omphalotus olearius',
'Oyster',
'Panther cap',
'Peppery Milkcap',
'Peppery bolete',
'Pine Bolete',
'Pine cone mushroom',
'Plums and Custard',
'Poison Pie',
'Psathyrella candolleana',
'Psilocybe cubensis',
'Rooting bolete',
'Rosy bonnet',
'Royal fly agaric',
'Russula Ochroleuca',
'Russula integra',
'Russula vesca',
'Saffron milk cap',
'Sarcosphaera coronaria',
"Satan's bolete",
'Scaly Wood Mushroom',
'Scarlet cup',
'Scarlet hood',
'Scotch Bonnet',
'Smoky polypore',
'Spiny puffball',
'Spotted tricholoma',
"St. George's Mushroom",
'Stinking russula',
'Stubble rosegill',
'Suillus brevipes',
'Suillus granulatus',
'Suillus luteus',
'Sulphur tuft',
'Summer cep',
'The prince',
'The sickener',
'Tinder fungus',
'Torn fibrecap',
'Trametes versicolor',
'Tricholoma scalpturatum',
'Velvet-top fungus',
'Violet webcap',
'Warted Amanita',
'White Saddle',
"Witch's hat",
'Wood blewit',
'Woolly  milkcap',
'Xerocomellus chrysenteron',
'Yellow knight',
'Yellow-stainers',
'shiitake']
    
 