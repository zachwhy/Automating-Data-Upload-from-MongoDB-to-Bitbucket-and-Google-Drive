import pandas as pd

from datetime import datetime
from datetime import date

import pymongo

mongo = pymongo.MongoClient("",
    serverSelectionTimeoutMS = 1000)

print("server connected")

db = mongo.production
db = db.sonadatas


data = db.find({}, {
                    "data": 1,
                    "group": 1,
                    "createdAt": 1,
                    "participantId": 1
                    })




data = list(data)

print("data downloaded")


names = []
groups = []
values = []
created_at = []


for i in data:
    for j in i["data"]:
        name = i["participantId"]
        group = i["group"]
        start = i["createdAt"]

        value = j



        names.append(name)
        groups.append(group)
        values.append(value)
        created_at.append(start)

new_values = pd.DataFrame.from_dict(values)



df = pd.DataFrame({"id": names, "group": groups, "start": created_at})

df = df.join(new_values)

print("data converted")



current = str(date.today())



df.to_csv("/home/yncalab/curate_data/plonline_data/pldata_" + current + ".csv"  ,header=True, index_label=False, index=False)

print("done")
