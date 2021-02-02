from bs4 import BeautifulSoup
import requests
import pickle

source = requests.get('https://www.omniglot.com/language/names.htm').text
soup = BeautifulSoup(source, 'lxml')

degrees = []

for table in soup.find_all('table'):
    tbody = table.tbody
    count = 0
    for row in tbody.find_all('tr'):
        if count == 0:
            count+=1
            continue
        for col in row.find_all('td'):
            val = str(col.text)
            arr = val.split('(')
            degrees.append(arr[0].split(' ')[0])



with open("languages.txt", "w") as f:
    for s in degrees:
        try:
            f.write(str(s) +"\n")
            
        except Exception as e:
            print(s)

