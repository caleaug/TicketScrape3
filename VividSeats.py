from TicketInit import *

#https://www.vividseats.com/hermes/api/v1/listings?productionId=5099795&includeIpAddress=true&currency=USD&localizeCurrency=true

def VividSeatsData(key):
    url = "https://www.vividseats.com/hermes/api/v1/listings?productionId="+key
    jsonData = getJson(url)
    return jsonData


def GetVividSeatsPrice(data):
    arr = []
    for d in range(len(data["tickets"])):
        if (data["tickets"][d]['s'] == 'GA Budweiser Bleachers' and
(data["tickets"][d]['m'][0:2] == "1," or data["tickets"][d]['m'][0:2] == "1")):
            arr.append(math.ceil(float(data["tickets"][d]["aip"])))
    return min(arr)

def UpdateVividSeats():
  Keys = FindKeys("VividSeats")

  t0 = time.time(); n=0 ; delay = time.time()+ 1
  dates = wksMain.col_values(3)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
        price = GetVividSeatsPrice(VividSeatsData(Keys[d]))
        if time.time()< delay: time.sleep(delay-time.time())
        print(d, Keys[d], price, time.time())
        delay = time.time()+ 1; 
        n+=1

  print(round(time.time()-t0,2), n)

if __name__ == "__main__": UpdateVividSeats()

