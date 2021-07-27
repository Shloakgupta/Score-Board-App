from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_points = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name

class Member(models.Model):
    member_name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_name
