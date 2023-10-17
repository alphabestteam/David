from django.db import models


class Target(models.Model):
    name = models.CharField(max_length=100)
    attack_priority = models.PositiveIntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    enemy_organization = models.CharField(max_length=100)
    target_goal = models.CharField(max_length=100)
    was_target_destroyed = models.BooleanField()
    target_id = models.IntegerField(primary_key=True, null=False)

    # Implement here a target model with a __str__ function
    def __str__(self):
        return (f"Name: {self.name}, Priority: {self.attack_priority}, Lat: {self.latitude}, Long: {self.longitude}, "
                f"Organization: {self.enemy_organization}, Designation: {self.target_goal}, Damaged: {self.was_target_destroyed}, Target ID: {self.target_id}")
