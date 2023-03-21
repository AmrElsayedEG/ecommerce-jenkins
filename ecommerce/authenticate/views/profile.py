from rest_framework.generics import RetrieveUpdateAPIView
from utils import IsAuthenticated
from authenticate.serializers import ProfileSerializer

class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

