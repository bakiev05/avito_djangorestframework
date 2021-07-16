from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserSerializer
from users.models import User
from rest_framework import viewsets




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @api_view(['POST'])
    def create_auth(request):
        serialized = UserSerializer(data=request.DATA)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.init_data['username'],
                serialized.init_data['password']
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)