from django.db import models
import uuid

class Coach(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    age = models.PositiveIntegerField()
    biography = models.TextField(max_length=500)
    number_of_titles = models.PositiveIntegerField()
    hometown = models.CharField(max_length=50)
    # att para chave estrangeira 
    current_team = models.CharField(max_length=50)

