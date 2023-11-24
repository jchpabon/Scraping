import pandas as pd

url ='https://www.skysports.com/league-1-table'

df = pd.read_html(url)
df = df[0]

df.to_json('pandatable.json', orient = 'records')
df.to_csv('pandatable.xls', index =False)

