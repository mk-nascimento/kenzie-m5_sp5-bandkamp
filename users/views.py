from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .permissions import IsAccountOwner
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs.get(self.lookup_field))
