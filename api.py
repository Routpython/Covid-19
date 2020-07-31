import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "be40fa23dfmsh7582999b627271bp1b837fjsn264e833ddcf3"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)