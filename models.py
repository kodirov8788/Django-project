#  Question, Choice, and Submission
#  models for the Polls app


from django.db import models
from django.utils import timezone
import datetime

# Question model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # Returns the question text
    def __str__(self):
        return self.question_text
    # Returns True if the question was published within the last day
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 

# Choice model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # Returns the choice text
    def __str__(self):
        return self.choice_text
    
# Submission model
class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    # Returns the question text and choice text
    def __str__(self):
        return self.question.question_text + ' - ' + self.choice.choice_text
    

