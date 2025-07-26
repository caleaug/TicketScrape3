# **********3*******
import requests
import json
import urllib
import math
from pathlib import Path
import gspread, datetime, time
from google.oauth2.service_account import Credentials
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

CredsPath = Path(__file__).resolve().parent.parent / 'tickets-Cred.json'
creds = Credentials.from_service_account_file(CredsPath, scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(creds)
sheets = client.open_by_key("1jD9KDi1VwgWO9cZ674cPUrZu0JnyV32RrD3eQKuBGIQ")
wksMain = sheets.get_worksheet_by_id(0) #main #sheets.worksheets()
wksKeys = sheets.get_worksheet_by_id(1432966988)
wksCheapest = sheets.get_worksheet_by_id(855558548)

def start():
  date = str(datetime.date.today().strftime("%m.%d.%y"))
  Time = datetime.datetime.now().strftime("%I:%M %p")
  wksMain.update_cell(1,1,date)
  wksMain.update_cell(1,2,Time)
  #letters = ["A","B","C","D","E",'F','G']
  wksMain.batch_clear(["E2:J100"])

def FindColumn(head, sheet = wksMain):
  headings = sheet.row_values(1)
  c=1
  for h in headings:
    if h == head: return c
    c+=1

def FindKeys(head):
  Keys = {}
  DateCol = wksKeys.col_values(FindColumn("Date", wksKeys))[1:]
  KeyCol = wksKeys.col_values(FindColumn(head, wksKeys))[1:]

  for d, k in zip(DateCol,KeyCol):Keys[d] = k
  return Keys

def DateValid(date):
  if date:
    Cy = int(datetime.date.today().strftime("%y"))
    Cm = int(datetime.date.today().strftime("%m"))
    Cd = int(datetime.date.today().strftime("%d"))

    y = int(date.split("/")[2])
    m = int(date.split("/")[0])
    d = int(date.split("/")[1])
    if y > Cy: return True
    if Cy < y: return False
    if m > Cm: return True
    if m == Cm and d >= Cd: return True
  return False

def UpdateCell(x,y, val):
  wksMain.update_cell(x,y, val)

def timeFormat(num):
  m = int(num/60)
  sec = int(num-(m*60))
  if sec<10: return (str(m)+":0"+str(sec))
  return (str(m)+":"+str(sec))

def DisplayTime(site, col, sec):
  y = len(wksMain.col_values(col))+1
  UpdateCell(y, col ,timeFormat(sec))
  print(site+": "+timeFormat(sec))
  
