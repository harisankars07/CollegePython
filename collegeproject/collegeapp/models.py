from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_url = models.URLField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name