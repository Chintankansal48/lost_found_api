
from rest_framework import generics
from rest_framework.response import Response
from .models import LostItem, FoundItem
from .serializers import LostItemSerializer, FoundItemSerializer


class LostItemListCreate(generics.ListCreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer

class FoundItemListCreate(generics.ListCreateAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer

class DeleteLostItem(generics.DestroyAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer

class DeleteFoundItem(generics.DestroyAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer

class MatchItemsView(generics.GenericAPIView):
    def get(self, request):
        matches = []
        lost_items = LostItem.objects.all()
        found_items = FoundItem.objects.all()

        for lost in lost_items:
            for found in found_items:
                if (
                    lost.name.lower() in found.name.lower() or
                    found.name.lower() in lost.name.lower()
                ) and (lost.location.lower() == found.location.lower()):
                    matches.append({
                        "lost_item": LostItemSerializer(lost).data,
                        "found_item": FoundItemSerializer(found).data
                    })

        return Response(matches)

