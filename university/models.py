from django.db import models


class University(models.Model):
    title = models.CharField(max_length=100, null=True)
    city = models.ForeignKey('school.City', on_delete=models.SET_NULL, null=True, related_name='city_universities',
                             verbose_name='City')
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class Faculty(models.Model):
    title = models.CharField(max_length=100, null=True)
    university = models.ForeignKey('University', on_delete=models.SET_NULL, null=True, related_name='university_faculties',
                                   verbose_name='University')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


class Specialty(models.Model):
    title = models.CharField(max_length=100, null=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True, related_name='faculty_specialty',
                                   verbose_name='Faculty')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'
