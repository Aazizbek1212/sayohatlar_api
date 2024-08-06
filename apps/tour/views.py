
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from apps.tour.models import Category, Country, Destination, Hotel, Restaurant, Tour
from apps.tour.seralizers import CategorySerializer, CountrySerializer, DestinationSerializer, HotelSerializer, RestaurantSerializer, TourSerializer





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
    serializer = TourSerializer(tours, many = True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def tour_list_view(request):
    tours = Tour.objects.all()
    category = request.GET.get('category')
    destination = request.GET.get('destination')
    country = request.GET.get('country')

    if category:
        category = Category.objects.get(id=category)
        tours = tours.filter(categories__in=[category,])

    if destination:
        destination = Category.objects.get(id=destination)
        tours = tours.filter(destinations__in=[destination,])

    if country:
        country = Category.objects.get(id=country)
        tours = tours.filter(countries__in=[country,])

    serializer = TourSerializer(tours, many = True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def tour_detail_view(request, pk):
    tour = Tour.objects.get(id=pk)
    serializer = TourSerializer(tour, many = True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def hotel_detail_view(request, pk):
    hotel = Hotel.objects.get(id=pk)
    serializer = HotelSerializer(hotel, many = True)
    return Response(serializer.data, 200)


class TourViewSet(viewsets.ViewSet):

    def list(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many = True)
        return Response(serializer.data, 200)
    

    def retrieve(self, request, pk=None):
        tours = Tour.objects.get(pk=pk)
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, 200)

    