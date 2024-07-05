from api import query

def tempName():
    events = []
    while True:
        x = input("Enter an event you wish to search for, or q to finish. If no events are entered, all events are returned from query:\n")
        if x.lower() == "q": break
        events.append(x.lower())
        #time format: YYYY-MM-DDTHH:mm:ssZ -> year-month-dayThour-minuteZ  . T and Z always the same, this is iso format
    dateRange = input("Enter the desired range of dates for the events. Format is YYYY/MM/DD - YYYY/MM/DD:\n") 
    
    dates = dateRange.split("-")
    startDate = dates[0]
    endDate = dates[1]
    startDate = startDate.replace("/","-")
    endDate = endDate.replace("/","-")
    startDate = startDate + "T16:00:00Z"
    endDate = endDate + "T16:23:59Z"
    startDate = startDate.replace(" ", "")
    endDate = endDate.replace(" ", "")


    latLong = input("Enter the coordinates of your location. Ex: 35.5588220,-119.8874795:\n")
    latLong = latLong.replace(" ", "")
    latLong = latLong.split(",")
    lat = latLong[0]
    long = latLong[1]

    radius = input("Enter the distance in miles you are willing to travel for the events:\n")

    maxPrice = input("Enter the maximum price in dollars you are willing to pay for one ticket:\n")

    data = query(startDate, endDate, lat, long, radius, maxPrice)
    print(data)

    validEvents = False
    if len(events) != 0:
        if "_embedded" not in data:
            print("There were no events that satisfied your search criteria.")
        else:
            for event in data['_embedded']['events']:
                for element in events:
                    if element in event['name'].lower():
                        print(event['name'] + " " + event['url'])
                        validEvents = True
            if not validEvents:
                print("There were no events that satisfied your search criteria.")
    else:
        for event in data['_embedded']['events']:
            print(event['name'])


if __name__ == "__main__":
    tempName()
