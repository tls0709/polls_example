from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/cint:question_id', views.detail, name='detail'),
    path('polls/cint:question_id/vote', views.vote, name='vote'),
    path('polls/cint:question_id/results', views.results, name='results'),
    ]
