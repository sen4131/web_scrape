#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as pd
import json

def main(business_name):

    """Python client calling Knowledge Graph Search API."""
    api_key = open('./key.txt').read()
    query = str(business_name)

    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key
    }
    url = service_url + '?'
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    # data['itemListElement'][0]['result']

    company_df = pd.DataFrame()
    company_df['name'] = [data['itemListElement'][0]['result']['name']]
    company_df['description'] = [data['itemListElement'][0]['result']['description']]
    company_df['type'] = [data['itemListElement'][0]['result']['@type']]

    return company_df

if __name__ == '__main__':

    # get list of businesses from csv
    df = pd.read_csv(r'C:\Users\Sen\Desktop\knowledge_graph\businesses.csv', encoding='utf-8')

    for i, ch in enumerate(df['Business']):
        try:
            if i == 1:
                tmp_df = main(ch)
                tmp_df.to_csv('./businesses_filled.csv', index=False)
            else:
                tmp_df = main(ch)
                tmp_df.to_csv('./businesses_filled.csv', mode='a', header=False, index=False)
        except:
            contine
