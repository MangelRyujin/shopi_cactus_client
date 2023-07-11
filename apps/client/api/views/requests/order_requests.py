import requests

def created_order(id,cost,items):
    
    url = 'https://shopi-plants-admin.onrender.com/create_order/order/'
    response = requests.post(url, data={'user_id': [str(id)],'cost':[cost],'items':[items.values()]})
    data = response.json()
    if response.status_code == 201:
        return data,response.status_code
    else:
        return data,response.status_code
    
def created_items_order(plant_id,order,cost,qty):
    
    url = 'https://shopi-plants-admin.onrender.com/create_order/items_order/'
    response =requests.post(url, data={'plant': [plant_id],'order':[order],'cost':[cost],'qty':[qty]})
    data = response.json()
    if response.status_code == 201:
        return data,response.status_code
    else:
        return data,response.status_code