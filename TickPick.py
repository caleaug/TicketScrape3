from TicketInit import *
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#url = "https://www.tickpick.com/buy-chicago-cubs-vs-chicago-white-sox-tickets-wrigley-field-5-16-25-1pm/6574580/?sections=stars:any%7Cinclude:GA%20Bleachers%7Cexclude:all"
#url = "https://www.tickpick.com/buy-chicago-cubs-vs-chicago-white-sox-tickets-wrigley-field-5-16-25-1pm/6574580/"
url = "https://api.tickpick.com/1.0/listings/internal/event/6574580?trackView=true"

url = "https://example.com/api/data"
headers = {"forter-token-cookie": "c0dbe0d245c74ef98c518b086442cd31_1747346149857_121_UDF9_24ck",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0",
"session-id":"zZlkPcuwodaFdiiLE_bFSS9AnXarMLfY"}



response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
