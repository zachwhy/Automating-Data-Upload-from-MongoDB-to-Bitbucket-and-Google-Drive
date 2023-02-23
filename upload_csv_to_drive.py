from pydrive.auth import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from datetime import date

import pymongo


import pandas as pd


######## creating daily session csv##############

current = str(date.today())

name = "/home/yncalab/curate_data/plonline_data/" + "pldata_" + current + ".csv"

df = pd.read_csv(name)


df2 = df.loc[:,["id","sessionNo", "start"]]

names = list(set(df2.id))

# names

sessions = []
created_at = []

print("converting data")

for i in names:
    total = df2[df2["id"] == i ]

    session = int(total.iloc[-1:,1])
    dates = total.iloc[-1:,2].to_list()[0]

    sessions.append(session)
    created_at.append(dates)

current2 = str(date.today().strftime('%d-%m-%Y'))

new_df = pd.DataFrame({"id" : names, "final_session_" + current2 : sessions,"start" : created_at})

new_df["start"] = pd.to_datetime(new_df['start'], format='%Y%m%d %H:%M:%S')

new_df.to_csv("/home/yncalab/curate_data/daily_session.csv")

print("data convert done")


############### Upload to Google Drive #####################################

gauth = GoogleAuth()

scope = ['https://www.googleapis.com/auth/drive']
client_json_path = "/home/yncalab/curate_data/client_secrets.json"


gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(client_json_path, scope)

gauth.ServiceAuth()

drive = GoogleDrive(gauth)

#

gfile = drive.CreateFile({ "id": "[file id]",'title': "daily_session.csv", 'parents': [{'id': '[folder id]'}]})

upload_file = "/home/yncalab/curate_data/daily_session.csv"

print("uploading to Google Drive")

gfile.SetContentFile(upload_file)

gfile.Upload() # Upload the file.

print("uploading done")






