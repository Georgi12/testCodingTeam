from rest_framework import serializers
from restaurant.models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')


class CreateFoodSerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=200)
    code = serializers.IntegerField()
    internal_code = serializers.IntegerField()
    name_ru = serializers.CharField(max_length=200)
    cost = serializers.DecimalField(decimal_places=2, max_digits=10)

