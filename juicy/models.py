from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)


class Mouse(models.Model):
    university = models.ForeignKey('university.University', null=True, on_delete=models.CASCADE)
    type_in = models.CharField(max_length=200, null=True, blank=True)
    color = models.IntegerField(null=True)


class Computer(models.Model):
    university = models.ForeignKey('university.University', null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('authorize.User', null=True, on_delete=models.CASCADE)
    faculty = models.ForeignKey('university.Faculty', null=True, on_delete=models.CASCADE)
    specialty = models.ForeignKey('university.Specialty', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
