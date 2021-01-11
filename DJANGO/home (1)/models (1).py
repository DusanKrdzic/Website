from django.db import models

class Form(models.Model):
    summary=models.TextField(max_length=200)
