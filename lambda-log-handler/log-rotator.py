#!/usr/bin/python3
# -*- coding: utf-8 -*-

### by Giuliano

import json
import requests
import os
from datetime import date

def lambda_handler(event, context):

    # gets latests backups
    backups = requests.get(os.environ['ELASTICSEARCH_ENDPOINT'] + '/_snapshot/s3/_all?pretty')

    # make backups as json files
    backups = json.loads(backups.text)

    # prints length pf backups
    # print(type(backups))

    backups_len = len(backups['snapshots'])
    print("Backup Length: {}".format(backups_len))

    # gets current date
    today = date.today()
    today = today.strftime("%d-%m-%Y")
    print("Today: {}".format(today))

    # takes date from latest backup
    print("Latest Backup: {}".format(backups['snapshots'][backups_len - 1]['snapshot']))

    # checks if latest backup has SUCCESS state
    if (today == backups['snapshots'][backups_len - 1]['snapshot']) and (backups['snapshots'][backups_len - 1]['state'] == 'SUCCESS'):
        print('*****SUCCESS*****')
        for i in range((backups_len - 2), (backups_len - 5), (-1)):
            print(backups['snapshots'][i]['snapshot'])
        # delete backup from 3 days ago
        to_be_deleted = backups['snapshots'][(backups_len - 6) - (backups_len - 2)]['snapshot']
        print("Backup to be deleted: {}".format(to_be_deleted))
    else:
        print("Send a Slack notification that there is not backup today")

    # delete backup
    delete = requests.delete(os.environ['ELASTICSEARCH_ENDPOINT'] + '/_snapshot/s3/' + to_be_deleted)
    #delete = requests.delete(os.environ['ELASTICSEARCH_ENDPOINT'] + '/_snapshot/s3/' + '25-10-2021')
    print("delete error code: {}".format(delete))
    print("delete content: {}".format(delete.text))

    return {
        'statusCode': 200,
        'backups': backups
        # 'body': json.dumps('Hello from Lambda!'),
        # 'backups': backups.text
    }