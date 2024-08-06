from rest_framework import serializers

from apps.tour.models import Category, Country, Destination, Hotel, Restaurant, Tour


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    destinations_count = serializers.SerializerMethodField()

    def get_destinations_count(self, obj):
        return  obj.destination_set.count()
    
    class Meta:
        model = Country
        fields = ['id', 'name', 'image', 'destinations_count']


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True)
    class Meta:
        model = Tour
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'