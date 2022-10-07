from rest_framework import routers

from restaurant.views.food.viewsets import FoodViewSet

food_router = routers.DefaultRouter()


food_router.register(r'foods', FoodViewSet)
