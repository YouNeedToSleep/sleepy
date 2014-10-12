from rest_framework import generics

from sleepy.models.user import User
from sleepy.serializers.user import UserSerializer


class ListView(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
