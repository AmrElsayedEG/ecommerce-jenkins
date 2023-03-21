from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from utils import IsAuthenticated
from users.serializers import WishListSerializer, CreateWishListSerializer
from rest_framework.response import Response
from users.models import WishList

class ListWishListView(ListAPIView):
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)

class AddWishListView(CreateAPIView):
    queryset = WishList
    serializer_class = CreateWishListSerializer
    permission_classes = [IsAuthenticated]

class RemoveWishListView(DestroyAPIView):
    queryset = WishList
    serializer_class = CreateWishListSerializer
    permission_classes = [IsAuthenticated]