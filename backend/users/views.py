from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.views import Response
from .serializers import UserSerializer
from .models import User


class MyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(MyUser, self).retrieve(request, pk)