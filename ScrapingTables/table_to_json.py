from requests_html import HTMLSession
import json

s= HTMLSession()
url = 'https://www.skysports.com/league-1-table'
r = s.get(url)

#print(r.html.html)

#table = r.html.find('table') How many tables do we have into webpage?
#print(len(table))

table = r.html.find('table')[0]

# for row in table.find('tr'):  Finding all rows into table
#     print(row.text)

# for row in table.find('tr'):  #Finding each cell value into rows
#     for c in row.find('td'):
#         print(c.text)
#tabledata = [[c.text for c in row.find('td')] for row in table.find('tr')]# this sentnces is equal to 3 lines above
#print(tabledata)
tableheaders = [[c.text for c in row.find('th')[:-1]] for row in table.find('tr')][0]
tabledata = [[c.text for c in row.find('td')[:-1]] for row in table.find('tr')[1:]]# we don't need last cell in rows neither first row in table
#print(tabledata)
#print(tableheaders)
res = [dict(zip(tableheaders,t)) for t in tabledata] # join headers with data cells
#print(res)

with open ('table.json','w') as f:
    json.dump(res,f)