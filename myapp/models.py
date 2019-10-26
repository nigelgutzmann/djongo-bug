from djongo import models

class Universe(models.Model):
    name = models.CharField(max_length=30)
    _id = models.ObjectIdField(primary_key=True)

    def __str__(self):
        return 'Universe: {0}'.format(self.name)


class SolarSystem(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    _id = models.ObjectIdField(primary_key=True)

    def __str__(self):
        return 'Solar System: {0}'.format(self.name)


class Planet(models.Model):
    name = models.CharField(max_length=30)
    solar_system = models.ForeignKey(SolarSystem, on_delete=models.CASCADE)
    _id = models.ObjectIdField(primary_key=True)

    def __str__(self):
        return 'Planet: {0}'.format(self.name)
