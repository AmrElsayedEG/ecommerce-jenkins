class UpdatePasswordMixin:
    def update(self, validated_data):
        user = validated_data.get('user')
        user.set_password(validated_data.get('password'))
        user.requested_token = None
        user.save()
        return user

class TranslateTitleMixin:
    def to_representation(self, instance):
        result = super().to_representation(instance)
        if self.context['request'].LANGUAGE_CODE == 'en':
            result['title'] = instance.title_en
        return result

class TranslateProductMixin:
    def to_representation(self, instance):
        result = super().to_representation(instance)
        if self.context['request'].LANGUAGE_CODE == 'en':
            result['title'] = instance.title_en
            result['description'] = instance.description_en
            result['small_unit'] = instance.small_unit_en
        return result

class TranslateBannerMixin:
    def to_representation(self, instance):
        result = super().to_representation(instance)
        if self.context['request'].LANGUAGE_CODE == 'en':
            result['title'] = instance.title_en
            result['image'] = instance.image_en.url
        return result