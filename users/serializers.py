from rest_framework import serializers

from .models import User
from .utils import TeamSerializer, PlayerSerializer, ChampionshipSerializer
from django.shortcuts import get_object_or_404
from teams.models import Team
from players.models import Player
from championships.models import Championship


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
            "is_superuser",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserEnableDisableSerializer(serializers.ModelSerializer):
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
            "is_superuser",
        ]

    def update(self, instance: User, validated_data: dict) -> User:
        if not instance.is_active and not validated_data["is_active"]:
            raise serializers.ValidationError({"detail": "User is already deactivated"})

        if instance.is_active and validated_data["is_active"]:
            raise serializers.ValidationError({"detail": "User is already active"})

        instance.is_active = validated_data.get("is_active", instance.is_active)

        instance.save()

        return instance


class UserFavoriteDetailSerializer(serializers.ModelSerializer):
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
            "is_superuser",
        ]

    def update(self, instance: User, validated_data: dict) -> User:

        import ipdb
        ipdb.set_trace()

        # print()

        if validated_data["favorite_teams"]:
            teams_id = validated_data.pop("favorite_teams")
            for id in teams_id:
                team = get_object_or_404(Team, id=id)
                instance.favorite_teams.add(team)

        elif validated_data["favorite_players"]:
            players_id = validated_data.pop("favorite_players")
            for id in players_id:
                players = get_object_or_404(Player, id=id)
                instance.favorite_players.add(players)

        elif validated_data["favorite_championships"]:
            championships_id = validated_data.pop("favorite_championships")
            for id in championships_id:
                championships = get_object_or_404(Championship, id=id)
                instance.favorite_championships.add(championships)

        instance.save()

        return instance


class UserFavoriteSerializer(serializers.ModelSerializer):
    favorite_teams = TeamSerializer(many=True, read_only=True)
    favorite_players = PlayerSerializer(many=True, read_only=True)
    favorite_championships = ChampionshipSerializer(many=True, read_only=True)

    class Meta:
        model = User

        fields = (
            "id",
            "favorite_teams",
            "favorite_players",
            "favorite_championships",
        )
        read_only_fields = ["id"]


class Loginserializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
