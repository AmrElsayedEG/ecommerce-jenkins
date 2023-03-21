from rest_framework.generics import CreateAPIView, UpdateAPIView
from authenticate.serializers import ForgetPasswordRequestSerializer, CheckForgetPasswordTokenSerializer, SetForgetPasswordSerializer, ChangePasswordSerializer
from rest_framework.response import Response

class ForgetPasswordRequestView(CreateAPIView):
    serializer_class = ForgetPasswordRequestSerializer

    def post(self, request, *args, **kwargs):
        user = self.serializer_class(data=self.request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response(
            {
                "success" : "Please check your email for the code",
                "success_ar" : "برجاء مراجعة بريدك الالكتروني للحصول على الكود"
            }, status=200
        )

class CheckForgetPasswordTokenView(CreateAPIView):
    serializer_class = CheckForgetPasswordTokenSerializer

    def post(self, request, *args, **kwargs):
        user = self.serializer_class(data=self.request.data)
        user.is_valid(raise_exception=True)
        return Response(
            {
                "success" : "Correct Token, Please set a new password",
                "success_ar" : "كود صحيح، برجاء إدخال كلمة مرور جديدة"
            }, status=200
        )

class SetForgetPasswordView(UpdateAPIView):
    serializer_class = SetForgetPasswordSerializer

    def update(self, request, *args, **kwargs):
        user = self.serializer_class(data=self.request.data)
        user.is_valid(raise_exception=True)
        user.update(user.validated_data)
        return Response(
            {
                "success" : "Password changed successfully",
                "success_ar" : "تم تغيير كلمة المرور بنجاح"
            }, status=200
        )

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        user = self.serializer_class(data=self.request.data, context={'request' : self.request})
        user.is_valid(raise_exception=True)
        user.update(user.validated_data)
        return Response(
            {
                "success" : "Password changed successfully",
                "success_ar" : "تم تغيير كلمة المرور بنجاح"
            }, status=200
        )