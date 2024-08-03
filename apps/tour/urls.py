from django.urls import path

from apps.tour.views import featured_categories_view, featured_countries_view, festured_destination_view, festured_restaurant_view, hotel_detail_view, tour_detail_view, tours_by_destination_view


urlpatterns = [
    path('featured_categories/', featured_categories_view, name='categories'),
    path('featured_countries/', featured_countries_view, name='countries'),
    path('festured_destination/', festured_destination_view, name='destinations'),
    path('festured_restaurant/', festured_restaurant_view, name='restaurants'),
    path('tours_by_destination/<int:pk>/', tours_by_destination_view, name='tours'),
    path('tour_detail/<int:pk>/', tour_detail_view, name='tourdetail'),
    path('hotel_detail/<int:pk>/', hotel_detail_view, name='hoteldetail'),
]
