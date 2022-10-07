from django.http import JsonResponse
from rest_framework import viewsets
from django.db.models import Prefetch
from restaurant.models import Food, FoodCategory
from restaurant.views.food.serializers import FoodListSerializer, CreateFoodSerializer, FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()

    def list(self, request, *args, **kwargs):
        foods = self.queryset.prefetch_related(
            Prefetch(
                "food",
                queryset=Food.objects.filter(is_publish=True).distinct(),
                to_attr="foods"
            )
        ).filter(food__is_publish=True).distinct()

        serializer = FoodListSerializer(foods, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request, *args, **kwargs):
        serializer = CreateFoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        food_category, _ = FoodCategory.objects.get_or_create(name_ru=data.pop('category_name'))
        data['category'] = food_category
        food = Food(**data)
        food.save()
        return JsonResponse(data=FoodSerializer(food).data)
