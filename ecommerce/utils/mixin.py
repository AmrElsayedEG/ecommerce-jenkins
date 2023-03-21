class UpdatePasswordMixin:
    def update(self, validated_data):
        user = validated_data.get('user')
        user.set_password(validated_data.get('password'))
        user.requested_token = None
        user.save()
        return user