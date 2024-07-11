# users/views.py
from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    Регистрация нового пользователя.

    Данный эндпоинт позволяет зарегистрировать нового пользователя,
    отправив POST запрос с данными пользователя в формате JSON.

    Параметры запроса:
    - username (строка): уникальное имя пользователя
    - email (строка): адрес электронной почты пользователя
    - password (строка): пароль пользователя

    При успешной регистрации возвращает данные созданного пользователя
    в формате JSON с полем id и username.

    Пример запроса:
    ```
    POST /api/register/
    {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "securepassword"
    }
    ```
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    """
    Управление пользователями.

    Позволяет выполнять операции CRUD (создание, чтение, обновление, удаление)
    пользователей. Требует аутентификации через JWT токен.

    Параметры запроса:
    - username (строка): уникальное имя пользователя
    - email (строка): адрес электронной почты пользователя
    - password (строка): пароль пользователя

    Для доступа к данному API необходим JWT токен.

    Пример запроса:
    ```
    GET /api/users/
    ```
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """
        Получение данных текущего пользователя.

        Возвращает данные о текущем аутентифицированном пользователе.
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
