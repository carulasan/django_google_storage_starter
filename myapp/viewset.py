from rest_framework import  viewsets,filters
from myapp.models import Map
from myapp.serializer import MapSerializers
class MapViewset(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializers
    filter_backends = (filters.SearchFilter,)
  


