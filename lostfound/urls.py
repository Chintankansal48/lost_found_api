from django.urls import path
from .views import LostItemListCreate, FoundItemListCreate, DeleteLostItem, DeleteFoundItem, MatchItemsView  # ✅ Import added

urlpatterns = [
    path('lost-items/', LostItemListCreate.as_view(), name='lost-items'),
    path('found-items/', FoundItemListCreate.as_view(), name='found-items'),
    path('lost-items/<int:pk>/', DeleteLostItem.as_view(), name='delete-lost-item'),
    path('found-items/<int:pk>/', DeleteFoundItem.as_view(), name='delete-found-item'),
    path('match-items/', MatchItemsView.as_view(), name='match-items'),  # ✅ Fix added
]
