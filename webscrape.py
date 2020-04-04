#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[2]:


# site url
home_page = ""

# number of pages on site
pages = np.arange(1,15)


# In[3]:


def clean(string):
    val = string.replace('\n','').replace('\xa0','').split('div')
    return list(filter(None,[i.strip() for i in val]))


# In[4]:


def main():
    
    df = pd.DataFrame()
    # scrape site and clean
    all_text_in_div = [i.get_text("div") for i in soup.find_all("div", {"class": "entry-details"})]
    all_text_in_div_cleaned = list(map(lambda x: clean(x),all_text_in_div))
    
    # add data to df
    df = pd.DataFrame(all_text_in_div_cleaned, columns = ['Addr',"1",'Interest',"2",'Rank'])
    df["Bank"] = [i.get_text("h2") for i in soup.find_all("h2", {"class": "entry-title"})]
    
    # clean df
    df.drop(['1','2'], axis = 1)
    col_arranged = ['Bank','Addr','Interest','Rank']
    return df[col_arranged]


# In[8]:


if __name__ == '__main__':
    for i in pages:
        url = home_page + str(i) +'/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if i == 1:
            tmp_df = main()
            tmp_df.to_csv('./scrape.csv', index = False)
        else:
            tmp_df = main()
            tmp_df.to_csv('./scrape.csv', mode='a', header = False, index = False)
