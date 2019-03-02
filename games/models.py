from django.db import models


class Game(models.Model):
    blue_score = models.IntegerField(default=0)
    orange_score = models.IntegerField(default=0)
    overtime = models.BooleanField(default=False)
    overtime_length = models.IntegerField(default=0)

    def get_game_result(self):
        return f"{self.blue_score}-{self.orange_score}"
