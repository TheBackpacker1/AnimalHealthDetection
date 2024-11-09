from django.db import models

# Create your models here.

class cheepNecklace(models.Model):
    idNecklace = models.CharField(max_length=60)
    acceleration = models.FloatField()
    gyroscope = models.FloatField()
    pulse = models.IntegerField()
    temperature = models.FloatField()
    time = models.IntegerField()
    def __str__(self):
        return f"idnekless: {self.idNecklace}, acc: {self.acceleration}, gyro: {self.gyroscope}, pulse: {self.pulse}, temp: {self.temperature}, time: {self.time}"