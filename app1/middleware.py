import requests
import json
class Coviod19:
    def __init__(self,get_response):
        self.get_response=get_response
        response=requests.get('https://api.covid19india.org/state_district_wise.json')

        print(response.status_code)
        dict_data=json.loads(response.text)
        json.dump(dict_data,open('app1/raw/coviod19.json','w'))

        print('data created')


    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        print('I am call')
        return response