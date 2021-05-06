# import uvicorn
# from fastapi import FastAPI  # type:ignore
# from fastapi.responses import UJSONResponse  # type:ignore
# from mabel.logging import get_logger, set_log_name
from google.cloud import resource_manager
import sys
import numpy as np  # am i using this???
import pandas as pd
import os
import subprocess
import requests
import json
import fileinput

#Need to run this for Auth
#gcloud auth application-default login

client = resource_manager.Client()
access_token = os.popen('gcloud auth print-access-token').read()[:-1]

#Make a list of all the repos
response = requests.get('https://eu.gcr.io/v2/_catalog', auth=('_token', access_token))
with open('repo_image_list.json', 'w') as f:
    print(response.json(), file=f)

#tidy the output so ' becomes " - validating json
with fileinput.FileInput("repo_image_list.json", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('\'', "\""), end='')
        
df = pd.read_json ('repo_image_list.json')

#Need to run this to get further info
#gcloud container images describe eu.gcr.io/dcsgva-devsecops-prd/ms-twitter-publisher

with open('repo_image_tags_list.json', 'w') as f:
    #just to see it running
    print(response.json(), file=f)
    
for index, repositories in df.iterrows():
    repo = str(repositories['repositories'])
    resp = requests.get('https://eu.gcr.io/v2/' + repo + '/tags/list', auth=('_token', access_token))

    with open('repo_image_tags_list.json', 'a') as f:
        print(repo) #just to watch it progressing
        print(resp.json(), file=f)
        #resp.json()

#df_repo_image_list.to_json("datatester.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

with fileinput.FileInput("repo_image_tags_list.json", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('\'', "\""), end='')

df_img_tags_list = pd.read_json ('repo_image_tags_list.json', lines=True)

print(df_img_tags_list)

df_img_tags_list.to_json("datatester.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

df_img_tags_list = df_img_tags_list.iloc[1:]

print(df_img_tags_list)

with open('repo_name_tags_list.csv', 'w') as f:
    print("repo|tags", file=f)

#for index, repositories in df.iterrows():
 #   repo = str(repositories['repositories'])
 #   #print(repo)
for index, row in df_img_tags_list.iterrows():
    tags = str(['manifest'])
    print(index, row['name'], row['tags'], row['manifest']) #just to watch it progressing
    dft = pd.DataFrame(columns=[index, row['name'], row['tags']])
    
    with open('repo_name_tags_list.csv', 'a') as f:
        print((row['name'], row['tags']), file=f)
