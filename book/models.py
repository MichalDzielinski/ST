from django.db import models
from authors.models import Author 


class Book(models.Model):

    class STATUS_CHOICES(models.TextChoices):

        WANTED = 'Wanted', 'wanted'
        WAITING= 'Waiting','waiting'
        READING = 'Reading','reding'
        READ = 'Read', 'read'


    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books',on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES.WAITING)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)
