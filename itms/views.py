from rest_framework import status
from rest_framework.response import Response
from .models import Item, Contact
from django.shortcuts import get_object_or_404
from .serializer import ItemSerializer, ContactSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView


class ItemView(ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all().select_related('seller')
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)


class ItemDetail(RetrieveAPIView):
    queryset = Item.objects.all().select_related('seller')
    serializer_class = ItemSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = []


class AllItems(ListAPIView):
    queryset = Item.objects.all().select_related('seller')
    serializer_class = ItemSerializer
    authentication_classes = ([TokenAuthentication, BasicAuthentication])
    permission_classes = ()


@api_view(['PUT', ])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def mark_item_sold(request, pk):
    data = {}
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'PUT' and request.user == item.seller:
        item.sold = True
        item.save()
        data['response'] = 'Update Successful'
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data['response'] = 'You are not authorized'
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def delete_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if item.seller == request.user:
        if request.method == 'DELETE':
            data = {}
            item_deleted = item.delete()
            if item_deleted:
                data['response'] = 'Item deleted successfully'
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(data, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ContactView(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        item = get_object_or_404(Item, pk=self.request.data.get('item'))
        return serializer.save(item=item, interest=True)


class ContactDetail(RetrieveUpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, ]