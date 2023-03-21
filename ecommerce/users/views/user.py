from users.serializers import UserSerializer, UserEmailSerializer, EmailTokenSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from utils import IsAuthenticated, send_email
from django.utils.crypto import get_random_string

class UpdateUserInfoView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.serializer_class(self.request.user, data=self.request.data, partial=True)
        user.is_valid(raise_exception=True)
        user = user.update(self.request.user, user.validated_data)
        return Response(UserSerializer(user).data)

class UpdateUserEmailTokenView(APIView):
    serializer_class = UserEmailSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        new_email = self.serializer_class(data=self.request.data)
        new_email.is_valid(raise_exception=True)
        user = self.request.user
        try:
            token = get_random_string(5, '0123456789')
            send_email(
                subject="تغيير البريد الإلكترونى",
                template_name="change_email.html",
                context={
                    "token" : token,
                    "name" : user.first_name
                },
                to=[new_email.validated_data.get('email')]
            )
            user.requested_token = token
            user.save()
        except:
            Response({
                        "error" : "An error occured while sending email, Please contact support",
                        "error_ar" : "حدث خطأ، برجاء مراجعة الدعم الفني"
                    }, status=400)
        return Response({'success' : 'Please check your email for PIN', 'success_ar' : 'برجاء تفقد حسابك الإرلتكرونى للحصول على الكود'})

class UpdateUserEmailView(APIView):
    serializer_class = EmailTokenSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = self.serializer_class(data=self.request.data, context={'request' : self.request})
        user.is_valid(raise_exception=True)
        self.request.user.requested_token = None
        self.request.user.email = user.validated_data.get('email')
        self.request.user.save()
        return Response({'success' : 'You email has been changed', 'success_ar' : 'تم تغيير البريد الإلكترونى بنجاح'})