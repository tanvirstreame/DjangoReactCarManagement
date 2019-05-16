from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin
from .models import Car,ShowRoom,ShowRoomOwner,CarAssignToShowRoom,ShowRoomOwnerAssignToShowRoom,CarImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields ='__all__'


class CarSerializers(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    class Meta:
        model = Car
        fields = ('manufacture','tagline','car_model','mileage','year','status','transmission','price','horse_power','propellant','image')

class ShowRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowRoom
        fields = '__all__'


class ShowRoomOwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowRoomOwner
        fields = '__all__'


class CarAssignToShowRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarAssignToShowRoom
        fields = '__all__'
        # read_only_fields=('car',)


class ShowRoomOwnerAssignToShowRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowRoomOwnerAssignToShowRoom
        fields = '__all__'


class GetCarByShowRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarAssignToShowRoom
        fields = '__all__'
        read_only_fields=('car',)
        depth=1

