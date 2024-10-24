import pandas as pd
import numpy as np
import re

df = pd.read_csv('./Data.csv', sep=',')

dfnew = pd.read_csv('./fix_to_surname.csv', sep=';')

df['firt name'] = df['firt name'].str.replace('#','e').str.replace('@','a').str.replace('!','i').str.replace('$','o').str.replace('%','a').str.replace('-',' ')

df['last name'] = dfnew['last name'].str.replace('😀','o').str.replace('😂','u').str.replace('�','i').str.replace('$','e').str.replace('3','a').str.capitalize()

def replace_special_chars_after_at(text):
    if isinstance(text, str): 
        parts = text.split('@')
        if len(parts) == 2:
            cleaned_part = re.sub(r'[^a-zA-Z0-9]', '.', parts[1])
            return parts[0] + '@' + cleaned_part
    return text
  
df['email'] = df['email'].replace(np.nan, 'UNDEFINED').str.replace('$','@').str.replace('#','@').str.replace('!','@').str.replace('tmall.','hotmail.').str.strip()

df['email'] = df['email'].apply(replace_special_chars_after_at)

df['email'] = df['email'].str.replace('ufffd','', regex=False)

def clean_email(text):
  if text == "UNDEFINED":
    return text
  local_part, domain_part = text.split('@')
  cleaned_local_part = re.sub(r'(.)\1+', r'\1', local_part)
  return f'{cleaned_local_part}@{domain_part}'

df['email'] = df['email'].apply(clean_email)