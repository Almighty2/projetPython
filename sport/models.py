from django.db import models

# Create your models here.
class Users(models.Model):
    nom=models.CharField(max_length=255)
    pseudo=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    password_confirm=models.CharField(max_length=50)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom+"    "+self.pseudo


class Football(models.Model):
    club=models.CharField(max_length=255)
    la_mise=models.CharField(max_length=255,default=None)
    score = models.CharField(max_length=255)
    def __str__(self):
        return self.club

class Bolleyball(models.Model):
    club=models.CharField(max_length=255)
    la_mise=models.CharField(max_length=255,default=None)
    score = models.CharField(max_length=255)
    def __str__(self):
        return self.club


class Rugby(models.Model):
    club=models.CharField(max_length=255)
    la_mise=models.CharField(max_length=255,default=None)
    score = models.CharField(max_length=255)
    def __str__(self):
        return self.club

class Cyclisme(models.Model):
    club=models.CharField(max_length=255)
    la_mise=models.CharField(max_length=255,default=None)
    score = models.CharField(max_length=255)
    def __str__(self):
        return self.club

class Running(models.Model):
    club=models.CharField(max_length=255)
    la_mise=models.CharField(max_length=255,default=None)
    score = models.CharField(max_length=255)
    def __str__(self):
        return self.club
 
class Basketball(models.Model):
    club=models.CharField(max_length=255)
    la_mise=models.CharField(max_length=255,default=None)
    score=models.CharField(max_length=255)
    def __str__(self):
        return self.club

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username
         

 
