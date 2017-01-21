from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=1024)
    date = models.CharField(max_length=8)

    def __str__(self):
        return "Question: " + str(self.pk) + " - " + self.date + " - " + self.question_text

class Response(models.Model):
    user = models.ForeignKey("users.User")
    question = models.ForeignKey("questions.Question")
    response_text = models.CharField(max_length=4096)
    created = models.DateTimeField(editable=False)

    # http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        return super(Response, self).save(*args, **kwargs)

    def __str__(self):
        return "Response: " + str(self.pk) + " - User: " + self.user.pk
