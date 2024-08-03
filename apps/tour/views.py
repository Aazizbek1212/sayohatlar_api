
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.tour.models import Category, Country, Destination, Restaurant, Tour
from apps.tour.seralizers import CategorySerializer, CountrySerializer, DestinationSerializer, RestaurantSerializer

@api_view(['GET'])
def featured_categories_view(request):
    categories = Category.objects.all()[:5]
    serializer = CategorySerializer(categories, many = True)
    return Response(serializer.data, 200)




@api_view(['GET'])
def featured_countries_view(request):
    countries = Country.objects.all()[:3]
    serializer = CountrySerializer(countries, many = True)
    return Response(serializer.data, 200)



@api_view(['GET'])
def festured_destination_view(request):
    destination = Destination.objects.all()[:10]
    serializer = DestinationSerializer(destination, many = True)
    return Response(serializer.data, 200)



@api_view(['GET'])
def festured_restaurant_view(request):
    retaurants = Restaurant.objects.all()[:5]
    serializer = RestaurantSerializer(retaurants, many = True)
    return Response(serializer.data, 200)



@api_view(['GET'])
def tours_by_destination_view(request, pk):
    destination = Destination.objects.all()
    tours = Tour.objects.filter(destination_in=[destination])
    serializer = RestaurantSerializer(tours, many = True)
    return Response(serializer.data, 200)