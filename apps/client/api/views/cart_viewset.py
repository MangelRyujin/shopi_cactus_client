from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.client.shopi_cart.cart import Car
from rest_framework.decorators import action
from apps.client.api.views.requests.plants_requests import detail_plant






class CarViewSet(viewsets.GenericViewSet):
    
    # detail car
    def list(self,request,*args,**kargs):
        car = Car(request)
        if car:
            return Response({'order_items':car.car.values(),'qty_plants':car.qty_plants(self),'cost_car':car.cost_car(self)},status=status.HTTP_200_OK)

        return Response({'order_items':[]},status=status.HTTP_200_OK)
    
    @action(detail = False, methods = ['get'])
    def add_car(self,request):
        car = Car(request)
        plant_id = self.request.query_params.get('plant_id')
        plant,_ = detail_plant(plant_id)
        if plant:
            car.add(request = request.data,plant=plant) 
            return Response({'message':'Añadido al carrito','plant':plant},status=status.HTTP_200_OK)
        return Response({'error':'No estas enviando la información'},status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail = False, methods = ['delete'])
    def carro_remove_item(self,request):
        car = Car(request)
        plant_id = self.request.query_params.get('plant_id')
        plant,_ = detail_plant(plant_id)
        car.decrement(plant)
        return Response({'message':'Eliminaste una planta del carrito'},status=status.HTTP_200_OK)
    

    @action(detail = False, methods = ['delete'])
    def carro_limpiar(self,request):
        car = Car(request)
        car.clear()
        return Response({'car':'Carro limpiado'},status=status.HTTP_200_OK)
    
    
    
    