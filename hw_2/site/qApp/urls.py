from django.urls import path

from .views import IndexView, QuestionView, AnswerView, AddQuestionView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('question/', IndexView.as_view(), name='index'),
    path('question/create', AddQuestionView.as_view(), name='create'),
    path('question/<int:pk>/answer', AnswerView.as_view(), name='answer'),
    path('question/<int:pk>', QuestionView.as_view(), name='detail'),
]
