
import json

json_data = open("AllCards.json","r")
#print type(json_data) type lets you see if it is a file or string
data = json_data.read()

card_dict = json.loads(data)

print card_dict["Air Elemental"]
