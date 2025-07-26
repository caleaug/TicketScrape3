from TicketInit import *

def StubHubData(key):
    url = "https://www.stubhub.com/event/"+key+"/?quantity=1&sections=1441865&ticketClasses=4380&rows=&seats=&seatTypes=&listingQty=&estimatedFees=true"
    uClient = uReq(url)
    html = uClient.read()
    uClient.close()
    soupHtml = soup(html, "html.parser")

    file = soupHtml.find(id="index-data")
    jsonData = json.loads(file.string)
    return jsonData

def GetStubHubPrice(data):
    arr = []
    for d in range(len(data["grid"]["items"])):
        if("Bleachers" in data["grid"]["items"][d]["section"]):
            try:arr.append(int(data["grid"]["items"][d]["price"].replace("$","")))
            except: pass
    if arr: return min(arr)
    if not arr: return "NA"

def UpdateStubHub(p=False):
  Keys = FindKeys("StubHub")
  col = FindColumn("StubHub")

  t0 = time.time(); y=1
  dates = wksMain.col_values(3)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
      try: price = GetStubHubPrice(StubHubData(Keys[d]))
      except: price = "NA"
      if p: print(price)
      UpdateCell(y, col, price)
    y+=1
  DisplayTime("StubHub", col, time.time()-t0)

if __name__ == "__main__": UpdateStubHub(True)

