import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        json_content = json.loads(self.get_response_body())
        return json_content
    
get = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(get.load_json())