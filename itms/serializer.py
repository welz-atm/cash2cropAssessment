from rest_framework import serializers
from .models import Item, Contact


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('price', 'description', 'image', 'sold', )


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('pk', 'name', 'email', 'location', 'item', 'interest', )