from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=1024)
    date = models.CharField(max_length=8)

    def __str__(self):
        return "Question: " + str(self.pk) + ' - ' + self.date + ' - ' + self.question_text
