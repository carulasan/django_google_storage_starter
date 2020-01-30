# add this 'rest_framework', on installed app(settings)
from rest_framework import serializers
from myapp.models import Map
class MapSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ('url','id','map_name','map_data')

