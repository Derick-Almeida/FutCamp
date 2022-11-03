from rest_framework import serializers

from .models import User

#from teams.serializer import TeamsSerializer
#from players.serializer import PlayersSerializer
#from championships.serializer import ChampionshipsSerializer

class UserSerializer (serializers.ModelSerializer):
    
    #favorite_teams = TeamsSerializer(many = True)
    #favorite_players = PlayersSerializer(many = True)
    #favorite_championships = ChampionshipsSerializer(many = True)
    

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "birth_date", 
            "is_superuser", 
            "is_active", 
            "genre", 
            "created_at",
            "updated_at",
            "favorite_teams",
            "favorite_players",
            "favorite_championships" 
        ]

        write_only_fields = ["password"]
        read_only_fields = ["id","created_at", "updated_at", "is_superuser", "is_active"]    

    def create (self, validated_data):
        return User.objects.create_user(**validated_data)