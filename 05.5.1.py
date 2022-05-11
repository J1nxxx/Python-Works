from fileinput import filename
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

myURL="https://shorturl.asia/awPYO"  

r = requests.get(myURL)  
s = BeautifulSoup(r.content, "html.parser") 

for i in s.find_all('div'):
   print(i.find('div',attrs={"class":"PostContentstyle__PostContentContainer-sc-17nog4h-5 kDJwCh post-content"}).get_text())


