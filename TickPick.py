from TicketInit import *

def GetGameData(key):
    url = "https://www.tickpick.com/buy-chicago-cubs/" +key+ "/?sections=stars:any|include:GA%20Bleachers|exclude:all&qty=1-false"
    print(url)
    uClient = uReq(url)
    html = uClient.read()
    uClient.close()
    soupHtml = soup(html, "html.parser")
    return soupHtml

def GetTickPickPrice(soup):
    return 142.21
    
def UpdateTickPick(p=False):
  Keys = FindKeys("TickPick")
  col = FindColumn("TickPick")

  t0 = time.time(); y=1
  dates = wksMain.col_values(3)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
      try: price = GetTickPickPrice(GetGameData(Keys[d]))
      except: price = "NA"
      if p: print(price)
      UpdateCell(y, col, price)
    y+=1
  DisplayTime("TickPick", col, time.time()-t0)

#if __name__ == "__main__": UpdateTickPick(True)
