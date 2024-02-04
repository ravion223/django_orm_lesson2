from django.db import models

# Create your models here.


class User(models.Model):
    class Role(models.TextChoices):
        admin = "admin", "ADMIN"
        user = "user", "USER"

    login = models.CharField(max_length=63, unique=True)
    email = models.EmailField()
    role = models.CharField(max_length=63, choices=Role.choices, default=Role.user)
    tasks = models.ManyToManyField("Task")

    def __str__(self):
        return self.login
    

class Task(models.Model):
    status = models.CharField(max_length = 63, choices=[("done", "DONE"), ("processing", "PROCESSING"), ("no work", "NO WORK")], default=("no work", "NO WORK"))
    title = models.CharField(max_length = 63)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
