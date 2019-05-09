from django.db import models
from django.urls import reverse
from django.utils import timezone


class Question(models.Model):
    topic = models.CharField(max_length=100)
    body = models.CharField(max_length=2500)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic + "\n\n" + self.body + "\n" + str(self.pub_date)

    def get_absolute_url(self):
        return reverse('detail', args = [self.pk])


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.CharField(max_length=2500)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body + "\n" + str(self.pub_date)

    def get_absolute_url(self):
        return reverse('detail', args = [self.question_id])
