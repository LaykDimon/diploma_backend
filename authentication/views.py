from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import UserRegisterSerializer, LogoutSerializer, ProfileSerializer, CustomTokenObtainPairSerializer
from authentication.services.auth import move_refresh_token_to_blacklist
from authentication.services.querysets import CustomUserQueryset


class RegisterUser(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class Logout(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        move_refresh_token_to_blacklist(serializer.data['refresh'])

        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)


class GetProfile(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    lookup_field = "id"

    def get_queryset(self):
        return CustomUserQueryset.get_user_by_id(user_id=self.kwargs['id'])