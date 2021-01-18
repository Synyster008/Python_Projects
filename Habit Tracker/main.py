import requests
from datetime import datetime

USERNAME = 'synyster008'
TOKEN = 'asdn45kk45kk'

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    'X-USER-TOKEN': TOKEN,
}

graph_config = {
    'id': 'graph1',
    'name': 'Gaming',
    'unit': 'hours',
    'type': 'float',
    'color': 'momiji',
}

#graph_response = requests.post(url=graph_endpoint, json=graph_config, headers= header)
#print(graph_response.text)

now = datetime.now().strftime('%Y%m%d')

pixel_endpoint = f"{graph_endpoint}/graph1/{now}"

pixel_config = {
    'quantity': '1.5'
}

pixel_response = requests.put(url=pixel_endpoint, json=pixel_config, headers= header)
print(pixel_response.text)


