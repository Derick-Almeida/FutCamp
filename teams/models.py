from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    mascot = models.CharField(max_length=150)
    team_foundation_year = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    coach = models.OneToOneField("coachs.Coach", on_delete=models.CASCADE)
    stadium = models.OneToOneField("stadiums.Stadium", on_delete=models.CASCADE)
