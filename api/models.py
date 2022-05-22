from django.db import models


grades = [('Grade 11', 'Grade 11'), ('Grade 12', 'Grade 12')]
subjects = [('English', 'English'), ('Mathematics', 'Mathematics')]


class Material(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    grade = models.CharField(max_length=25, choices=grades)
    subject = models.CharField(max_length=25, choices=subjects)
