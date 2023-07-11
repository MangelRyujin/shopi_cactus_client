from django.conf import settings
from shopi_cactus_client.settings.base import CARRO_SESSION_ID



class Car:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        car = self.session.get(settings.CARRO_SESSION_ID)
        if not car:
            car = self.session[settings.CARRO_SESSION_ID]={}
        self.car=car
        
        
    def add(self,request, plant):
        if str(plant['id']) not in self.car.keys():
            self.car[plant['id']] = {
                "plant_id": plant['id'],
                "plant_name":plant['name'],
                "qty": 1,
                "cost": round(float(plant['cost']),2),
                "image":plant['image'] if plant['image'] != '' else '',
            }
        else:
            for key, value in self.car.items():
                if key == str(plant['id']):
                    value["qty"] = value["qty"]+1
                    value["cost"] = round(float(plant['cost']) * value["qty"],2)
                    break
        self.save()
        
        
    def car(sefl,request):
        return sefl.car 
        
    def save(self):
        self.session["car"] = self.car
        self.session.modified = True
        
        
    def remove(self,plant):
        plant_id = str(plant['id'])
        if plant_id in self.car:
            del self.car[plant_id]
            self.save()
            
    def decrement(self,plant):
        for key, value in self.car.items():
            if key == str(plant['id']):
                value["qty"] = value["qty"]-1
                value["cost"] = round(float(plant['cost']) * value["qty"],2)
                if value["qty"] < 1:
                    self.remove(plant)
                else:
                    self.save()
                break
            else:
                pass
        
    def clear(self):
        self.session[settings.CARRO_SESSION_ID]={}
        self.session.modified=True
        
        
    def qty_plants(self,request):
        qty = 0
        
        for value in self.car.values():
            qty+= value['qty']
        return qty
    
    def cost_car(self,request):
        cost = 0
        
        for value in self.car.values():
            cost+= value['cost']
        return cost