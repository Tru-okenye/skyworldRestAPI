# models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class Question(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    PROGRAMMING_CHOICES = [
        ('Reactjs', 'Reactjs'),
        ('Vue', 'Vue'),
        ('Angular', 'Angular'),
        ('MySQL', 'MySQL'),
        ('Go', 'Go'),
        ('PHP', 'PHP'),
        ('Java', 'Java'),
        ('Microsoft SQL Server', 'Microsoft SQL Server'),
        ('SQL', 'SQL'),
        ('Postgres', 'Postgres'),
    ]

    fullname = models.CharField(max_length=100, blank=False, null=False)
    email_address = models.EmailField(max_length=100, blank=False, null=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    description = models.TextField(blank=True, null=True)
    programmingStack = models.CharField(max_length=20, choices=PROGRAMMING_CHOICES)
    upload = models.FileField(upload_to="uploads/files", default="", validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.fullname


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    email_address = models.EmailField()
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    programming_stack = models.CharField(max_length=20)
    file_upload = models.FileField(upload_to="uploads/certificates", blank=True, null=True)

    def __str__(self):
        return f"Response for {self.email_address}"
