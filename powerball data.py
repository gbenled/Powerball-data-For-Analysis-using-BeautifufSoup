def powerball_data(): 
  import requests
  from bs4 import BeautifulSoup
  import csv
  import urllib.request
  import codecs
  import pandas as pd

  link = 'https://www.txlottery.org/export/sites/lottery/Games/Powerball/Winning_Numbers/download.html'
  r = requests.get(link)
  soup = BeautifulSoup(r.text, "html.parser")
  l= []
  for i in soup.find_all('a'):
      if i.get('href')!=None:
          if i.get('href')[0]!= "/" and i.get('href')[-3:]== "csv":
              link = (i.get('href'))

  url = link
  response = urllib.request.urlopen(url)
  cr = csv.reader(codecs.iterdecode(response, 'utf-8'))
  a=[]
  for row in cr:
      a.append(row)

  data = pd.DataFrame(a)
 return data
 
 
powerball_data()
