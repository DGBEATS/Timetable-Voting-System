from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 150)
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE) # using question as the foreign key when it's is deleted delete this too
    option_text = models.CharField(max_length = 150)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.option_text
