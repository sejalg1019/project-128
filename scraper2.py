from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

request = requests.get(url)

soup = bs(request.text,'html.parser')
star_data = soup.find_all('table')
data = []

table_rows = star_data[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    data.append(row)

name = []
distance =[]
mass = []
radius =[]


for i in range(1,len(data)):
    name.append(data[i][0])
    distance.append(data[i][5])
    mass.append(data[i][7])
    radius.append(data[i][8])

df2 = pd.DataFrame(list(zip(name,distance,mass,radius,)),columns=['name','distance','mass','radius'])
print(df2)

df2.to_csv('dwarf_stars.csv')