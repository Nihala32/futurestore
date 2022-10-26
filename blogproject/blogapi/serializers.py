from rest_framework import serializers
from blogapi.models import Mobiles,Reviews,Carts,Orders
from django.contrib.auth.models import User


class MobileSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    band=serializers.CharField()
    display=serializers.CharField()
    processor=serializers.CharField()

    def validate(self,data):
        cost=data.get("price")
        if cost<0:
            raise serializers.ValidationError("invalid price")
        else:
            return data


class MobileModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    average_rating=serializers.CharField(read_only=True)
    class Meta:
        model=Mobiles
        fields=["id",
            "name",
            "price",
            "band",
            "display",
            "processor",
                "average_rating",
                "total_reviews"
        ]

    def validate(self, data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid price")
        return data



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model=Reviews
        fields=["review","rating","author"]

    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Reviews.objects.create(author=user,product=product,**validated_data)

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["user",
                "product",
                "date",
                "status"]

    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(**validated_data,user=user,product=product)

class OrderSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields=[
            "user",
            "product",
            "status"
        ]

    def create(self, validated_data):
        user = self.context.get("user")
        product = self.context.get("product")
        return Orders.objects.create(user=user, product=product, **validated_data)





