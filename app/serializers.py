# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для пользователя.

    Сериализует основные поля пользователя, такие как id, username, email,
    first_name и last_name.

    Поля:
    - id (число): уникальный идентификатор пользователя (только для чтения)
    - username (строка): уникальное имя пользователя
    - email (строка): адрес электронной почты пользователя
    - first_name (строка, опционально): имя пользователя
    - last_name (строка, опционально): фамилия пользователя
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя.

    Данный сериализатор используется для создания нового пользователя.
    Требует передачи полей username, email и password для регистрации.

    Поля:
    - username (строка): уникальное имя пользователя
    - email (строка): адрес электронной почты пользователя
    - password (строка): пароль пользователя (только для записи)
    - first_name (строка, опционально): имя пользователя
    - last_name (строка, опционально): фамилия пользователя

    При успешной регистрации создает пользователя с использованием
    метода create().
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        """
        Создание нового пользователя.

        Метод create() создает нового пользователя на основе переданных
        проверенных данных. Использует метод create_user() модели User
        для создания пользователя.

        Параметры:
        - validated_data (словарь): проверенные данные пользователя

        Возвращает созданного пользователя.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
