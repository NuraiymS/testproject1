from django.db import models

# Create your models here.

class Course(models.Model):
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = 'Kursy'
    name = models.CharField(max_length=100, verbose_name='Nazvanie')

    def __str__(self):
        return self.name

class Student(models.Model):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Studenty'
    name = models.CharField('Nazvanie', max_length=255, blank=False)
    age = models.IntegerField('Vozrast', default=20, blank=False)
    birthday = models.DateField('Data rojdenia', null=True, blank=True)
    course = models.ForeignKey(Course, verbose_name='Kurs', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

