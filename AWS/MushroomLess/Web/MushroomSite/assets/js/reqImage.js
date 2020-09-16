var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    var myObj = JSON.parse(this.responseText);
    //var x = new String(myObj.body);
    var edibleLookUp=['Agaricus bisporus', 'Horse Musroom',
              'Agrocybe praecox', 'King trumpet Mushroom',
              'Amethyst deceiver', 'Leccinum aurantiacum',
              'Bay Boltete', 'Lurid bolete',
                'Beefasteak fungus', 'Macrolepiota Procera',
'Birch bolete', "Miller",
'Black truffle', "Morchella",
'Bloody Milk cap', 'Neoboletus luridiformis',
"Blusher, Oyster",
'Bovine bolete', 'Pine Bolete',
"Caesar's Mushroom", 'Russula integra',
"Cep", 'Russula vesca',
"Chanterelle", 'Saffron milk cap',
'Charcoal burner', 'Scaly Wood Mushroom',
'Chicken of the Wood', 'Scotch Bonnet',
'Common Puffbal', "shiitake",
'Coprinus comatus', "St. George's Mushroom",
'Dark Cep', 'Stubble rosegill',
'Deceiving bolete', 'Suillus brevipes',
'False saffron milkcap', 'Suillus granulatus',
'Field Mushroom', 'Suillus luteus',
'Fried chicken mushroom', 'Summer cep',
'Funnel Chanterelle', 'The prince',
'Gypsy Mushroom', 'Violet webcap',
"Hedgehog", 'Wood blewit',
'Hen of the Woods', 'Xerocomellus chrysenteron',
'Horn of plenty'];
  var pois=['Bitter beech bolete', 'Lyophyllum connatum',
'Bitter bolete', 'Megacollybia platyphylla',
'Blackening brittlegill', "Mower's Mushroom",
'Blushing bracket', 'Omphalotus olearius',
'Brick cap', 'Panther cap',
'Brown roll-rim', 'Peppery bolete',
'Buttery Collybia', 'Peppery Milkcap',
'Clouded agaric', 'Pine cone mushroom',
'Collared earthstar', 'Plums and Custard',
'Common Stinkhorn', 'Poison Pie',
'Coprinellus micaceus', 'Psathyrella candolleana',
"Dead man's fingers", 'Psilocybe cubensis',
'Deadly dapperling', 'Rooting bolete',
'Deadly webcap', 'Rosy bonnet',
'Death cap', 'Royal fly agaric',
'Destroying angel', 'Russula Ochroleuca',
'Earthy inocybe', 'Sarcosphaera coronaria',
'False champignon', "Satan's bolete",
'False chanterelle', 'Scarlet cup',
'False turkey tail', 'Scarlet hood',
'Fly agaric', 'Smoky polypore',
"Fool's mushroom", 'Spiny puffball',
'Fools webcap', 'Spotted tricholoma',
'Galerina marginata', 'Stinking russula',
'Gassy webcap', 'Sulphur tuft',
'Gemmed Amanita', 'The sickener',
'Goblet funnel cap', 'Tinder fungus',
'Gyromitra esculent', 'Torn fibrecap',
'Honey fungus', 'Trametes versicolor',
'Inky cap', 'Tricholoma scalpturatum',
'Inocybe erubescens', 'Velvet-top fungus',
'Inocybe Rimosa', 'Warted Amanita',
'Lacrymaria lacrymabunda', 'White Saddle',
'Latticed stinkhorn', "Witch's hat",
'Lilac bonnet', 'Woolly  milkcap',
'Lingzhi mushroom', 'Yellow knight',
'Livid entoloma', "Yellow - stainers"]
  var edi="";
  for(var i=0;i<edibleLookUp.length;i++){
    if(myObj[0]==edibleLookUp[i]){
      edi="Edible";
      break;
    }
  }
  for (var i=0;i<pois.length;i++){
     if(myObj[0]==pois[i]){
      edi="Poisonous";
    }
  }

    document.getElementById('tog').innerHTML = edi+" mushroom with name: "+ myObj[0];
    var res=(100*myObj[1]).toFixed(0);
    document.getElementById('score').innerHTML ="Matching percentage: "+res +"%";
    console.log(myObj);
    
  }
};
xmlhttp.open('GET', 'https://rnnwnu5bl9.execute-api.us-east-1.amazonaws.com/default/lambda-1', true);
xmlhttp.send();
//#document.getElementById("toggel").innerHTML = "Tutorix";
