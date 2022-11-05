from rest_framework import serializers

from .models import User
from .utils import TeamSerializer, PlayerSerializer, ChampionshipSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = (
            "id",
            "name",
            "email",
            "birthdate",
            "genre",
            "is_superuser",
            "is_active",
            "created_at",
            "updated_at",
        )


class UserDetailSerializer(serializers.ModelSerializer):
    favorite_teams = TeamSerializer(many=True, read_only=True)
    favorite_players = PlayerSerializer(many=True, read_only=True)
    favorite_championships = ChampionshipSerializer(many=True, read_only=True)

    class Meta:
        model = User

        fields = (
            "id",
            "name",
            "email",
            "password",
            "birthdate",
            "genre",
            "is_superuser",
            "is_active",
            "created_at",
            "updated_at",
            "favorite_teams",
            "favorite_players",
            "favorite_championships",
        )
        extra_kwargs = {"password": {"write_only": True}}

        read_only_fields = [
            "created_at",
            "updated_at",
            "is_active",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class Loginserializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
