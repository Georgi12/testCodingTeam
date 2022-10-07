from django.contrib import admin
from django.urls import path, include

from restaurant.views.food.urls import food_router

urlpatterns = [
    path('api/v1/', include(food_router.urls)),
    path('admin/', admin.site.urls),
]
