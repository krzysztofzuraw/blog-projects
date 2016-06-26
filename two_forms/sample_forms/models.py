from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=30)
    date_questioned = models.DateField()

class Answer(models.Model):
    answer_text = models.CharField(max_length=30)
    date_answered = models.DateField()
    
