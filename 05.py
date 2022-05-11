from audioop import findfactor
from bdb import effective
from ctypes.wintypes import HHOOK
from curses import def_prog_mode
from curses.ascii import LF
from decimal import DivisionByZero
from email.generator import DecodedGenerator
from email.utils import decode_rfc2231
from fcntl import F_GETFD, F_GETPATH
from lib2to3.pgen2 import grammar
from lib2to3.pgen2.pgen import DFAState
from os import fdatasync, fsdecode
from pkgutil import get_data
from readline import read_history_file
from socket import J1939_NO_ADDR
from ssl import VerifyFlags
from this import d
from tkinter import E
from tkinter.filedialog import FileDialog
from turtle import fd
from urllib import response
from winreg import HKEY_DYN_DATA
from xml.dom.minidom import getDOMImplementation
from xml.sax.handler import feature_external_ges
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL="https://shorturl.asia/awPYO" 

def get_data(url):
  response = requests.get(URL)  
  soup = BeautifulSoup(r.content, "html.parser")

  data = []
  
  for i in s.find_all('div'): 
    print(i.find('div',attrs={"class":"PostContentstyle__PostContentContainer-sc-17nog4h-5 kDJwCh post-content"}).get_text())

  def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel("books.xlsx")
    df.to_csv("books.xlsx")

  if __name__ == '__main__':
    data = get_data("https://shorturl.asia/awPYO")
    export_data(data)
    print("Done.")