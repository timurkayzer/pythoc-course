import json

with open("files/example.json", "r+") as file:
    dictionary = json.loads(file.read())
    dictionary["testparam2"] = 1212121
    file.seek(0)
    file.truncate(0)
    file.write(json.dumps(dictionary))
    
    print(dictionary)