import os
import requests
import json

cwd_dir = os.getcwd()
db_dir = os.path.join(cwd_dir, "FlavorDB")

if not os.path.exists(db_dir):
    os.makedirs(db_dir)

for index in range(1000):
    try:
        url = "https://cosylab.iiitd.edu.in/flavordb/entities_json?id=%d" % index
        data = requests.get(url).json()
        obj = json.dumps(data)
        
        name_key = "entity_alias_readable"
        name = data[name_key]

        print("Downloading %s data" % name)

        file_name = os.path.join(db_dir, "%d.json" % index)

        with open(file_name,'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        
        index+=1
    except:
        continue

print("Done")