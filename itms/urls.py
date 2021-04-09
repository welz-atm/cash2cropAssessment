from django.urls import path
from .views import AllItems, ItemView, ContactView, ContactDetail, delete_item, mark_item_sold, ItemDetail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'itms'

urlpatterns = [
    path('create/', ItemView.as_view(), name='create_item'),
    path('list/', AllItems.as_view(), name='all_items'),
    path('view/<int:pk>/', ItemDetail.as_view(), name='view_item'),
    path('update/<int:pk>/', mark_item_sold, name='update_item'),
    path('contact/', ContactView.as_view(), name='create_contact'),
    path('contact/<int:pk>/', ContactDetail.as_view(), name='view_contact'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
]

urlpatterns = format_suffix_patterns(urlpatterns)