import json
import pprint
file_path = "tweet\sample.json"
list = []
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
    for i in range(len(json_data)):
        name = json_data[i]["title"]
        content = json_data[i]["description"]
        tag = json_data[i]["variety"]
        country = json_data[i]["country"]

        list.append({"name":name, "content":content, "tag":tag, "country":country})

pprint.pprint(list)

