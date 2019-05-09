from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('topic', 'body')
        labels = { 'topic': 'Topic', 'body': 'Question'}


class AnswerForm(forms.ModelForm):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['question'].widget = forms.HiddenInput()

    class Meta:
        model = Answer
        fields = ('body', 'question')
        labels = { 'body': 'Answer'}
