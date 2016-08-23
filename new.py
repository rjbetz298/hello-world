import json

json_data = open("C:\Users\RyanRex\Desktop\AllCards.json", "r")
# print type(json_data) type lets you see if it is a file or string
data = json_data.read()

card_dict = json.loads(data)

# lets search through the dict for something?!?

Elephant_List = []
for card_name,card in card_dict.iteritems():
    try:
        for subtype in card["subtypes"]:
            if subtype == "Elephant":
                Elephant_List.append([card_name])
    except KeyError:
        continue #if in a loop it goes to the next item
print Elephant_List
