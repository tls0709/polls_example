from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse




def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# 포트번호/polls/n/
# n번째에 대한 정보(question)를 보여주는거
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
#                                                    #키     #밸류


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return  render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})






