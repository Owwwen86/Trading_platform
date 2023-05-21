from django.db import transaction
from rest_framework import serializers
from tradingplatform.links.models import Link, Contact, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkCreateSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)

    def create(self, validated_data):
        link = Link.objects.create(**validated_data)
        link.is_level()
        return link

    class Meta:
        model = Link
        read_only_fields = ('level', 'TimeCreate',)
        exclude = ('id', )
        depth = 1


class LinkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)

    class Meta:
        model = Link
        read_only_fields = ('id', 'debt',)
        fields = '__all__'
        depth = 1


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

