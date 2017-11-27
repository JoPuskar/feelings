from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.HiddenField(default='')

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name',
                  'email', 'last_login', 'date_joined')
        read_only_fields = ('username', 'last_login', 'date_joined',)

    def create(self, validated_data):
        validated_data['password'] = self.context['request'].data['password']
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        try:
            del validated_data['username']
        except KeyError:
            pass
        return super().update(self, validated_data)

