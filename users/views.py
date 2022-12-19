from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrCreateOnly

from .models import User
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCreateOnly]
    queryset = User.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = UserSerializer
