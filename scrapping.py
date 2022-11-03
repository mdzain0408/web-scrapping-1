from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(url)
soup = bs(page.text, 'html.parser')
table = soup.find('table')
temp_list = []
t_rows = table.find_all('tr')
for tr in t_rows:
    t_dta = tr.find_all('td')
    row = [i.text.rstrip() for i in t_dta]
    temp_list.append(row)
name = []
mass = []
radius = []
distance = []
luminosity = []
for i in range(1, len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    luminosity.append(temp_list[i][7])
df = pd.DataFrame(list(zip(name, distance, mass, radius, luminosity)), columns = ['Star_Names', 'Star_Distance', 'Star_mass', 'Star_radius', "Star_luminosity"])
df.to_csv('brightstars.csv')