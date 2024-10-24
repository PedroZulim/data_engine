import pandas as pd
import numpy as np
import re

def clean_email(text):
  if text == "UNDEFINED":
    return text
  local_part, domain_part = text.split('@')
  cleaned_local_part = re.sub(r'(.)\1+', r'\1', local_part)
  cleaned_domain_part = re.sub(r'[^a-zA-Z0-9]', '.', domain_part)
  return f'{cleaned_local_part}@{cleaned_domain_part}'

df = pd.read_csv('./Data.csv', sep=',')

dfnew = pd.read_csv('./fix_to_surname.csv', sep=';')

df['firt name'] = df['firt name'].str.replace('#','e').str.replace('@','a').str.replace('!','i').str.replace('$','o').str.replace('%','a').str.replace('-',' ')

df['last name'] = dfnew['last name'].str.replace('😀','o').str.replace('😂','u').str.replace('�','i').str.replace('$','e').str.replace('3','a').str.capitalize()

df = df.replace(np.nan, 'UNDEFINED')
  
df['email'] = df['email'].replace(np.nan, 'UNDEFINED').str.replace('$','@').str.replace('#','@').str.replace('!','@').str.replace('tmall.','hotmail.').str.strip()

df['email'] = df['email'].str.replace('ufffd','', regex=False)

df['email'] = df['email'].apply(clean_email)

df['phone number'] = df['phone number'].str.replace('.','-').str.replace('/','-')