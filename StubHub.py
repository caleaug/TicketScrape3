from TicketInit import *
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

##url = "https://www.stubhub.com/chicago-cubs-chicago-tickets-5-14-2025/event/154616437/?quantity=1&sections=1441865&ticketClasses=4380&rows=&seats=&seatTypes=&listingQty="
##
##uClient = uReq(url)
##html = uClient.read()
##uClient.close()
##soup = soup(html, "html.parser")
##
##file = soup.find(id="index-data")
##data = json.loads(file.string)

def StubHubData(key):
    url = "https://www.stubhub.com/event/"+key+"/?quantity=1&sections=1441865&ticketClasses=4380&rows=&seats=&seatTypes=&listingQty=&estimatedFees=true"
    #url = "https://www.stubhub.com/chicago-cubs-chicago-tickets-6-12-2025/event/154617683/?quantity=2"
    #url = "https://www.stubhub.com/event/154617673/?quantity=1&sections=1441865&ticketClasses=4380&rows=&seats=&seatTypes=&listingQty=&estimatedFees=true"
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
            try:arr.append(int(data["grid"]["items"][1]["price"].replace("$","")))
            except: pass
    if arr: return min(arr)
    if not arr: return "Error"

def UpdateStubHub():
  Keys = FindKeys("StubHub")

  t0 = time.time(); n=0
  dates = wksMain.col_values(3)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
        price = GetStubHubPrice(StubHubData(Keys[d]))
        print(d, Keys[d], price)
        n+=1

  print(round(time.time()-t0,2), n)

key0 = "154617673" # jun 14
