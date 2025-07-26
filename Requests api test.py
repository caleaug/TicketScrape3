import requests

api_url = "https://www.stubhub.com/Browse/VenueMap/GetMapAvailabilityAndPrices/"
parameters = {"ShowAllTickets":True,"HideDuplicateTicketsV2":False,"Quantity":1,
              "IsInitialQuantityChange":False,"PageVisitId":"BF890DD7-37E6-470F-9ED6-B3229F07D355","PageSize":20,
              "CurrentPage":1,"SortBy":"CUSTOM_RANKING","SortDirection":1,"Sections":"1441865","Rows":"","Seats":"",
              "SeatTypes":"","TicketClasses":"4380","ListingNotes":"","PriceRange":"0,100","InstantDelivery":False,
              "EstimatedFees":True,"BetterValueTickets":True,"PriceOption":"","HasFlexiblePricing":False,
              "ExcludeSoldListings":False,"RemoveObstructedView":False,"NewListingsOnly":False,"PriceDropListingsOnly":
              False,"ConciergeTickets":False,"EventId":154620439,"CategoryId":5564,"ShowBestSellingSections":False,
              "ShowAmazingSections":False,"Favorites":False}

response = requests.get(api_url, params=parameters)

print(response)

##if response.status_code == 200:
##    print("API call successful!")
##    print(response.json())  # Assuming the response is JSON
##else:
##    print(f"Error: {response.status_code} - {response.text}")
