from django.db import models

from school.models import SubjectFirst, SubjectSecond


class University(models.Model):
    title = models.CharField(max_length=100, null=True)
    city = models.ForeignKey('school.City', on_delete=models.SET_NULL, null=True, related_name='city_universities',
                             verbose_name='City')
    address = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, verbose_name='Photo')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class Stuff(models.Model):
    bio = models.CharField(max_length=100, null=True)
    university = models.ForeignKey('University', on_delete=models.SET_NULL, null=True, related_name='university_stuff',
                             verbose_name='University')
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True, related_name='faculty_stuff',
                                   verbose_name='Faculty')


class Faculty(models.Model):
    title = models.CharField(max_length=100, null=True)
    university = models.ManyToManyField('University', related_name='university_faculties',
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


class GrantPoint(models.Model):
    subject_first = models.ForeignKey(SubjectFirst, on_delete=models.SET_NULL, null=True, related_name='subject_first_grant',
                                        verbose_name='First subject')
    subject_second = models.ForeignKey(SubjectSecond, on_delete=models.SET_NULL, null=True, related_name='subject_second_grant',
                                        verbose_name='Second subject')                                       
    point = models.IntegerField()
    specialty = models.ForeignKey('Specialty', on_delete=models.SET_NULL, null=True, related_name='specialty_grant_point',
                                    verbose_name='Specialty')
    

class Survey(models.Model):
    user = models.ForeignKey('authorize.User', on_delete=models.CASCADE)
    string = models.CharField(max_length=1000, null=True)

class UniversityPassPoint(models.Model):
    university = models.ForeignKey('University', related_name='university_points', on_delete=models.CASCADE,
                                   verbose_name='University')
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True, related_name='faculty_points',
                                   verbose_name='Faculty')
    specialty = models.ForeignKey('Specialty', on_delete=models.SET_NULL, null=True, related_name='specialty_points',
                                    verbose_name='Specialty')                             
    pass_point = models.IntegerField("Pass point for university", null=True, blank=True)


class Motivation(models.Model):
    quote = models.CharField(max_length=1000, null=True)
    