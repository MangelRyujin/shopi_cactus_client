import requests

def url_image(url):
    url_image = f'https://shopi-plants-admin.onrender.com{url}'
    return url_image

def image(plant):
    for key in plant.keys():
        if key == 'image':
            plant[key] = url_image(plant[key])
    return plant

def list_image(plants):
    for p in plants:
        image(p)
    return plants



def list_plants():
    url = 'https://shopi-plants-admin.onrender.com/plants/plants/'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        data = list_image(response.json())
        return data,response.status_code
    
    else:
        return data,response.status_code
    
def detail_plant(pk = None):
    url = f'https://shopi-plants-admin.onrender.com/plants/plants/{pk}/'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        data = response.json()
        data = image(data)
        return data,response.status_code
    
    else:
        return data,response.status_code
    
    