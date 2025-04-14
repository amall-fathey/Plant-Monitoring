from rest_framework.generics import ListAPIView
from .serializers import PlantSerializer, Plant

class ListPlantsAPI(ListAPIView) : 
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    
    
