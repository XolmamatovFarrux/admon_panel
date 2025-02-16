from django.db import models


class Kurs(models.Model):
    title = models.CharField(max_length=100,verbose_name = 'Cures')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'
        ordering = ['created_at']


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/')
    kurs = models.OneToOneField(Kurs, on_delete= models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Studenslar'
        ordering = ['created_at']


class Teacher(models.Model):
    pass