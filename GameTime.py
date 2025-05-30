from TicketInit import *

def GetGameData(key):
    url = "https://mobile.gametime.co/v3/listings/"+key+"?quantity=1"
    jsonData = getJson(url)
    return jsonData


def GetGameTimePrice(data):
    arr = []
    try:
        for d in range(len(data["listings"])):
            if data["listings"][d]["spot"]["section_group"] == "GA Bleachers":
                arr.append(int(data["listings"][d]["price"]["total"]/100))
        return max(arr)
    except: return "NA"

def UpdateGameTime():
  Keys = FindKeys("GameTime")

  t0 = time.time(); n=0 ; delay = time.time()+ 1
  dates = wksMain.col_values(3)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
        price = GetGameTimePrice(GetGameData(Keys[d]))
        if time.time()< delay: time.sleep(delay-time.time())
        print(d, Keys[d], price, time.time())
        delay = time.time()+ 1;
        n+=1
  print(round(time.time()-t0,2), n)

if __name__ == "main": UpdateGameTime()



















