import requests

api_key = 'mGxAZ0XpuFIKWpSW73hf61aSzWNVCPpt'

base_url = 'https://app.ticketmaster.com/discovery/v2/'

start_date = "2024-07-04T16:18:00Z"
end_date = "2024-09-24T15:39:00Z"
min_price = 10
max_price = 100
def query(startDate, endDate, latitude, longitude, radius, maxPrice):
    endpoint = 'events.json'
    url = f'{base_url}{endpoint}'
    params = {
        'apikey': api_key,
        'latlong': f'{latitude},{longitude}',
        'radius': radius,
        'startDateTime': startDate,
        'endDateTime': endDate,
        'unit': "miles",
        'maxPrice': maxPrice
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data
