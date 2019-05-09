from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


class IndexView(generic.ListView):

    context_object_name = 'question_list'
    template_name = 'index.html'

    def get_queryset(self):
        return Question.objects.order_by('-pk')


class QuestionView(generic.DetailView):

    model = Question
    template_name = 'detail.html'

    def get_form(self):
        return AnswerForm(initial={'question': self.kwargs['pk']})


class AddQuestionView(generic.CreateView):

    model = Question
    form_class = QuestionForm
    template_name = 'create.html'


class AnswerView(generic.CreateView):

    model = Answer
    form_class = AnswerForm

    def get(self, request):
        return redirect(reverse('detail', {'pk' : self.kwargs['pk']}))
