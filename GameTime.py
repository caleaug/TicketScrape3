from TicketInit import *

def GetGameData(key):
    url = "https://mobile.gametime.co/v3/listings/"+key+"?quantity=1"
    response = requests.get(url)
    return response.json()

def GetGameTimePrice(data):
    arr = []
    try:
        for d in range(len(data["listings"])):
            if data["listings"][d]["spot"]["section_group"] == "General Admission":
                arr.append(int(data["listings"][d]["price"]["total"]/100))
        return max(arr)
    except: return "NA"

def UpdateGameTime(p=False):
  Keys = FindKeys("GameTime")
  col = FindColumn("GameTime")

  t0 = time.time();y=1;delay = time.time()+ 1
  dates = wksMain.col_values(3)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
        price = GetGameTimePrice(GetGameData(Keys[d]))
        UpdateCell(y, col, price)
        if p: print(price) # Testing

        if time.time()< delay: time.sleep(delay-time.time())
        delay = time.time()+ 1;
    y+=1
  DisplayTime("GameTime", col, time.time()-t0)

if __name__ == "__main__": UpdateGameTime(True)



















