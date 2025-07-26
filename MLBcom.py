from TicketInit import *


def GetGameData(key):
    url = "https://mlb.tickets.com/?orgid=5&agency=MLB_MPV&pid=" + key
    print(url)
    uClient = uReq(url)
    html = uClient.read()
    uClient.close()
    soupHtml = soup(html, "html.parser")
    return soupHtml

def GetMLBcomPrice(soup):
    return 142.21
    
def UpdateMLBcom(p=False):
  Keys = FindKeys("MLBcom")
  col = FindColumn("MLBcom")

  t0 = time.time(); y=1
  dates = wksMain.col_values(3)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
      try: price = GetMLBcomPrice(GetGameData(Keys[d]))
      except: price = "NA"
      if p: print(price)
      UpdateCell(y, col, price)
    y+=1
  DisplayTime("StubHub", col, time.time()-t0)

#if __name__ == "__main__": UpdateMLBcom(True)
