# **********3******* This is a test 
import requests
import json
import urllib
import math
from pathlib import Path
import gspread, datetime, time
from google.oauth2.service_account import Credentials

CredsPath = Path(__file__).resolve().parent.parent / 'tickets-Cred.json'
creds = Credentials.from_service_account_file(CredsPath, scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(creds)
sheets = client.open_by_key("1jD9KDi1VwgWO9cZ674cPUrZu0JnyV32RrD3eQKuBGIQ")
wksMain = sheets.get_worksheet_by_id(0) #main #sheets.worksheets()
wksKeys = sheets.get_worksheet_by_id(1432966988)
wksCheapest = sheets.get_worksheet_by_id(855558548)

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

def getJson(url):
    response = requests.get(url)
    return response.json()
