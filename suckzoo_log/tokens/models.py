from django.db import models

class Token(models.Model):
    issuer = models.ForeignKey('users.User')
    serial = models.CharField(max_length=12)

