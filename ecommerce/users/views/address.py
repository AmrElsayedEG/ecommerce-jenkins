from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from users.models import Address, City, Country
from utils import IsAuthenticated
from users.serializers import AddressSerializer, CountrySerializer, CitySerializer
from rest_framework.response import Response

class ListCountriesAndCities(ListAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "countries" : CountrySerializer(Country.objects.all(), many=True).data,
            "cities" : CitySerializer(City.objects.all(), many=True).data
        })

class AddUserAddress(CreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        kwargs['data']['user'] = self.request.user.id
        return super().get_serializer(*args, **kwargs)

class RemoveUserAddress(DestroyAPIView):
    queryset = Address
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        if self.get_object().user.id != self.request.user.id:
            return Response({'error' : ['You dont have access to this page'], 'error_ar' : ['ليس لديك صلاحية']}, status=401)
        return super(RemoveUserAddress, self).delete(request)

class AddressShippingFees(ListAPIView):
    queryset = Address
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)