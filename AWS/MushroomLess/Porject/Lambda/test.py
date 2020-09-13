def parse_ans_to_list(li):
    data = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
             1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
             0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
             0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
             0, 0]]

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
    i=0
    for st in  lix:
        if (i < 5):
            data[0][i] = binary_switch(i, st)
        else:
            data[0][i] = not binary_switch(i, st)
        ++i
    return data
li=[
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
  "leaves"
]
def binary_switch(i, st):
    val = 0
    if li[i] == st:
        val = 0
    else:
        val = 1
    return val
print(parse_ans_to_list(li))
class GET_ans:
    def __init__(self):
        data = 0

    def getdata(self):
        return data

    def setdata(dataC):
        data = dataC


DATA_STATIC = GET_ans()
print DATA_STATIC