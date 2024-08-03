from django.contrib import admin

from apps.tour.models import Category, Country, Destination, Restaurant, Tour



admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(Restaurant)
admin.site.register(Tour)