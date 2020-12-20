from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class Quiz(models.Model):
    name = models.CharField(max_length=50)


class Question(models.Model):
    query = models.CharField(max_length=5000)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)


class Test(models.Model):
    quiz = models.ForeignKey(Quiz, null=False, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, null=False, on_delete=models.DO_NOTHING)
